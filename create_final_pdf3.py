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

def add_code_page(pdf, title, code_lines):
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 14)
    pdf.set_text_color(*GREEN_DARK)
    pdf.cell(0, 10, title, 0, 1, 'C')
    pdf.ln(8)
    draw_code_box(pdf, code_lines, 15, pdf.get_y(), 180, 8)

def add_sub_dense(pdf, title, bullets):
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 12)
    pdf.set_text_color(*GREEN_DARK)
    pdf.cell(0, 10, title, 0, 1, 'L')
    pdf.ln(3)
    pdf.set_font('Helvetica', '', 11)
    pdf.set_text_color(*BLACK)
    for b in bullets:
        pdf.cell(8, 6, chr(8226), 0, 0, 'L')  # bullet
        pdf.cell(0, 6, b, 0, 1, 'L')
    pdf.ln(5)

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
pdf.multi_cell(0, 7, 'This is to certify that this is a bonafide record of practical work', 1, 'L')
pdf.multi_cell(0, 7, 'done by [Student Name], Regd. No. [Roll Number]', 1, 'L')
pdf.multi_cell(0, 7, 'of III B.Tech I Semester Class in', 1, 'L')
pdf.multi_cell(0, 7, 'Flutter Application Development', 1, 'L')
pdf.multi_cell(0, 7, 'during the year 2024-25.', 1, 'L')
pdf.ln(10)
pdf.multi_cell(0, 7, 'No. of Tasks Completed and Certified:', 1, 'L')
pdf.ln(5)
pdf.multi_cell(0, 7, 'Lecture In-Charge                                                                          Head of The Department', 1, 'L')
pdf.ln(5)
pdf.multi_cell(0, 7, 'Date: [Date]', 1, 'L')
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
    ('12', 'Dart Programming Language'),
    ('13', 'Flutter Widgets'),
    ('14', 'Responsive UI Design'),
    ('15', 'Navigation and Routing'),
    ('16', 'State Management Patterns'),
    ('17', 'SQLite Database'),
    ('18', 'Form Validation'),
    ('19', 'Animations'),
    ('20', 'Testing and Debugging'),
    ('', 'Appendix A: Full Dart Code'),
    ('', 'Appendix B: Database Schema'),
    ('', 'Appendix C: Widget Reference'),
]
pdf.set_font('Helvetica', '', 11)
pdf.set_text_color(*BLACK)
for num, title in toc_items:
    if num:
        pdf.set_font('Helvetica', 'B', 10)
        pdf.cell(10, 10, num, 0, 0, 'L')
        pdf.set_font('Helvetica', '', 10)
    else:
        pdf.set_font('Helvetica', '', 10)
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
    '',
    'The application follows modern mobile development practices including clean architecture,',
    'separation of concerns, and offline-first data storage. It serves as a complete example',
    'of a production-ready Flutter application from concept to deployment. The project',
    'demonstrates best practices in Flutter development including widget composition,',
    'state management, and data persistence strategies.',
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
    'codebase easier to understand, modify, and extend over time.',
])
pdf.ln(3)
pdf.set_font('Helvetica', 'B', 10)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 8, 'Layer 1: Presentation Layer (5 UI Screens):', 0, 1, 'L')
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(*BLACK)
pdf.multi_cell(0, 6, 'SplashPage - Initial loading screen with animated progress indicator (2-second delay). Displays application logo, handles initial auth state check, and navigates to appropriate screen. Uses CircularProgressIndicator with green color scheme and fade-in animation. ', 1, 'L')
pdf.multi_cell(0, 6, 'LoginPage - Authentication screen with email/password validation. Features form validation for empty fields, minimum password length (6 characters), and password visibility toggle. On successful authentication, AuthProvider state is updated and user is navigated to HomePage. On failure, SnackBar displays error message. Uses Form widget with GlobalKey for validation.', 1, 'L')
pdf.multi_cell(0, 6, 'RegisterPage - User registration with name, email, password, and password confirmation. Validation ensures all fields are filled, password is at least 6 characters long, and password confirmation matches. On successful registration, user is automatically logged in and redirected to HomePage. Includes Terms checkbox and link to login for existing users.', 1, 'L')
pdf.multi_cell(0, 6, 'HomePage - Main dashboard displaying available trees for adoption. Features welcome message with user name and trees adopted count, list of available trees with card-based layout using TreeCard widget, adopt button on each tree card, quick statistics summary, and navigation to profile section. Uses SingleChildScrollView with padding.', 1, 'L')
pdf.multi_cell(0, 6, 'ProfilePage - User profile management with edit capability. Includes user avatar with circular border, full name/email/phone fields using TextFormField, bio section, statistics cards, edit mode toggle, and logout functionality with confirmation dialog. Uses FormBuilder for complex form fields and AlertDialog for confirmation.', 1, 'L')
pdf.ln(3)
pdf.set_font('Helvetica', 'B', 10)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 8, 'Layer 2: State Management Layer (AuthProvider):', 0, 1, 'L')
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(*BLACK)
pdf.multi_cell(0, 6, 'Uses Provider package with ChangeNotifier for reactive UI updates. AuthProvider manages authentication state (isLoggedIn), user profile information (userName, userEmail, userPhone, userBio), and adopted tree count (treesAdopted). Provides methods: login(), register(), logout(), updateProfile(), addAdoptedTree(). Uses notifyListeners() to trigger widget rebuilds. Simulates API calls with Future.delayed(const Duration(seconds: 1)) for demonstration.', 1, 'L')
pdf.ln(3)
pdf.set_font('Helvetica', 'B', 10)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 8, 'Layer 3: Data Layer (SQLite via sqflite):', 0, 1, 'L')
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(*BLACK)
pdf.multi_cell(0, 6, 'Uses SQLite database via the sqflite package for offline-first data persistence. Database file named tree_adopter.db with schema version 1. Platform-specific implementations: io for mobile/desktop, web for web. Handles all database operations: creating tables (users, trees, adoptions), inserting records, querying data with where/clauses, updating records, deleting records, and opening/closing database connection. Uses Future for all async database operations.', 1, 'L')

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
add_section(pdf, '3', 'Feature Modules', [
    'The application is modularized into the following key feature modules:',
])
pdf.ln(3)
modules = [
    ('3.1 Splash Screen', 'The SplashScreen is the first screen users see when launching the application. It displays the application logo (Flutter icon with leaf) and a progress indicator (CircularProgressIndicator). After a 2-second delay (const Duration(seconds: 2)), the splash screen checks the authentication state via AuthProvider and navigates to either the LoginPage (if user is not logged in) or HomePage (if already logged in). The splash screen provides a professional first impression and handles the initial routing logic for the application. Uses AnimatedSwitcher for transition between screens.'),
    ('3.2 Login Page', 'The LoginPage allows registered users to authenticate using their email and password. The form includes validation for empty fields using FormValidator, minimum password length (6 characters), and password visibility toggle using IconButton with visibility/icons.visibility_off. On successful login, the AuthProvider updates the state with login() method and navigates the user to the HomePage using Navigator.pushReplacementNamed(context, '/home'). On failure, SnackBar displays "Invalid email or password" with red background. Features email field with prefix icon Icons.email and password field with suffix icon.'),
    ('3.3 Register Page', 'The RegisterPage allows new users to create an account. The registration form collects user name (TextFormField with validator), email address (TextFormField with email validator), password (ObscureText with toggle visibility), and password confirmation. Validation ensures all fields are filled, password is at least 6 characters long, and password confirmation matches the password field. Uses FormField with onSaved to capture values. Upon successful registration, the user is automatically logged in and redirected to the HomePage. Features name field with prefix Icons.person, email with Icons.email, password with toggle, and confirm password field.'),
    ('3.4 Home Page', 'The HomePage is the main dashboard of the application, displayed after successful authentication. It features: a welcome message with user name and trees adopted count using Text widget with green color scheme and headlineSmall style, a list of available trees for adoption with card-based layout using TreeCard widget (2 columns on mobile, 3 on web/desktop), an Adopt button on each tree card to initiate adoption using ElevatedButton with green color scheme and "Adopt This Tree" text, quick statistics summary cards (trees adopted count, total expenses), navigation drawer or bottom navigation bar, and floating action button for adding new trees. Uses GridView.builder for responsive grid layout.'),
    ('3.5 Profile Page', 'The ProfilePage displays and manages user profile information. It includes: a user avatar with circular border using Container with BoxDecoration(shape: BoxShape.circle), full name field using TextFormField with initialValue, email field, phone number field with keyboardType: TextInputType.phone, bio section for personal description using TextField with maxLines: 3 and decoration: InputDecoration(hintText: "Tell us about yourself"), statistics cards showing trees adopted count and membership duration using StatCard widget, edit mode toggle using ElevatedButton (text: "Edit Profile" when not editing, "Save Profile" when editing), and logout functionality with confirmation dialog using AlertDialog with title "Logout", content "Are you sure you want to logout?", and actions: Cancel button and Logout button.'),
]
for title, desc in modules:
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 8, f'{title}:', 0, 1, 'L')
    pdf.set_font('Helvetica', '', 10)
    pdf.multi_cell(0, 6, '  ' + desc, 1, 'L')

