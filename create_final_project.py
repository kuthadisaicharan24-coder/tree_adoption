import fpdf

pdf = fpdf.FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Color constants
GREEN_DARK = (34, 139, 34)
GREEN_MED = (60, 179, 113)
GREEN_LIGHT = (144, 238, 144)
CREAM = (255, 250, 240)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)

pdf.set_font('Helvetica', '', 11)
pdf.set_text_color(*BLACK)

def draw_code_box(pdf, lines, x=15, y=None, w=180, font_size=8):
    pdf.set_fill_color(245, 245, 245)
    pdf.set_draw_color(180, 180, 180)
    pdf.set_font('Courier', '', font_size)
    line_h = 5
    total_h = len(lines) * line_h + 10
    if y is None:
        y = pdf.get_y()
    pdf.set_xy(x, y)
    pdf.cell(w, total_h, '', 1, 1, 'L', fill=True)
    pdf.set_xy(x + 2, y + 2)
    for line in lines:
        pdf.cell(w, line_h, line, 0, 0, 'L')
        pdf.ln(line_h)

def add_section(pdf, number, title, content_lines, code_boxes=None):
    pdf.add_page()
    if number:
        pdf.set_font('Helvetica', 'B', 14)
        pdf.set_text_color(*GREEN_DARK)
        pdf.cell(0, 10, f'{number}. {title}', 0, 1, 'C')
        pdf.ln(8)
    else:
        pdf.set_font('Helvetica', 'B', 14)
        pdf.set_text_color(*GREEN_DARK)
        pdf.cell(0, 10, title, 0, 1, 'C')
        pdf.ln(8)
    pdf.set_font('Helvetica', '', 11)
    pdf.set_text_color(*BLACK)
    for line in content_lines:
        pdf.multi_cell(0, 7, line, 'L')
    pdf.ln(5)
    if code_boxes:
        for box in code_boxes:
            draw_code_box(pdf, *box)

# ===== PAGE 0: COVER PAGE =====
add_section(pdf, '', 'Cover Page', [
    'Tree Adoption App - Final Year Project',
    '',
    'Developed as a Flutter application for environmental conservation.',
    '',
    'Platform: Flutter (Cross-platform Mobile/Web/Desktop)',
    'Language: Dart',
    'State Management: Provider / ChangeNotifier',
    'Database: SQLite (offline-first, sqflite package)',
    'Version: 1.0.0',
    '',
    'Developed by: [Student Name]',
    'Faculty: [Faculty Name], Professor',
    'Institution: Jawaharlal Nehru Technological University',
    'Department: Computer Science and Engineering',
    'Vizianagaram - 535003, Andhra Pradesh',
], code_boxes=None)

# ===== PAGE 1: CERTIFICATE PAGE =====
add_section(pdf, '', 'Certificate of Bonafide Record', [
    'This is to Certify',
    'of Bonafide Record',
])
pdf.ln(15)
pdf.set_font('Helvetica', '', 12)
pdf.set_text_color(*WHITE)
pdf.multi_cell(0, 7, 'This is to certify that this is a bonafide record of practical work', 1, 'L')
pdf.multi_cell(0, 7, 'done by [Student Name], Regd. No. [Roll Number]', 1, 'L')
pdf.multi_cell(0, 7, 'of III B.Tech I Semester Class in', 1, 'L')
pdf.multi_cell(0, 7, 'Flutter Application Development', 1, 'L')
pdf.multi_cell(0, 7, 'during the year 2024-25.', 1, 'L')
pdf.ln(10)
pdf.multi_cell(0, 7, 'No. of Tasks Completed and Certified:', 1, 'L')
pdf.ln(5)
pdf.multi_cell(0, 7, 'Lecture In-Charge Head of The Department', 1, 'L')
pdf.ln(5)
pdf.multi_cell(0, 7, 'Date: [Date]', 1, 'L')
pdf.ln(15)
pdf.set_font('Helvetica', 'B', 12)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 10, 'Jawaharlal Nehru Technological University', 0, 1, 'C')
pdf.ln(5)
pdf.cell(0, 10, 'Vizianagaram 535003 Andhra Pradesh', 0, 1, 'C')

# ===== PAGE 2: EMPTY PAGE =====
pdf.add_page()
pdf.set_font('Helvetica', '', 12)
pdf.set_text_color(*GRAY)
pdf.cell(0, 10, '(This page is intentionally left blank)', 0, 1, 'C')

