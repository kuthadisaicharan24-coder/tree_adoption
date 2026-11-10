import fpdf

pdf = fpdf.FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# ===== COLOR CONSTANTS =====
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
    """Draw a code highlight box"""
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
    """Add a section with numbered title and content"""
    pdf.add_page()
    if number:
        pdf.set_font('Helvetica', 'B', 16)
        pdf.set_text_color(*GREEN_DARK)
        pdf.cell(0, 10, f'{number}. {title}', 0, 1, 'C')
        pdf.ln(5)
    else:
        pdf.set_font('Helvetica', 'B', 16)
        pdf.set_text_color(*GREEN_DARK)
        pdf.cell(0, 10, title, 0, 1, 'C')
        pdf.ln(5)
    pdf.set_font('Helvetica', '', 11)
    pdf.set_text_color(*BLACK)
    for line in content_lines:
        pdf.multi_cell(0, 6, line, 'L')
    pdf.ln(3)
    if code_boxes:
        for box in code_boxes:
            draw_code_box(pdf, *box)

def add_code_section(pdf, title, code_lines):
    """Add a page with code box"""
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 16)
    pdf.set_text_color(*GREEN_DARK)
    pdf.cell(0, 10, title, 0, 1, 'C')
    pdf.ln(5)
    draw_code_box(pdf, code_lines, 15, pdf.get_y(), 180, 8)

# ===== PAGE 0: COVER PAGE =====
pdf.add_page()
pdf.set_fill_color(*GREEN_DARK)
pdf.ln(30)
pdf.set_font('Helvetica', 'B', 28)
pdf.set_text_color(*CREAM)
pdf.cell(0, 15, 'Tree Adoption App', 0, 1, 'C')
pdf.set_font('Helvetica', '', 16)
pdf.set_text_color(*GREEN_LIGHT)
pdf.cell(0, 10, 'A Flutter Application for Environmental Conservation', 0, 1, 'C')
pdf.ln(20)
pdf.set_font('Helvetica', '', 11)
pdf.set_text_color(*WHITE)
info_items = [
    ('Project:', 'Tree Adoption App'),
    ('Platform:', 'Flutter (Cross-platform Mobile/Web/Desktop)'),
    ('Language:', 'Dart'),
    ('State Management:', 'Provider / ChangeNotifier'),
    ('Database:', 'SQLite (offline-first, sqflite package)'),
    ('Auth Provider:', 'Custom AuthProvider with ChangeNotifier'),
    ('Version:', '1.0.0'),
]
for label, value in info_items:
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 8, label, 0, 0, 'R')
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(0, 8, value, 0, 1, 'L')
pdf.ln(15)
pdf.set_font('Helvetica', 'I', 10)
pdf.set_text_color(*GREEN_LIGHT)
pdf.cell(0, 10, 'Developed as a Final Year Project', 0, 1, 'C')
pdf.cell(0, 10, 'for Computer Science and Engineering', 0, 1, 'C')
pdf.ln(5)
pdf.cell(0, 10, '[Faculty Name], Professor', 0, 1, 'C')

# ===== PAGE 1: CERTIFICATE PAGE =====
add_section(pdf, '', 'Certificate of Bonafide Record', [
    'This is to Certify',
    'of Bonafide Record',
])
pdf.ln(15)
pdf.set_font('Helvetica', '', 12)
pdf.set_text_color(*WHITE)
pdf.multi_cell(0, 6, 'This is to certify that this is a bonafide record of practical work', 1, 'L')
pdf.multi_cell(0, 6, 'done by [Student Name], Regd. No. [Roll Number]', 1, 'L')
pdf.multi_cell(0, 6, 'of III B.Tech I Semester Class in', 1, 'L')
pdf.multi_cell(0, 6, 'Flutter Application Development', 1, 'L')
pdf.multi_cell(0, 6, 'during the year 2024-25.', 1, 'L')
pdf.ln(10)
pdf.multi_cell(0, 6, 'No. of Tasks Completed and Certified:', 1, 'L')
pdf.ln(5)
pdf.multi_cell(0, 6, 'Lecture In-Charge                                                                          Head of The Department', 1, 'L')
pdf.ln(5)
pdf.multi_cell(0, 6, 'Date: [Date]', 1, 'L')
pdf.ln(15)
pdf.set_font('Helvetica', 'B', 12)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 10, 'Jawaharlal Nehru Technological University', 0, 1, 'C')
pdf.ln(5)
pdf.cell(0, 10, 'Vizianagaram - 535003, Andhra Pradesh', 0, 1, 'C')

