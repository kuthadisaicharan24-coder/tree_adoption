import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';
import '../providers/auth_provider.dart';

class CertificatePage extends StatefulWidget {
  final AdoptedTreeItem? initialTree;

  const CertificatePage({super.key, this.initialTree});

  @override
  State<CertificatePage> createState() => _CertificatePageState();
}

class _CertificatePageState extends State<CertificatePage> {
  AdoptedTreeItem? _selectedTree;

  @override
  void initState() {
    super.initState();
    _selectedTree = widget.initialTree;
  }

  String _generateCertificateId(AdoptedTreeItem item) {
    final year = item.adoptedAt.year;
    final idPad = item.id.toString().padLeft(4, '0');
    return 'CERT-ECO-$year-$idPad';
  }

  void _copyCertId(String certId) {
    Clipboard.setData(ClipboardData(text: certId));
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text('Certificate ID $certId copied to clipboard! 📋'),
        backgroundColor: Colors.green.shade800,
        duration: const Duration(seconds: 2),
      ),
    );
  }

  void _downloadCertificate(String treeName) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text('Certificate for "$treeName" saved successfully! 📥'),
        backgroundColor: Colors.green.shade800,
        duration: const Duration(seconds: 2),
      ),
    );
  }

  void _shareCertificate(String treeName, String certId) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text('Sharing Certificate ($certId) for $treeName... 📤'),
        backgroundColor: Colors.green.shade800,
        duration: const Duration(seconds: 2),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Consumer<AuthProvider>(
      builder: (context, auth, _) {
        final adoptedList = auth.adoptedTrees;

        // If no tree selected yet, pick initial or first
        if (_selectedTree == null && adoptedList.isNotEmpty) {
          _selectedTree = adoptedList.first;
        } else if (_selectedTree != null && !adoptedList.contains(_selectedTree)) {
          // If list changed
          _selectedTree = adoptedList.isNotEmpty ? adoptedList.first : null;
        }

        final tree = _selectedTree;

        return Scaffold(
          backgroundColor: Colors.green.shade50,
          appBar: AppBar(
            title: const Text(
              'Adoption Certificate',
              style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white),
            ),
            backgroundColor: Colors.green.shade700,
            elevation: 0,
            leading: Navigator.canPop(context)
                ? IconButton(
                    icon: const Icon(Icons.arrow_back, color: Colors.white),
                    onPressed: () => Navigator.pop(context),
                  )
                : null,
            actions: [
              if (tree != null)
                IconButton(
                  icon: const Icon(Icons.share, color: Colors.white),
                  tooltip: 'Share Certificate',
                  onPressed: () => _shareCertificate(tree.name, _generateCertificateId(tree)),
                ),
            ],
          ),
          body: adoptedList.isEmpty
              ? Center(
                  child: Padding(
                    padding: const EdgeInsets.all(32),
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Container(
                          width: 90,
                          height: 90,
                          decoration: BoxDecoration(
                            color: Colors.green.shade100,
                            shape: BoxShape.circle,
                          ),
                          child: Icon(Icons.workspace_premium_outlined, size: 50, color: Colors.green.shade700),
                        ),
                        const SizedBox(height: 20),
                        const Text(
                          'No Certificates Yet',
                          style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
                        ),
                        const SizedBox(height: 8),
                        Text(
                          'Adopt a tree to earn your official environmental stewardship certificate verified by the conservation council.',
                          textAlign: TextAlign.center,
                          style: TextStyle(color: Colors.grey.shade600, fontSize: 14, height: 1.4),
                        ),
                        const SizedBox(height: 24),
                        ElevatedButton.icon(
                          style: ElevatedButton.styleFrom(
                            backgroundColor: Colors.green.shade700,
                            padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                          ),
                          onPressed: () {
                            if (Navigator.canPop(context)) {
                              Navigator.pop(context);
                            } else {
                              Navigator.pushReplacementNamed(context, '/home');
                            }
                          },
                          icon: const Icon(Icons.eco, color: Colors.white),
                          label: const Text(
                            'Adopt a Tree Now',
                            style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
                          ),
                        ),
                      ],
                    ),
                  ),
                )
              : SingleChildScrollView(
                  padding: const EdgeInsets.all(16),
                  child: Column(
                    children: [
                      // Tree Selector (if user has adopted multiple trees)
                      if (adoptedList.length > 1) ...[
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 6),
                          decoration: BoxDecoration(
                            color: Colors.white,
                            borderRadius: BorderRadius.circular(12),
                            border: Border.all(color: Colors.green.shade200),
                          ),
                          child: Row(
                            children: [
                              Icon(Icons.park, color: Colors.green.shade700, size: 20),
                              const SizedBox(width: 10),
                              const Text(
                                'Select Tree:',
                                style: TextStyle(fontWeight: FontWeight.bold, fontSize: 13),
                              ),
                              const SizedBox(width: 12),
                              Expanded(
                                child: DropdownButtonHideUnderline(
                                  child: DropdownButton<AdoptedTreeItem>(
                                    value: tree,
                                    isExpanded: true,
                                    icon: Icon(Icons.arrow_drop_down, color: Colors.green.shade700),
                                    items: adoptedList.map((item) {
                                      return DropdownMenuItem<AdoptedTreeItem>(
                                        value: item,
                                        child: Text(
                                          '${item.icon} ${item.name} (${item.species})',
                                          style: const TextStyle(fontSize: 13, fontWeight: FontWeight.w600),
                                          overflow: TextOverflow.ellipsis,
                                        ),
                                      );
                                    }).toList(),
                                    onChanged: (newItem) {
                                      if (newItem != null) {
                                        setState(() => _selectedTree = newItem);
                                      }
                                    },
                                  ),
                                ),
                              ),
                            ],
                          ),
                        ),
                        const SizedBox(height: 16),
                      ],

                      // The Prestigious Certificate Card
                      _buildCertificateCard(tree!, auth.userName),

                      const SizedBox(height: 20),

                      // Efficiency Action Buttons (Download, Print, Copy ID)
                      Row(
                        children: [
                          Expanded(
                            child: ElevatedButton.icon(
                              style: ElevatedButton.styleFrom(
                                backgroundColor: Colors.green.shade700,
                                padding: const EdgeInsets.symmetric(vertical: 14),
                                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                              ),
                              onPressed: () => _downloadCertificate(tree.name),
                              icon: const Icon(Icons.download, color: Colors.white),
                              label: const Text(
                                'Download PDF',
                                style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
                              ),
                            ),
                          ),
                          const SizedBox(width: 12),
                          Expanded(
                            child: OutlinedButton.icon(
                              style: OutlinedButton.styleFrom(
                                side: BorderSide(color: Colors.green.shade700),
                                padding: const EdgeInsets.symmetric(vertical: 14),
                                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                              ),
                              onPressed: () => _copyCertId(_generateCertificateId(tree)),
                              icon: Icon(Icons.copy, color: Colors.green.shade800),
                              label: Text(
                                'Copy Cert ID',
                                style: TextStyle(color: Colors.green.shade900, fontWeight: FontWeight.bold),
                              ),
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 16),
                    ],
                  ),
                ),
        );
      },
    );
  }

  Widget _buildCertificateCard(AdoptedTreeItem item, String userName) {
    final certId = _generateCertificateId(item);
    final dateStr = '${item.adoptedAt.day} ${_monthName(item.adoptedAt.month)} ${item.adoptedAt.year}';
    final recipient = userName.trim().isNotEmpty ? userName.trim() : 'Honored Eco Guardian';

    return Container(
      width: double.infinity,
      decoration: BoxDecoration(
        color: const Color(0xFFFDFBF7), // Certificate ivory parchment
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: const Color(0xFFD4AF37), width: 3), // Gold border
        boxShadow: const [
          BoxShadow(
            color: Colors.black12,
            blurRadius: 12,
            offset: Offset(0, 6),
          ),
        ],
      ),
      padding: const EdgeInsets.all(6), // Outer margin between double borders
      child: Container(
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(12),
          border: Border.all(color: Colors.green.shade800, width: 1.5), // Inner emerald line
        ),
        padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 24),
        child: Column(
          children: [
            // Top Organization Header
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(Icons.eco, color: Colors.green.shade800, size: 28),
                const SizedBox(width: 8),
                Text(
                  'GLOBAL GREEN CONSERVATION INITIATIVE',
                  textAlign: TextAlign.center,
                  style: TextStyle(
                    fontSize: 11,
                    letterSpacing: 1.4,
                    fontWeight: FontWeight.bold,
                    color: Colors.green.shade900,
                  ),
                ),
                const SizedBox(width: 8),
                Icon(Icons.eco, color: Colors.green.shade800, size: 28),
              ],
            ),
            const SizedBox(height: 12),

            // Certificate Title
            Text(
              'CERTIFICATE OF ADOPTION',
              textAlign: TextAlign.center,
              style: TextStyle(
                fontFamily: 'serif',
                fontSize: 22,
                letterSpacing: 2,
                fontWeight: FontWeight.w900,
                color: Colors.green.shade900,
              ),
            ),
            const SizedBox(height: 4),
            Text(
              'ENVIRONMENTAL STEWARDSHIP AWARD',
              textAlign: TextAlign.center,
              style: TextStyle(
                fontSize: 10,
                letterSpacing: 2,
                fontWeight: FontWeight.w600,
                color: Colors.amber.shade900,
              ),
            ),
            const SizedBox(height: 16),

            // Ornamental Divider
            Row(
              children: [
                Expanded(child: Divider(color: Colors.amber.shade700, thickness: 1)),
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 10),
                  child: Icon(Icons.star, color: Colors.amber.shade700, size: 16),
                ),
                Expanded(child: Divider(color: Colors.amber.shade700, thickness: 1)),
              ],
            ),
            const SizedBox(height: 16),

            // Presentation Statement
            const Text(
              'THIS IS PROUDLY PRESENTED TO',
              style: TextStyle(
                fontSize: 11,
                letterSpacing: 1.5,
                fontWeight: FontWeight.w500,
                color: Colors.black54,
              ),
            ),
            const SizedBox(height: 8),

            // Recipient Full Name
            Text(
              recipient,
              textAlign: TextAlign.center,
              style: TextStyle(
                fontFamily: 'serif',
                fontSize: 24,
                fontWeight: FontWeight.bold,
                color: Colors.green.shade900,
                decoration: TextDecoration.underline,
                decorationColor: Colors.amber.shade600,
                decorationThickness: 1.5,
              ),
            ),
            const SizedBox(height: 14),

            // Recognition Paragraph
            Text(
              'In sincere recognition of your distinguished support for reforestation and dedication to planetary biodiversity by adopting and securing the lifetime nurturing of:',
              textAlign: TextAlign.center,
              style: TextStyle(
                fontSize: 12,
                height: 1.5,
                color: Colors.grey.shade800,
              ),
            ),
            const SizedBox(height: 16),

            // Adopted Tree Showcase Box
            Container(
              width: double.infinity,
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
              decoration: BoxDecoration(
                color: Colors.green.shade50,
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: Colors.green.shade300),
              ),
              child: Row(
                children: [
                  Container(
                    width: 50,
                    height: 50,
                    decoration: BoxDecoration(
                      color: Colors.white,
                      shape: BoxShape.circle,
                      border: Border.all(color: Colors.green.shade200),
                    ),
                    child: Center(
                      child: Text(item.icon, style: const TextStyle(fontSize: 28)),
                    ),
                  ),
                  const SizedBox(width: 14),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          item.name,
                          style: TextStyle(
                            fontSize: 17,
                            fontWeight: FontWeight.bold,
                            color: Colors.green.shade900,
                          ),
                        ),
                        Text(
                          'Botanical Species: ${item.species}',
                          style: TextStyle(
                            fontSize: 12,
                            fontStyle: FontStyle.italic,
                            color: Colors.grey.shade700,
                          ),
                        ),
                        const SizedBox(height: 2),
                        Text(
                          'Reserve Sector: Green Valley Nature Reserve • Plot ${item.id}A',
                          style: TextStyle(fontSize: 10, color: Colors.green.shade800),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 16),

            // Guaranteed Eco Impact Pills
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                _buildSmallBadge(Icons.cloud_done, '48 lbs CO2', 'Filtered / Year'),
                _buildSmallBadge(Icons.air, '260 lbs O2', 'Produced / Year'),
                _buildSmallBadge(Icons.verified_user, 'Perpetual', 'Protected Status'),
              ],
            ),
            const SizedBox(height: 20),

            // Date & Certificate ID Row
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    const Text('DATE OF ADOPTION', style: TextStyle(fontSize: 9, letterSpacing: 1, color: Colors.grey)),
                    const SizedBox(height: 2),
                    Text(
                      dateStr,
                      style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold),
                    ),
                  ],
                ),
                Column(
                  crossAxisAlignment: CrossAxisAlignment.end,
                  children: [
                    const Text('CERTIFICATE NUMBER', style: TextStyle(fontSize: 9, letterSpacing: 1, color: Colors.grey)),
                    const SizedBox(height: 2),
                    Text(
                      certId,
                      style: TextStyle(
                        fontSize: 11,
                        fontWeight: FontWeight.bold,
                        color: Colors.green.shade900,
                        letterSpacing: 0.5,
                      ),
                    ),
                  ],
                ),
              ],
            ),
            const SizedBox(height: 20),

            // Golden Seal & Official Signatures Row
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              crossAxisAlignment: CrossAxisAlignment.end,
              children: [
                // Signature 1
                Column(
                  children: [
                    Container(
                      width: 80,
                      height: 26,
                      alignment: Alignment.bottomCenter,
                      child: Text(
                        'M. Chanda',
                        style: TextStyle(
                          fontFamily: 'serif',
                          fontStyle: FontStyle.italic,
                          fontSize: 16,
                          fontWeight: FontWeight.bold,
                          color: Colors.blueGrey.shade800,
                        ),
                      ),
                    ),
                    Container(width: 85, height: 1, color: Colors.black45),
                    const SizedBox(height: 3),
                    const Text(
                      'Chief Forestry Officer',
                      style: TextStyle(fontSize: 9, color: Colors.black54),
                    ),
                  ],
                ),

                // Center Gold Verified Badge
                Container(
                  width: 58,
                  height: 58,
                  decoration: BoxDecoration(
                    color: Colors.amber.shade100,
                    shape: BoxShape.circle,
                    border: Border.all(color: const Color(0xFFD4AF37), width: 2),
                    boxShadow: const [BoxShadow(color: Colors.black12, blurRadius: 4)],
                  ),
                  child: Center(
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Icon(Icons.workspace_premium, color: Colors.amber.shade900, size: 24),
                        Text(
                          'VERIFIED',
                          style: TextStyle(
                            fontSize: 7,
                            fontWeight: FontWeight.w900,
                            letterSpacing: 0.8,
                            color: Colors.amber.shade900,
                          ),
                        ),
                      ],
                    ),
                  ),
                ),

                // Signature 2
                Column(
                  children: [
                    Container(
                      width: 80,
                      height: 26,
                      alignment: Alignment.bottomCenter,
                      child: Text(
                        'P. Subramanyam',
                        style: TextStyle(
                          fontFamily: 'serif',
                          fontStyle: FontStyle.italic,
                          fontSize: 15,
                          fontWeight: FontWeight.bold,
                          color: Colors.blueGrey.shade800,
                        ),
                      ),
                    ),
                    Container(width: 85, height: 1, color: Colors.black45),
                    const SizedBox(height: 3),
                    const Text(
                      'Conservation Director',
                      style: TextStyle(fontSize: 9, color: Colors.black54),
                    ),
                  ],
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildSmallBadge(IconData icon, String title, String subtitle) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 6),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(8),
        border: Border.all(color: Colors.green.shade200),
      ),
      child: Column(
        children: [
          Icon(icon, color: Colors.green.shade700, size: 16),
          const SizedBox(height: 2),
          Text(
            title,
            style: const TextStyle(fontSize: 10, fontWeight: FontWeight.bold),
          ),
          Text(
            subtitle,
            style: TextStyle(fontSize: 8, color: Colors.grey.shade600),
          ),
        ],
      ),
    );
  }

  String _monthName(int month) {
    const months = [
      'January', 'February', 'March', 'April', 'May', 'June',
      'July', 'August', 'September', 'October', 'November', 'December'
    ];
    if (month >= 1 && month <= 12) {
      return months[month - 1];
    }
    return '';
  }
}

