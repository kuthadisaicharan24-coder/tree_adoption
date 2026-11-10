import 'package:flutter_test/flutter_test.dart';
import 'package:tree_adoption/providers/auth_provider.dart';

void main() {
  group('AuthProvider Data Integrity Tests', () {
    late AuthProvider auth;

    setUp(() {
      auth = AuthProvider();
    });

    test('Demo user has accurate initial profile and adopted trees', () async {
      final success = await auth.login('user@treeadoption.org', 'password123');
      expect(success, isTrue);
      expect(auth.userName, 'Sai Charan');
      expect(auth.userEmail, 'user@treeadoption.org');
      expect(auth.userPhone, '+91 98765 43210');
      expect(auth.userBio, isNotEmpty);
      expect(auth.memberSince, '2024');
      expect(auth.treesAdopted, 2);
      expect(auth.adoptedTrees.length, 2);
      expect(auth.isTreeAdopted(1), isTrue); // Oak Tree
      expect(auth.isTreeAdopted(2), isTrue); // Maple Tree
    });

    test('Register preserves full name, phone, and accurate memberSince', () async {
      final success = await auth.register(
        'Pinnelli Avinash',
        'avinash@example.com',
        'secret123',
        'secret123',
        phone: '+91 91234 56789',
      );
      expect(success, isTrue);
      expect(auth.userName, 'Pinnelli Avinash');
      expect(auth.userEmail, 'avinash@example.com');
      expect(auth.userPhone, '+91 91234 56789');
      expect(auth.treesAdopted, 0);
      expect(auth.adoptedTrees, isEmpty);
    });

    test('Adopting a tree updates treesAdopted and stores tree record in profile', () async {
      await auth.register(
        'Jane Doe',
        'jane@example.com',
        'secret123',
        'secret123',
      );

      auth.addAdoptedTree(
        treeId: 3,
        treeName: 'Pine Tree',
        treeSpecies: 'Pinus sylvestris',
        treeIcon: '🌲',
      );

      expect(auth.treesAdopted, 1);
      expect(auth.isTreeAdopted(3), isTrue);
      expect(auth.isTreeAdopted(1), isFalse);
      expect(auth.adoptedTrees.first.name, 'Pine Tree');
      expect(auth.adoptedTrees.first.species, 'Pinus sylvestris');
    });

    test('Logging out and logging back in preserves user name and adopted trees', () async {
      await auth.register(
        'Subramanyam',
        'subbu@example.com',
        'mypassword',
        'mypassword',
        phone: '+91 99887 76655',
      );

      auth.addAdoptedTree(
        treeId: 4,
        treeName: 'Birch Tree',
        treeSpecies: 'Betula pendula',
        treeIcon: '🌿',
      );

      // User logs out
      auth.logout();
      expect(auth.isLoggedIn, isFalse);
      expect(auth.userName, '');
      expect(auth.treesAdopted, 0);

      // User logs back in
      final success = await auth.login('subbu@example.com', 'mypassword');
      expect(success, isTrue);
      expect(auth.isLoggedIn, isTrue);
      // Verify data is completely intact and not overwritten with email prefix
      expect(auth.userName, 'Subramanyam');
      expect(auth.userEmail, 'subbu@example.com');
      expect(auth.userPhone, '+91 99887 76655');
      expect(auth.treesAdopted, 1);
      expect(auth.adoptedTrees.first.name, 'Birch Tree');
    });

    test('Editing profile updates information persistently', () async {
      await auth.login('user@treeadoption.org', 'password123');

      auth.updateProfile(
        name: 'Sai Charan Updated',
        email: 'user@treeadoption.org',
        phone: '+91 90000 00000',
        bio: 'Updated bio for testing',
      );

      expect(auth.userName, 'Sai Charan Updated');
      expect(auth.userPhone, '+91 90000 00000');
      expect(auth.userBio, 'Updated bio for testing');

      auth.logout();
      await auth.login('user@treeadoption.org', 'password123');
      expect(auth.userName, 'Sai Charan Updated');
      expect(auth.userPhone, '+91 90000 00000');
    });
  });
}