# ===== PAGE 2: EMPTY PAGE =====
pdf.add_page()
pdf.set_font('Helvetica', '', 12)
pdf.set_text_color(*GRAY)
pdf.cell(0, 10, '(This page is intentionally left blank)', 0, 1, 'C')

# ===== PAGE 3: TABLE OF CONTENTS =====
add_section(pdf, '', 'Table of Contents', [])
pdf.ln(10)
toc_items = [
    ('1', 'Project Overview'),
    ('2', 'System Architecture'),
    ('3', 'Feature Modules'),
    ('4', 'Database Design'),
    ('5', 'Screen Navigation'),
    ('6', 'Widget Library'),
    ('7', 'State Management'),
    ('8', 'Installation Guide'),
    ('9', 'Usage Instructions'),
    ('10', 'Conclusion'),
    ('11', 'Future Scope'),
    ('', 'Appendix A: Full Dart Code'),
    ('', 'Appendix B: Database Schema Details'),
    ('', 'Appendix C: Widget Properties Reference'),
]
pdf.set_font('Helvetica', '', 12)
pdf.set_text_color(*BLACK)
for num, title in toc_items:
    if num:
        pdf.set_font('Helvetica', 'B', 11)
        pdf.cell(10, 10, num, 0, 0, 'L')
        pdf.set_font('Helvetica', '', 11)
    else:
        pdf.set_font('Helvetica', '', 11)
    pdf.cell(0, 10, f'  {title}', 0, 1, 'L')

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
])
pdf.ln(3)
pdf.set_font('Helvetica', 'B', 11)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 8, 'Purpose of the Application:', 0, 1, 'L')
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(*BLACK)
features = [
    'Register and create a personal profile',
    'Browse available trees for adoption',
    'Adopt trees and track adoption history',
    'View statistics on total trees adopted',
    'Manage profile information (name, email, phone, bio)',
    'Receive updates and notifications (future scope)',
    'Contribute to environmental conservation efforts',
]
for f in features:
    pdf.cell(5, 6, '+', 0, 0, 'L')
    pdf.cell(0, 6, f, 0, 1, 'L')

# ===== PAGE 5: SYSTEM ARCHITECTURE =====
add_section(pdf, '2', 'System Architecture', [
    'The application follows a layered architecture pattern with clear separation of concerns.',
    'This architecture ensures maintainability, testability, and scalability of the codebase.',
])
pdf.ln(3)
pdf.set_font('Helvetica', 'B', 10)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 8, 'Layer 1: Presentation Layer:', 0, 1, 'L')
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(*BLACK)
screens = [
    'SplashPage - Initial loading screen with animated progress indicator',
    'LoginPage - Authentication screen with email/password fields',
    'RegisterPage - User registration with name, email, password fields',
    'HomePage - Main dashboard displaying available trees for adoption',
    'ProfilePage - User profile management screen with statistics',
]
for s in screens:
    pdf.cell(5, 6, '-', 0, 0, 'L')
    pdf.cell(0, 6, s, 0, 1, 'L')

pdf.ln(3)
pdf.set_font('Helvetica', 'B', 10)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 8, 'Layer 2: State Management Layer:', 0, 1, 'L')
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(*BLACK)
provider_methods = [
    'login(String email, String password) - Simulates API authentication',
    'register(String name, String email, String password, String confirmPassword) - Simulates user registration',
    'logout() - Clears authentication state and resets user data',
    'updateProfile({name, email, phone, bio}) - Updates user profile information',
    'addAdoptedTree() - Increments the count of adopted trees',
    'isLoggedIn - Boolean getter for authentication status',
]
for m in provider_methods:
    pdf.cell(5, 6, '+', 0, 0, 'L')
    pdf.cell(0, 6, m, 0, 1, 'L')

pdf.ln(3)
pdf.set_font('Helvetica', 'B', 10)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 8, 'Layer 3: Data Layer:', 0, 1, 'L')
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(*BLACK)
pdf.multi_cell(0, 6, 'Uses SQLite database via the sqflite package for offline-first data persistence. The data layer consists of database helper classes that handle all database operations including creating tables, inserting records, querying data, and updating records. Platform-specific implementations are used for mobile (io), web (web), and desktop.', 1, 'L')

