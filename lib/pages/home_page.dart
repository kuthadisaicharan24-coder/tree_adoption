import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/auth_provider.dart';
import 'adopted_trees_page.dart';
import 'impact_page.dart';
import 'profile_page.dart';
import 'tree_detail_page.dart';
import 'certificate_page.dart';

class HomePage extends StatefulWidget {
  final int initialTabIndex;

  const HomePage({super.key, this.initialTabIndex = 0});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  late int _currentIndex;
  String _searchQuery = '';
  String _selectedCategory = 'All';

  final List<Tree> trees = [
    Tree(
      id: 1,
      name: 'Oak Tree',
      species: 'Quercus robur',
      category: 'Shade',
      description: 'Majestic oak tree perfect for shade and urban air purification.',
      imageUrl: '🌳',
      benefits: 'Provides extensive shade and wildlife habitat (absorbs 48 lbs CO2/yr)',
      co2PerYear: '48 lbs/yr',
      oxygenPerYear: '260 lbs/yr',
      lifespan: '200+ years',
      location: 'North Reserve • Plot A1',
    ),
    Tree(
      id: 2,
      name: 'Maple Tree',
      species: 'Acer saccharum',
      category: 'Flowering',
      description: 'Beautiful maple with vibrant fall colors and eco-rich canopy.',
      imageUrl: '🍂',
      benefits: 'Stunning seasonal display and supports pollinators',
      co2PerYear: '42 lbs/yr',
      oxygenPerYear: '240 lbs/yr',
      lifespan: '150+ years',
      location: 'East Valley • Plot B3',
    ),
    Tree(
      id: 3,
      name: 'Pine Tree',
      species: 'Pinus sylvestris',
      category: 'Evergreen',
      description: 'Evergreen pine providing year-round green beauty and shelter.',
      imageUrl: '🌲',
      benefits: 'Provides shelter and produces refreshing pine oxygen',
      co2PerYear: '50 lbs/yr',
      oxygenPerYear: '280 lbs/yr',
      lifespan: '120+ years',
      location: 'Highland Ridge • Plot C2',
    ),
    Tree(
      id: 4,
      name: 'Birch Tree',
      species: 'Betula pendula',
      category: 'Shade',
      description: 'Elegant tree with distinctive white bark and graceful branches.',
      imageUrl: '🌿',
      benefits: 'Beautiful aesthetic, prevents soil erosion, and filters rainwater',
      co2PerYear: '38 lbs/yr',
      oxygenPerYear: '210 lbs/yr',
      lifespan: '80+ years',
      location: 'Riverbank • Plot D4',
    ),
  ];

  @override
  void initState() {
    super.initState();
    _currentIndex = widget.initialTabIndex;
  }