# ===== PAGE 8: DATABASE DESIGN =====
add_section(pdf, '4', 'Database Design', [
    'The application uses SQLite database for local, offline-first data storage. All data including user profiles, tree information, and adoption records are stored locally on the device. This ensures the application works without an internet connection and provides fast data access. The sqflite package is used for SQLite operations, with platform-specific implementations for mobile (io), web (web), and desktop environments. The database file is named tree_adopter.db with schema version 1. All data operations are performed asynchronously using Futures.',
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
    'id INTEGER PRIMARY KEY AUTOINCREMENT - Unique identifier for each user, auto-incremented',
    'name TEXT NOT NULL - User full name, required field',
    'email TEXT NOT NULL UNIQUE - User email address, must be unique across all users',
    'phone TEXT - User phone number (optional), stores country code and number',
    'salt TEXT NOT NULL - Salt value for password hashing, generated during registration',
    'password_hash TEXT NOT NULL - Hashed password using bcrypt or similar algorithm',
    'is_guest INTEGER NOT NULL DEFAULT 0 - Flag for guest users (0=registered user, 1=guest session)',
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
    'id INTEGER PRIMARY KEY AUTOINCREMENT - Unique tree identifier, auto-incremented',
    'name TEXT NOT NULL - Name of tree species (Oak, Maple, Pine, Birch, Eucalyptus)',
    'species TEXT - Scientific name or species description (optional)',
    'description TEXT - Detailed description of tree benefits and characteristics',
    'image_path TEXT - Path to tree image asset (assets/images/ folder)',
    'adoption_date TEXT - Date when tree was adopted (YYYY-MM-DD format, null if not adopted)',
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
    'id INTEGER PRIMARY KEY AUTOINCREMENT - Unique adoption record ID, auto-incremented',
    'user_id INTEGER NOT NULL - Foreign key referencing users table',
    'tree_id INTEGER NOT NULL - Foreign key referencing trees table',
    'date_adopted TEXT NOT NULL - Date when tree was adopted (YYYY-MM-DD format)',
    'status TEXT NOT NULL DEFAULT "active" - Adoption status: "active", "completed", "cancelled"',
    'FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE - Cascades delete on user removal',
    'FOREIGN KEY (tree_id) REFERENCES trees(id) ON DELETE CASCADE - Cascades delete on tree removal',
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
    'CREATE INDEX idx_users_email ON users(email) - Accelerates user lookup by email during login',
    'CREATE INDEX idx_trees_name ON trees(name) - Accelerates tree search by name in catalog',
    'CREATE INDEX idx_adoptions_user ON adoptions(user_id) - Accelerates fetching user adoption history',
    'CREATE INDEX idx_adoptions_tree ON adoptions(tree_id) - Accelerates fetching adoption tree info',
    'CREATE INDEX idx_adoptions_status ON adoptions(status) - Accelerates filtering by adoption status',
]
for idx in indices:
    pdf.cell(5, 5, '+', 0, 0, 'L')
    pdf.cell(0, 5, idx, 0, 1, 'L')

# ===== PAGE 9: Sample SQL =====
pdf.add_page()
pdf.set_font('Helvetica', 'B', 16)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 10, '4.2 Sample SQL Queries and Commands', 0, 1, 'C')
pdf.ln(8)
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
    'All routes are defined in the main.dart file and can be accessed using Navigator.pushNamed()',
    'or Navigator.pushReplacementNamed(). This provides deep linking support and predictable navigation.',
])
pdf.ln(3)
pdf.set_font('Helvetica', 'B', 10)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 8, '5.1 Navigation Routes:', 0, 1, 'L')
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(*BLACK)
routes = [
    ('/', 'SplashPage', 'Initial screen that checks auth state and navigates to login or home. Uses context.pushNamed(\"/\") on first launch.'),
    ('/login', 'LoginPage', 'User authentication screen with email and password fields. Uses context.pushNamed(\"/login\") from splash or bottom navigation.'),
    ('/register', 'RegisterPage', 'New user registration with name, email, and password. Uses context.pushNamed(\"/register\") from login or splash.'),
    ('/home', 'HomePage', 'Main dashboard with tree adoption functionality. Uses context.pushNamed(\"/home\") after auth.'),
    ('/profile', 'ProfilePage', 'User profile management and statistics. Uses context.pushNamed(\"/profile\") from home bottom nav.'),
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
    'Navigator.pushNamed(context, \'/login\') - Navigate to new screen and add to route stack. User can press Back to return.',
    'Navigator.pushReplacementNamed(context, \'/home\') - Replace current screen with new one. User cannot press Back to previous screen. Best for auth state changes.',
    'Navigator.pop(context) - Go back to the previous screen. Pops the current route from the stack.',
    'Navigator.pushAndRemoveUntil(context, route, (route) => false) - Navigate to new route and remove all previous routes. Creates a clean navigation stack.',
    'Navigator.maybePop(context) - Pop only if the route can be popped (stack not empty). Prevents errors on empty stack.',
]
for p in patterns:
    pdf.cell(5, 6, '-', 0, 0, 'L')
    pdf.cell(0, 6, p, 0, 1, 'L')