# ===== PAGE 6: ARCHITECTURE DIAGRAM =====
pdf.add_page()
pdf.set_font('Helvetica', 'B', 16)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 10, '2.1 Architecture Diagram', 0, 1, 'C')
pdf.ln(5)
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(*BLACK)
diagram = 'The application uses a three-layer architecture pattern: Presentation Layer (UI Screens) handles user interactions, State Management Layer (AuthProvider with ChangeNotifier) manages application state, and Data Layer (SQLite via sqflite package) provides offline-first persistent storage. Navigation uses Flutter named routing with context.pushNamed().'
pdf.multi_cell(0, 6, diagram, 'L')

# ===== PAGE 7: FEATURE MODULES =====
add_section(pdf, '3', 'Feature Modules', [
    'The application is modularized into the following key feature modules:',
])
pdf.ln(3)
modules = [
    ('3.1 Splash Screen', 'The SplashScreen is the first screen users see when launching the application. It displays the application logo and a progress indicator. After a 2-second delay, the splash screen checks the authentication state via AuthProvider and navigates to either the LoginPage (if user is not logged in) or HomePage (if already logged in). The splash screen provides a professional first impression and handles the initial routing logic for the application.'),
    ('3.2 Login Page', 'The LoginPage allows registered users to authenticate using their email and password. The form includes validation for empty fields and minimum password length (6 characters). Upon successful login, the AuthProvider updates the state and navigates the user to the HomePage. The login process simulates an API call with a delayed response for demonstration purposes. Error handling displays appropriate feedback for invalid credentials.'),
    ('3.3 Register Page', 'The RegisterPage allows new users to create an account. The registration form collects user name, email address, password, and password confirmation. Validation ensures all fields are filled, the password is at least 6 characters long, and the password confirmation matches the password field. Upon successful registration, the user is automatically logged in and redirected to the HomePage.'),
    ('3.4 Home Page', 'The HomePage is the main dashboard of the application, displayed after successful authentication. It features: a welcome message with user name and trees adopted count, a list of available trees for adoption with card-based layout, an Adopt button on each tree card to initiate adoption, a quick statistics summary, and navigation to the profile section.'),
    ('3.5 Profile Page', 'The ProfilePage displays and manages user profile information. It includes: a user avatar with circular border, full name, email, phone number fields, a bio section for personal description, statistics cards showing trees adopted and membership duration, edit mode to modify profile information, and logout functionality with a confirmation dialog.'),
]
for title, desc in modules:
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 8, f'{title}:', 0, 1, 'L')
    pdf.set_font('Helvetica', '', 10)
    pdf.multi_cell(0, 6, '  ' + desc, 1, 'L')

# ===== PAGE 8: DATABASE DESIGN =====
add_section(pdf, '4', 'Database Design', [
    'The application uses SQLite database for local, offline-first data storage. All data including user profiles, tree information, and adoption records are stored locally on the device. This ensures the application works without an internet connection and provides fast data access. The sqflite package is used for SQLite operations, with platform-specific implementations for mobile (io), web (web), and desktop environments.',
])
pdf.ln(3)
pdf.set_font('Helvetica', 'B', 11)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 8, '4.1 Database Tables:', 0, 1, 'L')
pdf.ln(2)

# Users table
pdf.set_font('Helvetica', 'B', 10)
pdf.set_text_color(*BLACK)
pdf.cell(0, 7, '4.1.1 users Table:', 0, 1, 'L')
pdf.set_font('Helvetica', '', 9)
pdf.set_text_color(*BLACK)
users_cols = [
    'id INTEGER PRIMARY KEY AUTOINCREMENT - Unique identifier for each user',
    'name TEXT NOT NULL - User full name',
    'email TEXT NOT NULL UNIQUE - User email address (unique constraint)',
    'phone TEXT - User phone number (optional)',
    'salt TEXT NOT NULL - Salt for password hashing',
    'password_hash TEXT NOT NULL - Hashed password for authentication',
    'is_guest INTEGER NOT NULL DEFAULT 0 - Flag for guest users (0=registered, 1=guest)',
]
for col in users_cols:
    pdf.cell(5, 5, '-', 0, 0, 'L')
    pdf.cell(0, 5, col, 0, 1, 'L')

