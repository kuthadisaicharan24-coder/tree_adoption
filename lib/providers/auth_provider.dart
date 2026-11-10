import 'package:flutter/foundation.dart';

class AdoptedTreeItem {
  final int id;
  final String name;
  final String species;
  final String icon;
  final DateTime adoptedAt;

  AdoptedTreeItem({
    required this.id,
    required this.name,
    required this.species,
    required this.icon,
    required this.adoptedAt,
  });
}

class UserModel {
  String name;
  String email;
  String password;
  String phone;
  String bio;
  String memberSince;
  List<AdoptedTreeItem> adoptedTrees;

  UserModel({
    required this.name,
    required this.email,
    required this.password,
    this.phone = '',
    this.bio = '',
    String? memberSince,
    List<AdoptedTreeItem>? adoptedTrees,
  })  : memberSince = memberSince ?? DateTime.now().year.toString(),
        adoptedTrees = adoptedTrees ?? [];
}

class AuthProvider with ChangeNotifier {
  bool _isLoggedIn = false;
  UserModel? _currentUser;
  String _lastError = '';

  // In-memory user database storing registered users and their profile/adoption data
  final Map<String, UserModel> _users = {
    'user@treeadoption.org': UserModel(
      name: 'Sai Charan',
      email: 'user@treeadoption.org',
      password: 'password123',
      phone: '+91 98765 43210',
      bio: 'Nature enthusiast committed to planting and adopting trees for a greener tomorrow.',
      memberSince: '2024',
      adoptedTrees: [
        AdoptedTreeItem(
          id: 1,
          name: 'Oak Tree',
          species: 'Quercus robur',
          icon: '🌳',
          adoptedAt: DateTime(2024, 3, 15),
        ),
        AdoptedTreeItem(
          id: 2,
          name: 'Maple Tree',
          species: 'Acer saccharum',
          icon: '🍂',
          adoptedAt: DateTime(2024, 8, 22),
        ),
      ],
    ),
  };

  bool get isLoggedIn => _isLoggedIn;
  String get userName => _currentUser?.name ?? '';
  String get userEmail => _currentUser?.email ?? '';
  String get userPhone => _currentUser?.phone ?? '';
  String get userBio => _currentUser?.bio ?? '';
  int get treesAdopted => _currentUser?.adoptedTrees.length ?? 0;
  String get memberSince => _currentUser?.memberSince ?? '2024';
  List<AdoptedTreeItem> get adoptedTrees => _currentUser?.adoptedTrees ?? [];
  String get lastError => _lastError;

  // Login
  Future<bool> login(String email, String password) async {
    _lastError = '';
    await Future.delayed(const Duration(milliseconds: 600));

    final normalizedEmail = email.trim().toLowerCase();
    final trimmedPassword = password.trim();

    if (normalizedEmail.isEmpty) {
      _lastError = 'Please enter your email';
      return false;
    }
    if (trimmedPassword.isEmpty) {
      _lastError = 'Please enter your password';
      return false;
    }
    if (trimmedPassword.length < 6) {
      _lastError = 'Password must be at least 6 characters';
      return false;
    }

    // Check existing registered user
    if (_users.containsKey(normalizedEmail)) {
      final user = _users[normalizedEmail]!;
      if (user.password != trimmedPassword) {
        _lastError = 'Incorrect password for this account';
        return false;
      }
      _currentUser = user;
      _isLoggedIn = true;
      notifyListeners();
      return true;
    }

    // If account not registered yet, auto-create a profile with nicely formatted name
    final namePart = normalizedEmail.split('@')[0];
    final formattedName = namePart
        .replaceAll(RegExp(r'[._\d]'), ' ')
        .trim()
        .split(' ')
        .where((s) => s.isNotEmpty)
        .map((s) => s[0].toUpperCase() + s.substring(1))
        .join(' ');
    final displayName = formattedName.isNotEmpty ? formattedName : 'Tree Adopter';

    final newUser = UserModel(
      name: displayName,
      email: normalizedEmail,
      password: trimmedPassword,
      phone: '+91 98765 43210',
      bio: 'Tree enthusiast making the world greener one tree at a time.',
      memberSince: DateTime.now().year.toString(),
      adoptedTrees: [],
    );

    _users[normalizedEmail] = newUser;
    _currentUser = newUser;
    _isLoggedIn = true;
    notifyListeners();
    return true;
  }

  // Register
  Future<bool> register(
    String name,
    String email,
    String password,
    String confirmPassword, {
    String phone = '',
  }) async {
    _lastError = '';
    await Future.delayed(const Duration(milliseconds: 600));

    final trimmedName = name.trim();
    final normalizedEmail = email.trim().toLowerCase();
    final trimmedPassword = password.trim();
    final trimmedConfirm = confirmPassword.trim();

    if (trimmedName.isEmpty) {
      _lastError = 'Please enter your full name';
      return false;
    }
    if (normalizedEmail.isEmpty || !normalizedEmail.contains('@')) {
      _lastError = 'Please enter a valid email address';
      return false;
    }
    if (trimmedPassword.length < 6) {
      _lastError = 'Password must be at least 6 characters';
      return false;
    }
    if (trimmedPassword != trimmedConfirm) {
      _lastError = 'Passwords do not match';
      return false;
    }

    final newUser = UserModel(
      name: trimmedName,
      email: normalizedEmail,
      password: trimmedPassword,
      phone: phone.trim().isNotEmpty ? phone.trim() : '+91 98765 43210',
      bio: 'Nature lover passionate about growing trees and green initiatives.',
      memberSince: DateTime.now().year.toString(),
      adoptedTrees: [],
    );

    _users[normalizedEmail] = newUser;
    _currentUser = newUser;
    _isLoggedIn = true;
    notifyListeners();
    return true;
  }

  // Update profile
  void updateProfile({
    required String name,
    required String email,
    required String phone,
    required String bio,
  }) {
    if (_currentUser != null) {
      final oldEmail = _currentUser!.email;
      _currentUser!.name = name.trim();
      _currentUser!.email = email.trim().toLowerCase();
      _currentUser!.phone = phone.trim();
      _currentUser!.bio = bio.trim();

      // If email changed, re-key the map
      if (oldEmail != _currentUser!.email) {
        _users.remove(oldEmail);
        _users[_currentUser!.email] = _currentUser!;
      }
      notifyListeners();
    }
  }

  // Add adopted tree
  void addAdoptedTree({
    int? treeId,
    String? treeName,
    String? treeSpecies,
    String? treeIcon,
  }) {
    if (_currentUser != null) {
      _currentUser!.adoptedTrees.add(
        AdoptedTreeItem(
          id: treeId ?? (_currentUser!.adoptedTrees.length + 1),
          name: treeName ?? 'Adopted Tree',
          species: treeSpecies ?? 'Native Species',
          icon: treeIcon ?? '🌳',
          adoptedAt: DateTime.now(),
        ),
      );
      notifyListeners();
    }
  }

  // Check if specific tree is adopted
  bool isTreeAdopted(int treeId) {
    if (_currentUser == null) return false;
    return _currentUser!.adoptedTrees.any((t) => t.id == treeId);
  }

  // Count how many times a tree was adopted by this user
  int getAdoptedCountForTree(int treeId) {
    if (_currentUser == null) return 0;
    return _currentUser!.adoptedTrees.where((t) => t.id == treeId).length;
  }

  // Logout
  void logout() {
    _isLoggedIn = false;
    _currentUser = null;
    _lastError = '';
    notifyListeners();
  }
}
