import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/auth_provider.dart';

class ImpactPage extends StatelessWidget {
  const ImpactPage({super.key});

  @override
  Widget build(BuildContext context) {
    final showAppBar = ModalRoute.of(context)?.settings.name == '/impact';

    Widget content = Consumer<AuthProvider>(
      builder: (context, auth, _) {
        final count = auth.treesAdopted;
        final co2Lbs = count * 48;
        final oxygenLbs = count * 260;
        final waterGallons = count * 1000;
        final areaSqM = (count * 12.5).toStringAsFixed(1);

        String badgeName = 'Eco Seedling';
        IconData badgeIcon = Icons.spa;
        double progress = (count / 5).clamp(0.0, 1.0);

        if (count >= 5) {
          badgeName = 'Forest Champion';
          badgeIcon = Icons.military_tech;
          progress = 1.0;
        } else if (count >= 3) {
          badgeName = 'Tree Guardian';
          badgeIcon = Icons.shield;
          progress = count / 5.0;
        } else if (count >= 1) {
          badgeName = 'Green Sprout';
          badgeIcon = Icons.grass;
          progress = count / 5.0;
        }

        return ListView(
          padding: const EdgeInsets.all(16),
          children: [
            // Top Badge / Level Card
            Container(
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  colors: [Colors.green.shade700, Colors.teal.shade800],
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                ),
                borderRadius: BorderRadius.circular(16),
                boxShadow: const [BoxShadow(color: Colors.black12, blurRadius: 8)],
              ),
              child: Column(
                children: [
                  CircleAvatar(
                    radius: 30,
                    backgroundColor: Colors.white24,
                    child: Icon(badgeIcon, size: 36, color: Colors.white),
                  ),
                  const SizedBox(height: 12),
                  Text(
                    badgeName,
                    style: const TextStyle(
                      color: Colors.white,
                      fontSize: 22,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    '$count trees adopted • Active Environmental Steward',
                    style: const TextStyle(color: Colors.white70, fontSize: 13),
                  ),
                  const SizedBox(height: 16),
                  LinearProgressIndicator(
                    value: progress,
                    backgroundColor: Colors.white24,
                    valueColor: const AlwaysStoppedAnimation<Color>(Colors.lightGreenAccent),
                    minHeight: 8,
                    borderRadius: BorderRadius.circular(4),
                  ),
                  const SizedBox(height: 8),
                  Text(
                    count >= 5 ? 'Maximum tier achieved!' : 'Next Milestone: $count/5 trees',
                    style: const TextStyle(color: Colors.white70, fontSize: 12),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 20),

            // Impact Header
            Text(
              'Your Environmental Contributions',
              style: Theme.of(context).textTheme.titleMedium?.copyWith(
                    fontWeight: FontWeight.bold,
                    color: Colors.green.shade900,
                  ),
            ),
            const SizedBox(height: 12),

            // 4 Impact Grid Cards
            Row(
              children: [
                Expanded(
                  child: _buildImpactCard(
                    title: 'CO2 Absorbed',
                    value: '$co2Lbs lbs/yr',
                    icon: Icons.cloud_done,
                    color: Colors.blue.shade700,
                    subtitle: 'Clean air filtered',
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: _buildImpactCard(
                    title: 'Oxygen Produced',
                    value: '$oxygenLbs lbs/yr',
                    icon: Icons.air,
                    color: Colors.teal.shade700,
                    subtitle: 'Breathable oxygen',
                  ),
                ),
              ],
            ),
            const SizedBox(height: 12),
            Row(
              children: [
                Expanded(
                  child: _buildImpactCard(
                    title: 'Rainwater Conserved',
                    value: '$waterGallons gal/yr',
                    icon: Icons.water_drop,
                    color: Colors.indigo.shade600,
                    subtitle: 'Soil runoff prevented',
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: _buildImpactCard(
                    title: 'Canopy Coverage',
                    value: '$areaSqM sq.m',
                    icon: Icons.park,
                    color: Colors.green.shade700,
                    subtitle: 'Urban shade area',
                  ),
                ),
              ],
            ),
            const SizedBox(height: 24),

            // Green Facts Card
            Card(
              elevation: 2,
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
              child: Padding(
                padding: const EdgeInsets.all(16),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Row(
                      children: [
                        Icon(Icons.lightbulb, color: Colors.amber.shade700),
                        const SizedBox(width: 8),
                        const Text(
                          'Did You Know?',
                          style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                    const SizedBox(height: 10),
                    const Text(
                      '• A single mature tree absorbs carbon dioxide at a rate of 48 pounds per year.\n'
                      '• Two mature trees produce enough oxygen for a family of four.\n'
                      '• Trees planted in cities lower surrounding ambient temperatures by up to 5°C.\n'
                      '• Planting native trees boosts local biodiversity by providing homes for birds, bees, and butterflies.',
                      style: TextStyle(fontSize: 13, height: 1.6, color: Colors.black87),
                    ),
                  ],
                ),
              ),
            ),
            const SizedBox(height: 20),
          ],
        );
      },
    );

    if (showAppBar) {
      return Scaffold(
        backgroundColor: Colors.green.shade50,
        appBar: AppBar(
          title: const Text('Environmental Impact', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
          backgroundColor: Colors.green.shade700,
          leading: IconButton(
            icon: const Icon(Icons.arrow_back, color: Colors.white),
            onPressed: () => Navigator.pop(context),
          ),
        ),
        body: content,
      );
    }

    return content;
  }

  Widget _buildImpactCard({
    required String title,
    required String value,
    required IconData icon,
    required Color color,
    required String subtitle,
  }) {
    return Container(
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: color.withValues(alpha: 0.3)),
        boxShadow: const [BoxShadow(color: Colors.black12, blurRadius: 4)],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          CircleAvatar(
            radius: 18,
            backgroundColor: color.withValues(alpha: 0.15),
            child: Icon(icon, color: color, size: 20),
          ),
          const SizedBox(height: 10),
          Text(
            value,
            style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: color),
          ),
          const SizedBox(height: 2),
          Text(
            title,
            style: const TextStyle(fontSize: 13, fontWeight: FontWeight.w600, color: Colors.black87),
          ),
          const SizedBox(height: 2),
          Text(
            subtitle,
            style: TextStyle(fontSize: 11, color: Colors.grey.shade600),
          ),
        ],
      ),
    );
  }
}