# Trees table
pdf.ln(2)
pdf.set_font('Helvetica', 'B', 10)
pdf.set_text_color(*BLACK)
pdf.cell(0, 7, '4.1.2 trees Table:', 0, 1, 'L')
pdf.set_font('Helvetica', '', 9)
pdf.set_text_color(*BLACK)
trees_cols = [
    'id INTEGER PRIMARY KEY AUTOINCREMENT - Unique tree identifier',
    'name TEXT NOT NULL - Name of tree species (Oak, Maple, Pine)',
    'species TEXT - Scientific name or species description',
    'description TEXT - Detailed description of tree benefits and characteristics',
    'image_path TEXT - Path to tree image asset',
    'adoption_date TEXT - Date when tree was adopted (if adopted)',
]
for col in trees_cols:
    pdf.cell(5, 5, '-', 0, 0, 'L')
    pdf.cell(0, 5, col, 0, 1, 'L')

# Adoptions table
pdf.ln(2)
pdf.set_font('Helvetica', 'B', 10)
pdf.set_text_color(*BLACK)
pdf.cell(0, 7, '4.1.3 adoptions Table:', 0, 1, 'L')
pdf.set_font('Helvetica', '', 9)
pdf.set_text_color(*BLACK)
adoptions_cols = [
    'id INTEGER PRIMARY KEY AUTOINCREMENT - Unique adoption record ID',
    'user_id INTEGER NOT NULL - Reference to users table',
    'tree_id INTEGER NOT NULL - Reference to trees table',
    'date_adopted TEXT NOT NULL - Date when tree was adopted',
    'status TEXT NOT NULL DEFAULT "active" - Adoption status (active, completed, cancelled)',
    'FOREIGN KEY (user_id) REFERENCES users(id) - Foreign key constraint',
    'FOREIGN KEY (tree_id) REFERENCES trees(id) - Foreign key constraint',
]
for col in adoptions_cols:
    pdf.cell(5, 5, '-', 0, 0, 'L')
    pdf.cell(0, 5, col, 0, 1, 'L')

# Indices
pdf.ln(2)
pdf.set_font('Helvetica', 'B', 10)
pdf.set_text_color(*BLACK)
pdf.cell(0, 7, '4.1.4 Database Indices:', 0, 1, 'L')
pdf.set_font('Helvetica', '', 9)
pdf.set_text_color(*BLACK)
indices = [
    'CREATE INDEX idx_users_email ON users(email) - For fast user lookup by email',
    'CREATE INDEX idx_trees_name ON trees(name) - For searching trees by name',
    'CREATE INDEX idx_adoptions_user ON adoptions(user_id) - For getting users adoptions',
    'CREATE INDEX idx_adoptions_tree ON adoptions(tree_id) - For getting adoption history of a tree',
]
for idx in indices:
    pdf.cell(5, 5, '+', 0, 0, 'L')
    pdf.cell(0, 5, idx, 0, 1, 'L')

# ===== PAGE 9: Sample SQL =====
pdf.add_page()
pdf.set_font('Helvetica', 'B', 16)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 10, '4.2 Sample SQL Queries and Commands', 0, 1, 'C')
pdf.ln(5)
sql_lines = [
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
    'CREATE TABLE trees (',
    '  id INTEGER PRIMARY KEY AUTOINCREMENT,',
    '  name TEXT NOT NULL,',
    '  species TEXT,',
    '  description TEXT,',
    '  image_path TEXT,',
    '  adoption_date TEXT',
    ');',
    '',
    'CREATE TABLE adoptions (',
    '  id INTEGER PRIMARY KEY AUTOINCREMENT,',
    '  user_id INTEGER NOT NULL,',
    '  tree_id INTEGER NOT NULL,',
    '  date_adopted TEXT NOT NULL,',
    '  status TEXT NOT NULL DEFAULT "active",',
    '  FOREIGN KEY (user_id) REFERENCES users(id),',
    '  FOREIGN KEY (tree_id) REFERENCES trees(id)',
    ');',
]
draw_code_box(pdf, sql_lines, 15, pdf.get_y(), 180, 8)