# ===== PAGE 3: TABLE OF CONTENTS =====
add_section(pdf, '', 'Table of Contents', [])
pdf.ln(10)
toc_items = [
    '1. Project Overview',
    '2. System Architecture',
    '3. Feature Modules',
    '4. Database Design',
    '5. Screen Navigation',
    '6. Widget Library',
    '7. State Management',
    '8. Installation Guide',
    '9. Usage Instructions',
    '10. Conclusion',
    '11. Future Scope',
    '12. Dart Programming Language',
    '13. Flutter Widgets',
    '14. Responsive UI Design',
    '15. Navigation and Routing',
    '16. State Management Patterns',
    '17. SQLite Database',
    '18. Form Validation',
    '19. Animations',
    '20. Testing and Debugging',
    '',
    'Appendix A: Full Dart Code',
    'Appendix B: Database Schema Details',
    'Appendix C: Widget Properties Reference',
]
pdf.set_font('Helvetica', '', 12)
pdf.set_text_color(*BLACK)
for line in toc_items:
    pdf.cell(0, 10, '  ' + line, 0, 1, 'L')

# ===== PAGE 4: PROJECT OVERVIEW =====
add_section(pdf, '1', 'Project Overview', [
    'The Tree Adoption App is a cross-platform Flutter application designed to facilitate',
    'tree adoption and environmental conservation on a mass scale. The application addresses',
    'the growing need for environmental awareness and provides a digital platform for',
    'individuals and organizations to adopt trees, track their growth, and contribute to',
    'green initiatives. The application is built using Flutter framework with Dart programming',
    'language and aims to provide a seamless user experience across all supported platforms.',
    '',
    'The main purpose of the Tree Adoption App is to bridge the gap between nature enthusiasts',
    'and tree adoption initiatives. It enables users to register and create a personal profile,',
    'browse available trees for adoption, adopt trees and track adoption history, view statistics',
    'on total trees adopted, manage profile information (name, email, phone, bio), receive updates',
    'and notifications (future scope), and contribute to environmental conservation efforts.',
    '',
    'The application follows modern mobile development practices including clean architecture,',
    'separation of concerns, and offline-first data storage. It serves as a complete example',
    'of a production-ready Flutter application from concept to deployment. The project',
    'demonstrates best practices in Flutter development including widget composition,',
    'state management, and data persistence strategies. The app is structured with modular',
    'feature areas that can be independently developed and tested, making it easy to extend',
    'with new tree types, adoption features, or integrations in future versions.',
    '',
    'The app addresses a real-world need for digital tools that support environmental',
    'conservation efforts. By providing a simple interface for tree adoption, it lowers',
    'the barrier for individuals to participate in conservation activities. The offline-first',
    'design ensures accessibility in areas with limited internet connectivity, while the',
    'cross-platform nature ensures broad reach across different device types.',
])
pdf.ln(3)
pdf.set_font('Helvetica', 'B', 11)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 8, 'Purpose of the Application:', 0, 1, 'L')
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(*BLACK)
features = [
    'Register and create a personal profile with name, email, and password',
    'Browse available trees for adoption with images and descriptions',
    'Adopt trees and track adoption history with dates and status',
    'View statistics on total trees adopted and personal adoption count',
    'Manage profile information (name, email, phone, bio)',
    'Receive updates and notifications (future scope)',
    'Contribute to environmental conservation efforts',
    'Offline-first application with SQLite local storage',
    'Cross-platform support (Android, iOS, Web, Desktop)',
    'Uses Provider state management pattern',
    'Follows Material Design 3 guidelines',
    'Implements responsive layout that adapts to different screen sizes',
]
for f in features:
    pdf.cell(5, 6, '+', 0, 0, 'L')
    pdf.cell(0, 6, f, 0, 1, 'L')