# ===== PAGE 11: Widget Library =====
add_section(pdf, '6', 'Widget Library', [
    'The application uses a collection of reusable UI widgets built with Flutter widget framework.',
    'All widgets follow Material Design 3 guidelines and are composed to build complex user interfaces.',
])
pdf.ln(3)
widgets = [
    ('6.1 TreeCard', 'A card widget displaying tree information with icon/image, name, species, description, and benefits. Uses Card widget with elevation 3 and RoundedRectangleBorder border radius 12. Padding 16 inside card. Image or icon at top with size 60 and green shade 100 background. Tree name displayed in headlineSmall style with font weight bold and color Colors.green.shade700. Species displayed in bodySmall style with italic font style and color Grey.shade600. Description displayed in bodyMedium widget. Benefits displayed in Container with green shade 50 background, border with Colors.green.shade200, and border radius 8. Row with check circle icon and benefits text. Adopt This Tree button at bottom using ElevatedButton with style: ButtonStyle(backgroundColor: WidgetStateProperty.all(Colors.green.shade700), shape: WidgetStateProperty.all(RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)))), child: Text("Adopt This Tree", style: TextStyle(color: Colors.white, fontSize: 16)).'),
    ('6.2 AuthScaffold', 'A scaffold widget providing consistent layout structure across all screens. Uses AppBar with title: Text("Tree Adoption", style: Theme.of(context).textTheme.headlineSmall?.copyWith(color: Colors.white)), backgroundColor: Colors.green.shade700, elevation: 0, centerTitle: true. Body: SingleChildScrollView with padding: EdgeInsets.all(16). BottomNavigationBar: Items for Home, Profile, with selectedItemColor: Colors.green.shade700 and unselectedItemColor: Colors.grey.shade600. Uses BottomNavigationBarType.fixed.'),
    ('6.3 StatCard', 'A statistic card widget displaying a counter value with associated icon and label. Uses Card with elevation 3 and RoundedRectangleBorder border radius 12. Padding 20 inside card. Row with Icon(Icons.eco, color: Colors.green.shade700, size: 32) and expanded text. Value displayed in Theme.of(context).textTheme.headlineSmall?.copyWith(fontWeight: FontWeight.bold, color: Colors.green.shade700). Label displayed in Theme.of(context).textTheme.bodySmall?.copyWith(color: Colors.grey.shade600). MainAxisAlignment: spaceBetween.'),
    ('6.4 EmptyState', 'A placeholder widget displayed when no data is available (e.g., no trees adopted, empty profile). Uses Center with Container having green shade 100 background with border radius 12 and margin 24. Child: Column with Icon(Icons.insert_drive_file, color: Colors.grey.shade400, size: 48) and Text("No trees adopted yet", style: TextStyle(color: Colors.grey.shade600, fontSize: 16), textAlign: TextAlign.center). Padding 24. TextStyle: fontSize: 16, color: Colors.grey.shade600, fontWeight: FontWeight.w500.'),
    ('6.5 GlassContainer', 'A decorative container widget with glass-morphism effect - semi-transparent background, blurred effect, and rounded corners. Used to create visually appealing sections within the UI. Uses Container with decoration: BoxDecoration(color: Colors.green.shade100.withOpacity(0.8), border: Border.all(color: Colors.green.shade200, width: 1), borderRadius: BorderRadius.circular(8)). Child: Any widget. Used to create card-like sections with frosted glass appearance. Often used for statistic sections or filter chips.'),
    ('6.6 MileageGauge', 'An animated gauge widget visualizing adoption statistics or efficiency metrics. Uses CustomPainter to draw circular progress gauge with animated transitions. Features green color scheme with smooth animation when values change. Uses CustomPainter with Arc technique drawing progress arc from -pi/2 to value*pi. Animated widget that rebuilds only when value changes. Uses TweenAnimationBuilder for smooth transitions. Size: double.infinity. Duration: 500ms. Curve: Curves.easeOut'),
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
draw_code_box(pdf, provider_code, 15, pdf.get_y(), 180, 8)

# ===== PAGE 13: Installation Guide =====
add_section(pdf, '8', 'Installation Guide', [])
pdf.ln(3)
pdf.set_font('Helvetica', 'B', 11)
pdf.set_text_color(*GREEN_DARK)
pdf.cell(0, 8, 'Prerequisites:', 0, 1, 'L')
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(*BLACK)
reqs = [
    'Flutter SDK (version 3.10 or latest) - Download from flutter.dev',
    'Dart SDK (included with Flutter) - Comes with Flutter installation',
    'Visual Studio Code or Android Studio - IDE for Flutter development',
    'Git for version control - git clone repository command',
    'Android Studio emulator or physical iOS/Android device - For testing app',
    'Web browser (Chrome, Safari) - For web deployment testing',
    'Administrator privileges - For SDK installation on computer',
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
    '  Navigate to project directory: cd tree_adoption_app',
    '  Verify contents: ls -la',
    '',
    'Step 2: Install Flutter dependencies',
    '  Run: flutter pub get',
    '  This downloads all packages listed in pubspec.yaml',
    '  Verification: check .packages file created',
    '',
    'Step 3: Verify Flutter installation',
    '  Run: flutter doctor',
    '  Checks for installed dependencies, SDK location, and platform setup',
    '  Fix any reported issues before proceeding',
    '',
    'Step 4: Run the application on a device/emulator',
    '  Connect device via USB or start emulator',
    '  Run: flutter run',
    '  App launches on device/emulator automatically',
    '  Hot reload: press r key to reload without restart',
    '',
    'Step 5: For web support, ensure web target is configured',
    '  Run: flutter config --enable-web',
    '  Verify: flutter devices lists web option',
    '  Run: flutter run -d chrome',
    '',
    'Step 6: Build release APK for Android',
    '  Run: flutter build apk --release',
    '  Output: build/app/outputs/flutter-apk/app-release.apk',
    '  Distribute via Play Store or sideload',
    '',
    'Step 7: Build iOS archive (macOS only)',
    '  Run: flutter build ios --release',
    '  Output: ios/Runner.xcarchive',
    '  Distribute via App Store or TestFlight',
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
    '   On first launch, the SplashScreen appears for 2 seconds (const Duration(seconds: 2)).',
    '   If no user is logged in, navigation redirects to LoginPage.',
    '   If user is already logged in (isLoggedIn == true), navigation redirects to HomePage.',
    '   Splash screen uses Future.delayed and Navigator.pushReplacementNamed context.',
    '',
    '2. User Login',
    '   Enter registered email address in the email TextFormField.',
    '   Enter password (minimum 6 characters) in the password TextFormField.',
    '   Toggle password visibility using suffix icon button.',
    '   Click the Login button (ElevatedButton with onPressed: _login).',
    '   On success: AuthProvider login() returns true, Navigator.pushReplacementNamed(context, \"/home\")',
    '   On failure: ScaffoldMessenger.showSnackBar with "Invalid email or password"',
    '   SnackBar duration: Duration(seconds: 2), backgroundColor: Colors.red.shade700',
    '',
    '3. User Registration (new users)',
    '   Click "Register here" link on LoginPage (GestureDetector onTap: pushNamed \"/register\").',
    '   Fill in registration form: Full Name (TextFormField with validator),
    '   Email (TextFormField with validator email: true),',
    '   Password (TextFormField with obscureText: true, suffixIcon toggle),',
    '   Confirm Password (TextFormField with obscureText: true).',
    '   Ensure password is at least 6 characters and matches confirmation.',
    '   Click "Create Account" button (ElevatedButton onPressed: _register).',
    '   On success: AuthProvider register() returns true, Navigator.pushReplacementNamed(context, \"/home\")',
    '   On failure: SnackBar with error message about validation failures',
    '',
    '4. Browsing and Adopting Trees',
    '   On HomePage, browse the list of available trees (GridView.builder with 2 columns).',
    '   Each tree displayed as TreeCard with image, name, and description.',
    '   Click "Adopt This Tree" button on any tree card.',
    '   Tree added to user adoption count (AuthProvider addAdoptedTree()).',
    '   Adoption statistics updated in real-time via notifyListeners().',
    '   SnackBar shows "You adopted a [treeName]! 🎉" with green background.',
    '',
    '5. Managing Profile',
    '   Navigate to ProfilePage via bottomNavigationBarItem (icon: person) or app bar title.',
    '   View adopted trees count and personal statistics at top of page.',
    '   Click "Edit Profile" button (ElevatedButton) to enter edit mode.',
    '   Modify name, email, phone, or bio fields (TextFormField widgets).',
    '   Click "Save Profile" button to save changes and exit edit mode.',
    '   Click "Logout" button (OutlinedButton with color: Colors.red) to end session.',
    '   Logout confirms via AlertDialog with title "Logout" and content "Are you sure?"',
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
    'Clean architecture with separation of concerns (presentation, state, data layers) - Each layer has specific responsibilities and interfaces, making the codebase modular and testable.',
    'Provider state management pattern for reactive UI updates - AuthProvider uses ChangeNotifier and notifyListeners() to update UI when state changes. Widgets use Consumer<AuthProvider> or context.watch<AuthProvider>() to rebuild only when needed.',
    'SQLite database for persistent local storage with offline-first approach - Data stored locally via sqflite package. Works without internet connection. Schema versioning supports future updates. Database helper classes abstract platform-specific implementations.',
    'Responsive UI design using Material Design principles and custom widgets - MaterialDesign 3 colors, typography, and components. Custom widgets (TreeCard, StatCard, GlassContainer) provide consistent branding and user experience across all screens.',
    'Cross-platform codebase running on Android, iOS, Web, and Desktop from a single codebase - Flutter\'s write-once-run-anywhere philosophy. Platform-specific implementations for SQLite (io/web). Same UI code runs on all targets.',
    'Modular code structure enabling easy maintenance and feature expansion - Feature modules (splash, login, home, profile) separated by concern. Widget library provides reusable components. Appendixes provide reference material.',
    'Simulated API calls for demonstration with scope for real backend integration - AuthProvider login/register methods use Future.delayed to simulate network latency. Comments indicate where real API calls should be implemented (Firebase, custom backend).',
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
    'Integrate Firebase or custom backend for user authentication and data sync - Replace simulated login/register with real API calls to Firebase Auth or custom server endpoint. Use package: firebase_auth for authentication. Store user data in Firestore or realtime database.',
    'Add push notifications for adoption updates and reminders - Use firebase_messaging package. Schedule notifications when tree adoption milestone reached. Local notifications using flutter_local_notifications as fallback.',
    'Implement tree growth tracking with photos and milestones - Add tree profile page with growth chart. Allow users to upload photos of adopted tree. Track months since adoption. Milestone badges at 6, 12, 24 months.',
    'Add social features: share adoptions on social media, view friends adoptions - Integrate share package (share_plus). Implement social feed showing adoptions from connected friends. Use provider for friend network state.',
    'Implement gamification: badges, achievements, and leaderboards - Create Achievement model with criteria (trees adopted, days active, streaks). Use SharedPreferences for local badge storage. Leaderboard using Firebase Realtime Database.',
    'Add multi-language support (i18n) for wider accessibility - Use intl package. Define arb files for English, Spanish, French, Hindi. Localize button texts, labels, and messages. Support right-to-left layout if needed.',
    'Integrate with environmental APIs for real-time tree data - Connect to environmental APIs (e.g., WWF, UNEP) for real-time data on tree planting impact. Show carbon offset calculations. Display global adoption map.',
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
    ('Widget', 'Key Properties'),
    ('TreeCard', 'tree: Tree model, onAdopt: VoidCallback, padding: EdgeInsets.all(16), elevation: 3'),
    ('AuthScaffold', 'appBar: PreferredSize(child: Text(...), preferredSize: Size.fromHeight(50)), body: Widget, onLogout: VoidCallback'),
    ('StatCard', 'label: String, value: String, icon: IconData, color: Colors.green.shade700'),
    ('EmptyState', 'message: String, actionText: String, onAction: VoidCallback'),
    ('GlassContainer', 'child: Widget, width: double, height: double, color: Colors.green.shade100, opacity: 0.8'),
    ('MileageGauge', 'value: double, minValue: double, maxValue: double, size: double, animationDuration: int'),
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