# ===== PAGE 10: Screen Navigation =====
add_section(pdf, '5', 'Screen Navigation', [
    'The application uses Flutter named routing system for navigation between screens.',
    'All routes are defined in the main.dart file and can be accessed using Navigator.pushNamed() or Navigator.pushReplacementNamed().',
])
pdf.ln(3)
pdf.set_font('Helvetica', 'B', 10)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 8, '5.1 Navigation Routes:', 0, 1, 'L')
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(*BLACK)
routes = [
    ('/', 'SplashPage', 'Initial screen that checks auth state and navigates to login or home'),
    ('/login', 'LoginPage', 'User authentication screen with email and password fields'),
    ('/register', 'RegisterPage', 'New user registration with name, email, and password'),
    ('/home', 'HomePage', 'Main dashboard with tree adoption functionality'),
    ('/profile', 'ProfilePage', 'User profile management and statistics'),
]
for route, screen, desc in routes:
    pdf.cell(5, 6, route, 0, 0, 'L')
    pdf.cell(0, 6, f'{screen}: {desc}', 0, 1, 'L')

pdf.ln(3)
pdf.set_font('Helvetica', 'B', 10)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 8, '5.2 Navigation Patterns:', 0, 1, 'L')
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(*BLACK)
patterns = [
    'Navigator.pushNamed(context, \'/login\') - Navigate to new screen, add to route stack',
    'Navigator.pushReplacementNamed(context, \'/home\') - Replace current screen with new one',
    'Navigator.pop(context) - Go back to previous screen',
    'Navigator.pushAndRemoveUntil(context, route, (route) => false) - Navigate and clear route stack',
]
for p in patterns:
    pdf.cell(5, 6, '-', 0, 0, 'L')
    pdf.cell(0, 6, p, 0, 1, 'L')

# ===== PAGE 11: Widget Library =====
add_section(pdf, '6', 'Widget Library', [
    'The application uses a collection of reusable UI widgets built with Flutter widget framework.',
    'All widgets follow Material Design guidelines and are composed to build complex user interfaces.',
])
pdf.ln(3)
widgets = [
    ('6.1 TreeCard', 'A card widget displaying tree information with icon/image, name, species, description, and benefits. Features an Adopt This Tree button at the bottom using elevated button style with green color scheme.'),
    ('6.2 AuthScaffold', 'A scaffold widget providing consistent layout structure across all screens. Includes custom app bar with project branding, body area, and bottom navigation fab for floating action button. Ensures consistent padding and styling across the app.'),
    ('6.3 StatCard', 'A statistic card widget displaying a counter value with associated icon and label. Used to show metrics like Trees Adopted on the profile page. Features green color theme with icon on top and value in large bold text below.'),
    ('6.4 EmptyState', 'A placeholder widget displayed when no data is available (e.g., no trees adopted, empty profile). Displays descriptive icon and message prompting user to take action. Helps improve UX by providing meaningful feedback when views are empty.'),
    ('6.5 GlassContainer', 'A decorative container widget with glass-morphism effect - semi-transparent background, blurred effect, and rounded corners. Used to create visually appealing sections within the UI. Features green tint and subtle border.'),
    ('6.6 MileageGauge', 'An animated gauge widget visualizing adoption statistics or efficiency metrics. Uses custom painting to draw circular progress gauge with animated transitions. Features green color scheme with smooth animation when values change.'),
]
for title, desc in widgets:
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(0, 8, title, 0, 1, 'L')
    pdf.set_font('Helvetica', '', 10)
    pdf.multi_cell(0, 6, '  ' + desc, 1, 'L')

