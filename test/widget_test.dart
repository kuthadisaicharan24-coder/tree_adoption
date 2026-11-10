import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:tree_adoption/main.dart';

void main() {
  testWidgets('Tree Adoption App launches and navigates to login', (WidgetTester tester) async {
    await tester.pumpWidget(const MyApp());

    // Verify splash page text is shown
    expect(find.text('Tree Adoption'), findsOneWidget);

    // Advance time past the 2-second splash timer
    await tester.pump(const Duration(seconds: 3));
    await tester.pumpAndSettle();

    // Verify login page is now shown
    expect(find.text('Welcome Back'), findsOneWidget);
  });

  testWidgets('Connects all pages through BottomNavigationBar and opens Certificate', (WidgetTester tester) async {
    await tester.pumpWidget(const MyApp());
    await tester.pump(const Duration(seconds: 3));
    await tester.pumpAndSettle();

    // Log in using demo account
    await tester.tap(find.textContaining('user@treeadoption.org'));
    await tester.pumpAndSettle();

    await tester.tap(find.widgetWithText(ElevatedButton, 'Login'));
    await tester.pump(const Duration(seconds: 2));
    await tester.pumpAndSettle();

    // 1. Home / Explore Tab
    expect(find.text('Available Trees'), findsOneWidget);
    expect(find.text('Oak Tree'), findsOneWidget);

    // 2. Switch to My Trees Tab
    await tester.tap(find.byIcon(Icons.forest_outlined));
    await tester.pumpAndSettle();
    expect(find.text('My Forest'), findsOneWidget);

    // Open Certificate page from first tree
    await tester.tap(find.widgetWithText(ElevatedButton, 'Certificate').first);
    await tester.pumpAndSettle();

    // Verify Certificate details
    expect(find.text('CERTIFICATE OF ADOPTION'), findsOneWidget);
    expect(find.text('GLOBAL GREEN CONSERVATION INITIATIVE'), findsOneWidget);
    expect(find.text('Sai Charan'), findsOneWidget);
    expect(find.text('Download PDF'), findsOneWidget);
    expect(find.text('Copy Cert ID'), findsOneWidget);

    // Return to My Trees
    await tester.tap(find.byIcon(Icons.arrow_back));
    await tester.pumpAndSettle();

    // 3. Switch to Impact Tab
    await tester.tap(find.byIcon(Icons.eco_outlined));
    await tester.pumpAndSettle();
    expect(find.text('Your Environmental Contributions'), findsOneWidget);

    // 4. Switch to Profile Tab
    await tester.tap(find.byIcon(Icons.person_outline));
    await tester.pumpAndSettle();
    expect(find.text('My Profile'), findsOneWidget);
    expect(find.text('Sai Charan'), findsAtLeastNWidgets(1));
  });
}