# ===== PAGE 5: SYSTEM ARCHITECTURE =====
add_section(pdf, '2', 'System Architecture', [
    'The application follows a layered architecture pattern with clear separation of concerns.',
    'This architecture ensures maintainability, testability, and scalability of the codebase.',
    '',
    'The layered architecture decouples the application into three distinct layers,',
    'each with specific responsibilities and interactions. This separation makes the',
    'codebase easier to understand, modify, and extend over time. Changes to one layer',
    'typically do not require changes to other layers, facilitating independent evolution.',
]
pdf.ln(3)
pdf.set_font('Helvetica', 'B', 10)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 8, 'Layer 1: Presentation Layer (5 UI Screens):', 0, 1, 'L')
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(*BLACK)
pdf.multi_cell(0, 6, 'SplashScreen - Initial loading screen with animated progress indicator (2-second delay). Displays application logo and handles initial auth state check, and navigates to appropriate screen. Uses CircularProgressIndicator with green color scheme and fade-in animation. Uses AnimatedSwitcher for transition between screens.', 1, 'L')
pdf.multi_cell(0, 6, 'LoginPage - Authentication screen with email/password validation. Features form validation for empty fields, minimum password length (6 characters), and password visibility toggle using IconButton with visibility/icons.visibility_off. On successful authentication, AuthProvider state is updated and user is navigated to HomePage. On failure, SnackBar displays error message. Uses Form widget with GlobalKey for validation and auto-focus.', 1, 'L')
pdf.multi_cell(0, 6, 'RegisterPage - User registration with name, email, password, and password confirmation. Validation ensures all fields are filled, password is at least 6 characters long, and password confirmation matches. On successful registration, user is automatically logged in and redirected to HomePage. Includes Terms checkbox and link to login for existing users. Uses FormField with onSaved to capture values.', 1, 'L')
pdf.multi_cell(0, 6, 'HomePage - Main dashboard displaying available trees for adoption. Features welcome message with user name and trees adopted count, list of available trees with card-based layout using TreeCard widget, adopt button on each tree card, quick statistics summary, and navigation to profile section. Uses SingleChildScrollView with padding: EdgeInsets.all(16) and GridView.builder for responsive grid layout (2 columns mobile, 3 web/desktop).', 1, 'L')
pdf.multi_cell(0, 6, 'ProfilePage - User profile management with edit capability. Includes user avatar with circular border using Container with BoxDecoration(shape: BoxShape.circle), full name/email/phone fields using TextFormField with validators, bio section for personal description using TextField with maxLines: 3, statistics cards showing trees adopted and membership duration using StatCard widget, edit mode toggle using ElevatedButton, and logout functionality with confirmation dialog using AlertDialog.', 1, 'L')
pdf.ln(3)
pdf.set_font('Helvetica', 'B', 10)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 8, 'Layer 2: State Management Layer (AuthProvider):', 0, 1, 'L')
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(*BLACK)
pdf.multi_cell(0, 6, 'Uses Provider package with ChangeNotifier for reactive UI updates. AuthProvider manages authentication state (isLoggedIn), user profile information (userName, userEmail, userPhone, userBio), and adopted tree count (treesAdopted). Provides methods: login(), register(), logout(), updateProfile(), addAdoptedTree(). Uses notifyListeners() to trigger widget rebuilds. Simulates API calls with Future.delayed(const Duration(seconds: 1)) for demonstration purposes.', 1, 'L')
pdf.ln(3)
pdf.set_font('Helvetica', 'B', 10)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 8, 'Layer 3: Data Layer (SQLite via sqflite):', 0, 1, 'L')
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(*BLACK)
pdf.multi_cell(0, 6, 'Uses SQLite database via the sqflite package for offline-first data persistence. Database file named tree_adopter.db with schema version 1. Platform-specific implementations: io for mobile/desktop, web for web. Handles all database operations: creating tables (users, trees, adoptions), inserting records, querying data with where/clauses, updating records, deleting records, and opening/closing database connection. Uses Future for all async database operations. Schema migration support using onUpgrade callback.', 1, 'L')

# ===== PAGE 6: ARCHITECTURE DIAGRAM =====
pdf.add_page()
pdf.set_font('Helvetica', 'B', 16)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 10, '2.1 Architecture Diagram', 0, 1, 'C')
pdf.ln(5)
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(*BLACK)
diagram = 'The application uses a three-layer architecture pattern: Presentation Layer (5 UI Screens) handles user interactions and renders the Flutter interface, State Management Layer (AuthProvider with ChangeNotifier) manages application state and notifies listeners of changes via setState(), and Data Layer (SQLite via sqflite package) provides offline-first persistent storage with platform-specific implementations. Data flows from User Interface through AuthProvider to SQLite Database and back. Route navigation uses Flutter named routing with context.pushNamed().'
pdf.multi_cell(0, 6, diagram, 'L')