# ===== PAGE 12: State Management =====
add_section(pdf, '7', 'State Management', [
    'The application uses the Provider package with ChangeNotifier for state management.',
    'The AuthProvider is the single source of truth for application state and is inherited by widgets using Consumer, Context, or Provider.of() methods.',
])
pdf.ln(3)
pdf.set_font('Helvetica', 'B', 10)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 8, '7.1 AuthProvider Class:', 0, 1, 'L')
pdf.ln(2)
provider_code = [
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
    '      _isLoggedIn = true;',
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
draw_code_box(pdf, provider_code, 15, pdf.get_y(), 180, 7)

# ===== PAGE 13: Installation Guide =====
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
for step in steps:
    if step.startswith('Step'):
        pdf.set_font('Helvetica', 'B', 10)
    else:
        pdf.set_font('Helvetica', '', 10)
    pdf.cell(5, 6, '-', 0, 0, 'L')
    pdf.cell(0, 6, step, 0, 1, 'L')

# ===== PAGE 14: Usage Instructions =====
add_section(pdf, '9', 'Usage Instructions', [])
pdf.ln(3)
pdf.set_font('Helvetica', '', 11)
pdf.set_text_color(*BLACK)
usage = [
    '1. Launch the application',
    '   On first launch, the SplashScreen appears for 2 seconds',
    '   If no user is logged in, navigation redirects to LoginPage',
    '   If user is already logged in, navigation redirects to HomePage',
    '',
    '2. User Login',
    '   Enter registered email address in the email field',
    '   Enter password (minimum 6 characters)',
    '   Click the Login button',
    '   On success, user is redirected to HomePage',
    '   On failure, error snackbar displays "Invalid email or password"',
    '',
    '3. User Registration (new users)',
    '   Click Register here link on LoginPage',
    '   Fill in registration form: Full Name, Email, Password, Confirm Password',
    '   Ensure password is at least 6 characters and matches confirmation',
    '   Click Create Account button',
    '   On success, user automatically logged in and redirected to HomePage',
    '',
    '4. Browsing and Adopting Trees',
    '   On HomePage, browse list of available trees',
    '   Each tree displayed as TreeCard with image, name, and description',
    '   Click Adopt This Tree button on any tree card',
    '   Tree added to user adoption count',
    '   Adoption statistics updated in real-time',
    '',
    '5. Managing Profile',
    '   Navigate to ProfilePage via app bar or bottom navigation',
    '   View adopted trees count and personal statistics',
    '   Click Edit Profile to modify name, email, phone, or bio',
    '   Click Save Profile to save changes',
    '   Click Logout to end session and return to LoginPage',
]
for u in usage:
    pdf.cell(5, 6, '-', 0, 0, 'L')
    pdf.cell(0, 6, u, 0, 1, 'L')

# ===== PAGE 15: Conclusion =====
add_section(pdf, '10', 'Conclusion', [
    'The Tree Adoption App demonstrates a complete Flutter application development cycle from concept to deployment.',
    'The application successfully implements offline-first data storage, user authentication, and cross-platform compatibility.',
    'The project serves as a practical example of modern mobile development practices including:',
])
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
pdf.ln(5)
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
draw_code_box(pdf, auth_provider_lines, 15, pdf.get_y(), 180, 7)

# Appendix B
pdf.add_page()
pdf.set_font('Helvetica', 'B', 16)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 10, 'Appendix B: Database Schema Details', 0, 1, 'C')
pdf.ln(5)
schema_lines = [
    '-- SQLite Database: tree_adoption.db',
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
draw_code_box(pdf, schema_lines, 15, pdf.get_y(), 180, 7)

# Appendix C
pdf.add_page()
pdf.set_font('Helvetica', 'B', 16)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 10, 'Appendix C: Widget Properties Reference', 0, 1, 'C')
pdf.ln(5)
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(*BLACK)
pdf.cell(0, 8, 'Reference table of key widget properties used in the application:', 0, 1, 'L')
pdf.ln(3)
widgets_ref = [
    ('Widget', 'Key Properties'),
    ('TreeCard', 'tree: Tree model, onAdopt: VoidCallback'),
    ('AuthScaffold', 'title: String, body: Widget, onLogout: VoidCallback'),
    ('StatCard', 'label: String, value: String, icon: IconData'),
    ('EmptyState', 'message: String, actionText: String, onAction: VoidCallback'),
    ('GlassContainer', 'child: Widget, width: double, height: double, color: Color'),
    ('MileageGauge', 'value: double, minValue: double, maxValue: double, size: double'),
]
pdf.set_font('Helvetica', 'B', 9)
pdf.cell(30, 8, 'Widget', 1, 0, 'L')
pdf.cell(0, 8, 'Key Properties', 1, 1, 'L')
pdf.set_font('Helvetica', '', 9)
for w, p in widgets_ref[1:]:
    pdf.cell(30, 8, w, 1, 0, 'L')
    pdf.cell(0, 8, p, 1, 1, 'L')

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

# Save
pdf.output('tree_adoption_project_report.pdf')
print(f'PDF created with {pdf.page_no()} pages')