  void _showAboutDialog() {
    showDialog(
      context: context,
      builder: (ctx) => AlertDialog(
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
        title: Row(
          children: [
            Icon(Icons.eco, color: Colors.green.shade700),
            const SizedBox(width: 8),
            const Text('About Tree Adoption'),
          ],
        ),
        content: const Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'Tree Adoption App',
              style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16),
            ),
            SizedBox(height: 4),
            Text('Version 1.0.0', style: TextStyle(color: Colors.grey, fontSize: 12)),
            SizedBox(height: 12),
            Text(
              'A digital conservation platform connecting nature enthusiasts with tree adoption initiatives. Users can adopt trees, track their personal forest growth, and measure positive environmental impact in real time.',
              style: TextStyle(fontSize: 13, height: 1.4),
            ),
            SizedBox(height: 12),
            Divider(),
            Text(
              'JNTU Vizianagaram\nDepartment of Computer Science & Engineering',
              style: TextStyle(fontSize: 11, color: Colors.grey, fontStyle: FontStyle.italic),
            ),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(ctx),
            child: const Text('Close'),
          ),
        ],
      ),
    );
  }

  void _logout() {
    showDialog(
      context: context,
      builder: (ctx) => AlertDialog(
        title: const Text('Logout'),
        content: const Text('Are you sure you want to logout?'),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(ctx),
            child: const Text('Cancel'),
          ),
          TextButton(
            onPressed: () {
              Navigator.pop(ctx);
              final authProvider = Provider.of<AuthProvider>(context, listen: false);
              authProvider.logout();
              Navigator.of(context).pushReplacementNamed('/login');
            },
            child: const Text('Logout', style: TextStyle(color: Colors.red)),
          ),
        ],
      ),
    );
  }

  Widget _buildExploreTab(AuthProvider auth) {
    final filteredTrees = trees.where((tree) {
      final matchesSearch = tree.name.toLowerCase().contains(_searchQuery.toLowerCase()) ||
          tree.species.toLowerCase().contains(_searchQuery.toLowerCase()) ||
          tree.benefits.toLowerCase().contains(_searchQuery.toLowerCase());
      final matchesCategory = _selectedCategory == 'All' || tree.category == _selectedCategory;
      return matchesSearch && matchesCategory;
    }).toList();

    return Column(
      children: [
        // Welcome Header Banner
        Container(
          width: double.infinity,
          padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 16),
          color: Colors.green.shade700,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                'Welcome, ${auth.userName.isNotEmpty ? auth.userName : "Eco Friend"}!',
                style: const TextStyle(
                  color: Colors.white,
                  fontSize: 22,
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 6),
              Row(
                children: [
                  const Icon(Icons.eco, color: Colors.lightGreenAccent, size: 18),
                  const SizedBox(width: 6),
                  Text(
                    '${auth.treesAdopted} trees adopted so far',
                    style: const TextStyle(color: Colors.white70, fontSize: 14),
                  ),
                  const Spacer(),
                  InkWell(
                    onTap: () => setState(() => _currentIndex = 1),
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                      decoration: BoxDecoration(
                        color: Colors.white24,
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: const Text(
                        'View Forest →',
                        style: TextStyle(color: Colors.white, fontSize: 12, fontWeight: FontWeight.bold),
                      ),
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),

        // Search & Category Bar
        Container(
          color: Colors.white,
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
          child: Column(
            children: [
              TextField(
                onChanged: (val) => setState(() => _searchQuery = val),
                decoration: InputDecoration(
                  hintText: 'Search trees by name, species...',
                  prefixIcon: const Icon(Icons.search, size: 20),
                  contentPadding: const EdgeInsets.symmetric(vertical: 0, horizontal: 16),
                  filled: true,
                  fillColor: Colors.green.shade50,
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(12),
                    borderSide: BorderSide.none,
                  ),
                ),
              ),
              const SizedBox(height: 8),
              SingleChildScrollView(
                scrollDirection: Axis.horizontal,
                child: Row(
                  children: ['All', 'Shade', 'Flowering', 'Evergreen'].map((category) {
                    final isSelected = _selectedCategory == category;
                    return Padding(
                      padding: const EdgeInsets.only(right: 8),
                      child: ChoiceChip(
                        label: Text(category),
                        selected: isSelected,
                        onSelected: (_) => setState(() => _selectedCategory = category),
                        selectedColor: Colors.green.shade700,
                        labelStyle: TextStyle(
                          color: isSelected ? Colors.white : Colors.green.shade900,
                          fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
                          fontSize: 12,
                        ),
                        backgroundColor: Colors.green.shade50,
                      ),
                    );
                  }).toList(),
                ),
              ),
            ],
          ),
        ),

        // Trees List
        Expanded(
          child: filteredTrees.isEmpty
              ? Center(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Icon(Icons.search_off, size: 48, color: Colors.grey.shade400),
                      const SizedBox(height: 8),
                      Text(
                        'No trees found matching "$_searchQuery"',
                        style: TextStyle(color: Colors.grey.shade600),
                      ),
                    ],
                  ),
                )
              : ListView.builder(
                  padding: const EdgeInsets.all(16),
                  itemCount: filteredTrees.length,
                  itemBuilder: (context, index) {
                    final tree = filteredTrees[index];
                    final isAdopted = auth.isTreeAdopted(tree.id);
                    final adoptCount = auth.getAdoptedCountForTree(tree.id);

                    return TreeCard(
                      tree: tree,
                      isAdopted: isAdopted,
                      adoptionCount: adoptCount,
                      onTap: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) => TreeDetailPage(tree: tree),
                          ),
                        );
                      },
                      onAdopt: () {
                        _adoptTree(tree);
                      },
                    );
                  },
                ),
        ),
      ],
    );
  }

  void _adoptTree(Tree tree) {
    final authProvider = Provider.of<AuthProvider>(context, listen: false);
    authProvider.addAdoptedTree(
      treeId: tree.id,
      treeName: tree.name,
      treeSpecies: tree.species,
      treeIcon: tree.imageUrl,
    );

    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text('You adopted ${tree.name}! 🎉 Added to "My Trees" tab.'),
        backgroundColor: Colors.green.shade700,
        action: SnackBarAction(
          label: 'View',
          textColor: Colors.lightGreenAccent,
          onPressed: () => setState(() => _currentIndex = 1),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final auth = Provider.of<AuthProvider>(context);

    final titles = [
      'Available Trees',
      'My Adopted Trees',
      'Environmental Impact',
      'My Profile',
    ];

    final pages = [
      _buildExploreTab(auth),
      AdoptedTreesPage(onExploreTap: () => setState(() => _currentIndex = 0)),
      const ImpactPage(),
      const ProfilePage(isEmbedded: true),
    ];

    return Scaffold(
      backgroundColor: Colors.green.shade50,
      appBar: AppBar(
        title: Text(
          titles[_currentIndex],
          style: const TextStyle(fontWeight: FontWeight.bold, color: Colors.white),
        ),
        backgroundColor: Colors.green.shade700,
        elevation: 0,
        iconTheme: const IconThemeData(color: Colors.white),
        actions: [
          if (_currentIndex != 3)
            IconButton(
              icon: const Icon(Icons.person, color: Colors.white),
              tooltip: 'Go to Profile',
              onPressed: () => setState(() => _currentIndex = 3),
            ),
        ],
      ),

      // Navigation Drawer connecting all pages
      drawer: Drawer(
        child: Column(
          children: [
            UserAccountsDrawerHeader(
              decoration: BoxDecoration(
                color: Colors.green.shade800,
              ),
              currentAccountPicture: CircleAvatar(
                backgroundColor: Colors.green.shade200,
                child: Text(
                  auth.userName.isNotEmpty ? auth.userName[0].toUpperCase() : 'U',
                  style: TextStyle(
                    fontSize: 26,
                    fontWeight: FontWeight.bold,
                    color: Colors.green.shade900,
                  ),
                ),
              ),
              accountName: Text(
                auth.userName.isNotEmpty ? auth.userName : 'Tree Adopter',
                style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16),
              ),
              accountEmail: Text(auth.userEmail),
            ),
            ListTile(
              leading: Icon(Icons.park, color: _currentIndex == 0 ? Colors.green.shade700 : Colors.grey.shade700),
              title: const Text('Explore Trees'),
              selected: _currentIndex == 0,
              onTap: () {
                Navigator.pop(context);
                setState(() => _currentIndex = 0);
              },
            ),
            ListTile(
              leading: Icon(Icons.forest, color: _currentIndex == 1 ? Colors.green.shade700 : Colors.grey.shade700),
              title: const Text('My Adopted Trees'),
              trailing: auth.treesAdopted > 0
                  ? Badge(label: Text('${auth.treesAdopted}'), backgroundColor: Colors.green)
                  : null,
              selected: _currentIndex == 1,
              onTap: () {
                Navigator.pop(context);
                setState(() => _currentIndex = 1);
              },
            ),
            ListTile(
              leading: Icon(Icons.eco, color: _currentIndex == 2 ? Colors.green.shade700 : Colors.grey.shade700),
              title: const Text('Environmental Impact'),
              selected: _currentIndex == 2,
              onTap: () {
                Navigator.pop(context);
                setState(() => _currentIndex = 2);
              },
            ),
            ListTile(
              leading: Icon(Icons.person, color: _currentIndex == 3 ? Colors.green.shade700 : Colors.grey.shade700),
              title: const Text('My Profile'),
              selected: _currentIndex == 3,
              onTap: () {
                Navigator.pop(context);
                setState(() => _currentIndex = 3);
              },
            ),
            ListTile(
              leading: Icon(Icons.workspace_premium, color: Colors.amber.shade800),
              title: const Text('Adoption Certificates'),
              trailing: auth.treesAdopted > 0
                  ? Badge(label: Text('${auth.treesAdopted}'), backgroundColor: Colors.amber.shade800)
                  : null,
              onTap: () {
                Navigator.pop(context);
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => const CertificatePage()),
                );
              },
            ),
            const Divider(),
            ListTile(
              leading: const Icon(Icons.info_outline),
              title: const Text('About App'),
              onTap: () {
                Navigator.pop(context);
                _showAboutDialog();
              },
            ),
            const Spacer(),
            const Divider(),
            ListTile(
              leading: const Icon(Icons.logout, color: Colors.red),
              title: const Text('Logout', style: TextStyle(color: Colors.red, fontWeight: FontWeight.bold)),
              onTap: () {
                Navigator.pop(context);
                _logout();
              },
            ),
            const SizedBox(height: 12),
          ],
        ),
      ),

      // Main active page body
      body: pages[_currentIndex],

      // Bottom Navigation Bar
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _currentIndex,
        onTap: (index) => setState(() => _currentIndex = index),
        type: BottomNavigationBarType.fixed,
        selectedItemColor: Colors.green.shade800,
        unselectedItemColor: Colors.grey.shade600,
        selectedLabelStyle: const TextStyle(fontWeight: FontWeight.bold, fontSize: 12),
        unselectedLabelStyle: const TextStyle(fontSize: 12),
        backgroundColor: Colors.white,
        elevation: 8,
        items: [
          const BottomNavigationBarItem(
            icon: Icon(Icons.park_outlined),
            activeIcon: Icon(Icons.park),
            label: 'Explore',
          ),
          BottomNavigationBarItem(
            icon: Badge(
              isLabelVisible: auth.treesAdopted > 0,
              label: Text('${auth.treesAdopted}'),
              child: const Icon(Icons.forest_outlined),
            ),
            activeIcon: Badge(
              isLabelVisible: auth.treesAdopted > 0,
              label: Text('${auth.treesAdopted}'),
              child: const Icon(Icons.forest),
            ),
            label: 'My Trees',
          ),
          const BottomNavigationBarItem(
            icon: Icon(Icons.eco_outlined),
            activeIcon: Icon(Icons.eco),
            label: 'Impact',
          ),
          const BottomNavigationBarItem(
            icon: Icon(Icons.person_outline),
            activeIcon: Icon(Icons.person),
            label: 'Profile',
          ),
        ],
      ),
    );
  }
}

