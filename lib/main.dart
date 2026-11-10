import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'providers/auth_provider.dart';
import 'pages/login_page.dart';
import 'pages/register_page.dart';
import 'pages/home_page.dart';
import 'pages/profile_page.dart';
import 'pages/splash_page.dart';
import 'pages/adopted_trees_page.dart';
import 'pages/impact_page.dart';
import 'pages/certificate_page.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => AuthProvider()),
      ],
      child: MaterialApp(
        title: 'Tree Adoption App',
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
          colorScheme: ColorScheme.fromSeed(
            seedColor: Colors.green,
            primary: Colors.green.shade700,
          ),
          useMaterial3: true,
          scaffoldBackgroundColor: Colors.green.shade50,
          appBarTheme: AppBarTheme(
            backgroundColor: Colors.green.shade700,
            foregroundColor: Colors.white,
            elevation: 0,
            centerTitle: true,
          ),
        ),
        home: const SplashPage(),
        routes: {
          '/login': (context) => const LoginPage(),
          '/register': (context) => const RegisterPage(),
          '/home': (context) => const HomePage(),
          '/profile': (context) => const ProfilePage(),
          '/my-trees': (context) => const AdoptedTreesPage(),
          '/impact': (context) => const ImpactPage(),
          '/certificate': (context) => const CertificatePage(),
        },
      ),
    );
  }
}