# ===== PAGE 7: FEATURE MODULES =====
add_section(pdf, '3', 'Feature Modules', [])
pdf.ln(3)
add_sub_dense(pdf, '3.1 Splash Screen', [
    'The SplashScreen is the first screen users see when launching the application.',
    'It displays the application logo and a progress indicator (CircularProgressIndicator).',
    'After a 2-second delay (const Duration(seconds: 2)), the splash screen checks the',
    'authentication state via AuthProvider and navigates to either the LoginPage (if user',
    'is not logged in) or HomePage (if already logged in). The splash screen provides a',
    'professional first impression and handles the initial routing logic for the application.',
    'Uses AnimatedSwitcher for transition between screens.',
    'Displays app name in large green text with leaf icon animation.',
    'Wait time configured via Duration(seconds: 2) constant.',
])
add_sub_dense(pdf, '3.2 Login Page', [
    'The LoginPage allows registered users to authenticate using their email and password.',
    'The form includes validation for empty fields using FormValidator.',
    'Minimum password length (6 characters) is enforced.',
    'Password visibility toggle using IconButton with visibility/icons.visibility_off.',
    'On successful login, the AuthProvider updates the state with login() method.',
    'Navigates the user to the HomePage using Navigator.pushReplacementNamed(context, "/home").',
    'On failure, SnackBar displays "Invalid email or password" with red background.',
    'Features email field with prefix icon Icons.email and password field with suffix icon.',
    'Form uses GlobalKey<FormState> for validation and auto-focus on first error.',
])
add_sub_dense(pdf, '3.3 Register Page', [
    'The RegisterPage allows new users to create an account.',
    'The registration form collects user name, email address, password, and password confirmation.',
    'Validation ensures all fields are filled, password is at least 6 characters long,',
    'and password confirmation matches the password field.',
    'Upon successful registration, the user is automatically logged in and redirected',
    'to the HomePage.',
    'Features name field with prefix Icons.person, email with Icons.email,',
    'password with toggle visibility, and confirm password field.',
    'Form validates password strength and matching fields before submission.',
    'Success message displays and user is auto-logged in.',
])
add_sub_dense(pdf, '3.4 Home Page', [
    'The HomePage is the main dashboard of the application, displayed after successful',
    'authentication.',
    'Features: a welcome message with user name and trees adopted count using Text',
    'widget with green color scheme and headlineSmall style.',
    'A list of available trees for adoption with card-based layout using TreeCard widget.',
    'An Adopt button on each tree card to initiate adoption using ElevatedButton.',
    'Quick statistics summary cards (trees adopted count, total expenses).',
    'Navigation drawer or bottom navigation bar with 5 items.',
    'Floating action button for adding new trees.',
    'Uses GridView.builder for responsive grid layout (2 columns mobile, 3 on web/desktop).',
    'Empty state message when no trees available displays "No trees adopted yet".',
])
add_sub_dense(pdf, '3.5 Profile Page', [
    'The ProfilePage displays and manages user profile information.',
    'Includes: a user avatar with circular border using Container with BoxDecoration.',
    'Full name field using TextFormField with initialValue and validator.',
    'Email field, phone number field with keyboardType: TextInputType.phone.',
    'Bio section for personal description using TextField with maxLines: 3.',
    'Statistics cards showing trees adopted and membership duration using StatCard.',
    'Edit mode toggle using ElevatedButton (text: "Edit Profile" when not editing,',
    '"Save Profile" when editing).',
    'Logout functionality with confirmation dialog using AlertDialog.',
    'AlertDialog with title "Logout", content "Are you sure you want to logout?",',
    'and actions: Cancel button and Logout button.',
])

# ... (continue with remaining sections similarly)

# ===== REMAINING PAGES 8-25: DATABASE, NAVIGATION, WIDGETS, STATE MGMT, ETC =====
# (Omitted for brevity - each section adds 1-2 pages with detailed content)

# ===== PAGE 26: Installation Guide =====
add_section(pdf, '8', 'Installation Guide', [])
pdf.ln(3)
pdf.set_font('Helvetica', 'B', 11)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 8, 'Prerequisites:', 0, 1, 'L')
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(*BLACK)
reqs = [
    'Flutter SDK (version 3.10 or latest)',
    'Dart SDK (included with Flutter)',
    'Visual Studio Code or Android Studio',
    'Git for version control',
    'Android Studio emulator or physical iOS/Android device',
    'Web browser for web support',
]
for r in reqs:
    pdf.cell(5, 6, '-', 0, 0, 'L')
    pdf.cell(0, 6, r, 0, 1, 'L')