class Tree {
  final int id;
  final String name;
  final String species;
  final String category;
  final String description;
  final String imageUrl;
  final String benefits;
  final String co2PerYear;
  final String oxygenPerYear;
  final String lifespan;
  final String location;

  Tree({
    required this.id,
    required this.name,
    required this.species,
    this.category = 'Native',
    required this.description,
    required this.imageUrl,
    required this.benefits,
    this.co2PerYear = '48 lbs/yr',
    this.oxygenPerYear = '260 lbs/yr',
    this.lifespan = '100+ years',
    this.location = 'Green Reserve Sector A',
  });
}

class TreeCard extends StatelessWidget {
  final Tree tree;
  final bool isAdopted;
  final int adoptionCount;
  final VoidCallback onAdopt;
  final VoidCallback onTap;

  const TreeCard({
    super.key,
    required this.tree,
    required this.isAdopted,
    required this.adoptionCount,
    required this.onAdopt,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.only(bottom: 16),
      elevation: 3,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(12),
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Tree Image/Icon Container with Badge
              Stack(
                children: [
                  Container(
                    width: double.infinity,
                    padding: const EdgeInsets.symmetric(vertical: 24),
                    decoration: BoxDecoration(
                      color: Colors.green.shade100,
                      borderRadius: BorderRadius.circular(12),
                    ),
                    child: Center(
                      child: Text(
                        tree.imageUrl,
                        style: const TextStyle(fontSize: 60),
                      ),
                    ),
                  ),
                  if (isAdopted)
                    Positioned(
                      top: 10,
                      right: 10,
                      child: Container(
                        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                        decoration: BoxDecoration(
                          color: Colors.green.shade800,
                          borderRadius: BorderRadius.circular(20),
                          boxShadow: const [
                            BoxShadow(color: Colors.black26, blurRadius: 4),
                          ],
                        ),
                        child: Row(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            const Icon(Icons.check_circle, color: Colors.white, size: 14),
                            const SizedBox(width: 4),
                            Text(
                              adoptionCount > 1 ? 'Adopted ($adoptionCount)' : 'Adopted',
                              style: const TextStyle(
                                color: Colors.white,
                                fontSize: 12,
                                fontWeight: FontWeight.bold,
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),
                  Positioned(
                    bottom: 8,
                    right: 8,
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                      decoration: BoxDecoration(
                        color: Colors.white.withValues(alpha: 0.85),
                        borderRadius: BorderRadius.circular(8),
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Icon(Icons.info_outline, size: 12, color: Colors.green.shade900),
                          const SizedBox(width: 4),
                          Text(
                            'Details',
                            style: TextStyle(fontSize: 10, color: Colors.green.shade900, fontWeight: FontWeight.bold),
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 14),
              // Tree Name
              Text(
                tree.name,
                style: Theme.of(context).textTheme.titleLarge?.copyWith(
                      fontWeight: FontWeight.bold,
                      color: Colors.green.shade800,
                    ),
              ),
              const SizedBox(height: 2),
              // Species
              Text(
                'Species: ${tree.species}',
                style: Theme.of(context).textTheme.bodySmall?.copyWith(
                      color: Colors.grey.shade600,
                      fontStyle: FontStyle.italic,
                    ),
              ),
              const SizedBox(height: 10),
              // Description
              Text(
                tree.description,
                style: Theme.of(context).textTheme.bodyMedium,
                maxLines: 2,
                overflow: TextOverflow.ellipsis,
              ),
              const SizedBox(height: 12),
              // Benefits
              Container(
                padding: const EdgeInsets.all(10),
                decoration: BoxDecoration(
                  color: Colors.green.shade50,
                  borderRadius: BorderRadius.circular(8),
                  border: Border.all(color: Colors.green.shade200),
                ),
                child: Row(
                  children: [
                    Icon(Icons.eco, color: Colors.green.shade700, size: 18),
                    const SizedBox(width: 8),
                    Expanded(
                      child: Text(
                        tree.benefits,
                        style: Theme.of(context).textTheme.bodySmall,
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 14),
              // Action Buttons
              Row(
                children: [
                  Expanded(
                    child: ElevatedButton.icon(
                      style: ElevatedButton.styleFrom(
                        backgroundColor: isAdopted ? Colors.green.shade800 : Colors.green.shade700,
                        padding: const EdgeInsets.symmetric(vertical: 12),
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
                      ),
                      onPressed: onAdopt,
                      icon: Icon(
                        isAdopted ? Icons.add_circle_outline : Icons.favorite,
                        color: Colors.white,
                        size: 18,
                      ),
                      label: Text(
                        isAdopted ? 'Adopt Another' : 'Adopt This Tree',
                        style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
                      ),
                    ),
                  ),
                  const SizedBox(width: 8),
                  IconButton.filledTonal(
                    onPressed: onTap,
                    tooltip: 'View Details',
                    icon: const Icon(Icons.arrow_forward),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