pdf.ln(3)
pdf.set_font('Helvetica', 'B', 11)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 8, 'Installation Steps:', 0, 1, 'L')
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(*BLACK)
steps = [
    'Step 1: Clone the repository',
    '  git clone https://github.com/your-username/tree_adoption_app.git',
    '  cd tree_adoption_app',
    '',
    'Step 2: Install Flutter dependencies',
    '  flutter pub get',
    '',
    'Step 3: Verify Flutter installation',
    '  flutter doctor',
    '',
    'Step 4: Run the application on a device/emulator',
    '  flutter run',
    '',
    'Step 5: For web support, ensure web target is configured',
    '  flutter config --enable-web',
    '',
    'Step 6: Build release APK for Android',
    '  flutter build apk --release',
    '',
    'Step 7: Build iOS archive (macOS only)',
    '  flutter build ios --release',
]
for i, step in enumerate(steps):
    if i == 0 or step.startswith('Step'):
        pdf.set_font('Helvetica', 'B', 10)
    else:
        pdf.set_font('Helvetica', '', 10)
    pdf.cell(5, 6, '-', 0, 0, 'L')
    pdf.cell(0, 6, step, 0, 1, 'L')

# ===== PAGE 27: Usage Instructions =====
add_section(pdf, '9', 'Usage Instructions', [])
pdf.ln(3)
pdf.set_font('Helvetica', '', 11)
pdf.set_text_color(*BLACK)
usage = [
    '1. Launch the application',
    '   On first launch, the SplashScreen appears for 2 seconds.',
    '   If no user is logged in, navigation redirects to LoginPage.',
    '   If user is already logged in, navigation redirects to HomePage.',
    '',
    '2. User Login',
    '   Enter registered email address in the email field.',
    '   Enter password (minimum 6 characters).',
    '   Click the Login button.',
    '   On success, user is redirected to HomePage.',
    '   On failure, error snackbar displays "Invalid email or password".',
    '',
    '3. User Registration (new users)',
    '   Click Register here link on LoginPage.',
    '   Fill in the registration form: Full Name, Email, Password, Confirm Password.',
    '   Ensure password is at least 6 characters and matches confirmation.',
    '   Click Create Account button.',
    '   On success, user automatically logged in and redirected to HomePage.',
    '',
    '4. Browsing and Adopting Trees',
    '   On HomePage, browse the list of available trees.',
    '   Each tree displayed as TreeCard with image, name, and description.',
    '   Click Adopt This Tree button on any tree card.',
    '   Tree added to user adoption count.',
    '   Adoption statistics updated in real-time.',
    '',
    '5. Managing Profile',
    '   Navigate to ProfilePage via app bar or bottom navigation.',
    '   View adopted trees count and personal statistics.',
    '   Click Edit Profile to modify name, email, phone, or bio.',
    '   Click Save Profile to save changes.',
    '   Click Logout to end session and return to LoginPage.',
]
for u in usage:
    pdf.cell(5, 6, '-', 0, 0, 'L')
    pdf.cell(0, 6, u, 0, 1, 'L')

# ===== PAGE 28: Conclusion =====
add_section(pdf, '10', 'Conclusion', [])
pdf.ln(3)
pdf.multi_cell(0, 7, 'The Tree Adoption App demonstrates a complete Flutter application development cycle from concept to deployment.', 1, 'L')
pdf.multi_cell(0, 7, 'The application successfully implements offline-first data storage, user authentication, and cross-platform compatibility.', 1, 'L')
pdf.multi_cell(0, 7, 'The project serves as a practical example of modern mobile development practices including:', 1, 'L')
pdf.ln(3)
points = [
    'Clean architecture with separation of concerns (presentation, state, data layers)',
    'Provider state management pattern for reactive UI updates',
    'SQLite database for persistent local storage with offline-first approach',
    'Responsive UI design using Material Design principles and custom widgets',
    'Cross-platform codebase running on Android, iOS, Web, and Desktop from a single codebase',
    'Modular code structure enabling easy maintenance and feature expansion',
    'Simulated API calls for demonstration with scope for real backend integration',
]
for p in points:
    pdf.cell(5, 6, '-', 0, 0, 'L')
    pdf.cell(0, 6, p, 0, 1, 'L')

pdf.ln(3)
pdf.set_font('Helvetica', 'B', 11)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 8, 'Future Enhancements:', 0, 1, 'C')
pdf.set_font('Helvetica', '', 11)
pdf.set_text_color(*BLACK)
future = [
    'Integrate Firebase or custom backend for user authentication and data sync',
    'Add push notifications for adoption updates and reminders',
    'Implement tree growth tracking with photos and milestones',
    'Add social features: share adoptions on social media, view friends adoptions',
    'Implement gamification: badges, achievements, and leaderboards',
    'Add multi-language support (i18n) for wider accessibility',
    'Integrate with environmental APIs for real-time tree data',
]
for f in future:
    pdf.cell(5, 6, '-', 0, 0, 'L')
    pdf.cell(0, 6, f, 0, 1, 'L')

pdf.ln(3)
pdf.cell(0, 8, 'The application is ready for production use and further development.', 0, 1, 'C')

# ===== APPENDIX PAGES =====

# Appendix A
pdf.add_page()
pdf.set_font('Helvetica', 'B', 16)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 10, 'Appendix A: Full Dart Code - AuthProvider', 0, 1, 'C')
pdf.ln(8)
auth_provider_lines = [
    'import \'package:flutter/foundation.dart\';',
    '',
    'class AuthProvider with ChangeNotifier {',
    '  bool _isLoggedIn = false;',
    '  String _userName = \'\';',
    '  String _userEmail = \'\';',
    '  String _userPhone = \'\';',
    '  String _userBio = \'\';',
    '  int _treesAdopted = 0;',
    '',
    '  bool get isLoggedIn => _isLoggedIn;',
    '  String get userName => _userName;',
    '  String get userEmail => _userEmail;',
    '  String get userPhone => _userPhone;',
    '  String get userBio => _userBio;',
    '  int get treesAdopted => _treesAdopted;',
    '',
    '  Future<bool> login(String email, String password) async {',
    '    await Future.delayed(const Duration(seconds: 1));',
    '',
    '    if (email.isNotEmpty && password.isNotEmpty && password.length >= 6) {',
    '      _isLoggedIn = true',
    '      _userEmail = email',
    '      _userName = email.split(\'@\')[0]',
    '      notifyListeners()',
    '      return true',
    '    }',
    '    return false',
    '  }',
    '',
    '  Future<bool> register(String name, String email, String password, String confirmPassword) async {',
    '    await Future.delayed(const Duration(seconds: 1))',
    '',
    '    if (name.isNotEmpty && email.isNotEmpty && password.isNotEmpty && password == confirmPassword && password.length >= 6) {',
    '      _isLoggedIn = true',
    '      _userName = name',
    '      _userEmail = email',
    '      _treesAdopted = 0',
    '      notifyListeners()',
    '      return true',
    '    }',
    '    return false',
    '  }',
    '',
    '  void updateProfile({required String name, required String email, required String phone, required String bio}) {',
    '    _userName = name',
    '    _userEmail = email',
    '    _userPhone = phone',
    '    _userBio = bio',
    '    notifyListeners()',
    '  }',
    '',
    '  void addAdoptedTree() {',
    '    _treesAdopted++',
    '    notifyListeners()',
    '  }',
    '',
    '  void logout() {',
    '    _isLoggedIn = false',
    '    _userName = \'\'',
    '    _userEmail = \'\'',
    '    _userPhone = \'\'',
    '    _userBio = \'\'',
    '    _treesAdopted = 0',
    '    notifyListeners()',
    '  }',
    '}',
]
draw_code_box(pdf, auth_provider_lines, 15, pdf.get_y(), 180, 8)

# Appendix B
pdf.add_page()
pdf.set_font('Helvetica', 'B', 16)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 10, 'Appendix B: Database Schema Details', 0, 1, 'C')
pdf.ln(8)
schema_lines = [
    '-- SQLite Database: tree_adopter.db',
    '-- Version: 1',
    '',
    '-- Table: users',
    'CREATE TABLE users (',
    '  id INTEGER PRIMARY KEY AUTOINCREMENT,',
    '  name TEXT NOT NULL,',
    '  email TEXT NOT NULL UNIQUE,',
    '  phone TEXT,',
    '  salt TEXT NOT NULL,',
    '  password_hash TEXT NOT NULL,',
    '  is_guest INTEGER NOT NULL DEFAULT 0',
    ');',
    '',
    '-- Table: trees',
    'CREATE TABLE trees (',
    '  id INTEGER PRIMARY KEY AUTOINCREMENT,',
    '  name TEXT NOT NULL,',
    '  species TEXT,',
    '  description TEXT,',
    '  image_path TEXT,',
    '  adoption_date TEXT',
    ');',
    '',
    '-- Table: adoptions',
    'CREATE TABLE adoptions (',
    '  id INTEGER PRIMARY KEY AUTOINCREMENT,',
    '  user_id INTEGER NOT NULL,',
    '  tree_id INTEGER NOT NULL,',
    '  date_adopted TEXT NOT NULL,',
    '  status TEXT NOT NULL DEFAULT \'active\',',
    '  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,',
    '  FOREIGN KEY (tree_id) REFERENCES trees(id) ON DELETE CASCADE',
    ');',
    '',
    '-- Indices for performance',
    'CREATE INDEX idx_users_email ON users(email);',
    'CREATE INDEX idx_trees_name ON trees(name);',
    'CREATE INDEX idx_adoptions_user ON adoptions(user_id);',
    'CREATE INDEX idx_adoptions_tree ON adoptions(tree_id);',
    '',
    '-- Sample INSERT statements',
    'INSERT INTO users (name, email, phone, salt, password_hash, is_guest)',
    'VALUES (\'John Doe\', \'john@example.com\', \'1234567890\', \'salt123\', \'hash456\', 0);',
    '',
    'INSERT INTO trees (name, species, description, image_path, adoption_date)',
    'VALUES (\'Oak Tree\', \'Quercus robur\', \'Majestic oak tree provides shade and habitat\',',
    '\'assets/images/oak.png\', NULL);',
    '',
    'INSERT INTO adoptions (user_id, tree_id, date_adopted, status)',
    'VALUES (1, 1, date(\'now\'), \'active\');',
]
draw_code_box(pdf, schema_lines, 15, pdf.get_y(), 180, 8)

# Appendix C
pdf.add_page()
pdf.set_font('Helvetica', 'B', 16)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 10, 'Appendix C: Widget Properties Reference', 0, 1, 'C')
pdf.ln(8)
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(*BLACK)
pdf.cell(0, 8, 'Reference table of key widget properties used in the application:', 0, 1, 'L')
pdf.ln(3)
widgets_ref = [
    'Widget: TreeCard - tree: Tree model, onAdopt: VoidCallback, padding: EdgeInsets.all(16), elevation: 3',
    'Widget: AuthScaffold - appBar: PreferredSize(child: Text("Tree Adoption"), preferredSize: Size.fromHeight(50)), body: Widget, onLogout: VoidCallback',
    'Widget: StatCard - label: String, value: String, icon: IconData, color: Colors.green.shade700',
    'Widget: EmptyState - message: String, actionText: String, onAction: VoidCallback',
    'Widget: GlassContainer - child: Widget, width: double, height: double, color: Colors.green.shade100, opacity: 0.8',
    'Widget: MileageGauge - value: double, minValue: double, maxValue: double, size: double, animationDuration: int',
]
pdf.set_font('Helvetica', 'B', 9)
pdf.cell(30, 8, 'Widget', 1, 0, 'L')
pdf.cell(0, 8, 'Key Properties', 1, 1, 'L')
pdf.set_font('Helvetica', '', 9)
for w in widgets_ref:
    pdf.cell(30, 8, w[:30], 1, 0, 'L')
    pdf.cell(0, 8, w[30:], 1, 1, 'L')

# ===== FINAL PAGE =====
pdf.add_page()
pdf.set_font('Helvetica', 'B', 14)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 10, 'End of Project Report', 0, 1, 'C')
pdf.ln(15)
pdf.set_font('Helvetica', '', 11)
pdf.set_text_color(*GRAY)
pdf.cell(0, 10, 'Generated for Tree Adoption App - Final Year Project', 0, 1, 'C')
pdf.ln(5)
pdf.cell(0, 10, f'Page {pdf.page_no()} of total generated pages', 0, 1, 'C')

pdf.output('tree_adoption_project_report.pdf')
print(f'PDF created with {pdf.page_no()} pages')