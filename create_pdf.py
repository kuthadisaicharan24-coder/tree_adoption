import fpdf
import os

class PDF(fpdf.FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font('Helvetica', 'I', 8)
            self.cell(0, 5, 'Tree Adoption App - Project Report', 0, 0, 'C')
            self.ln(8)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# ===== COLOR PALETTE =====
GREEN_700 = (34, 139, 34)
GREEN_600 = (60, 179, 113)
GREEN_500 = (32, 178, 170)
GREEN_300 = (152, 251, 152)
GREEN_100 = (244, 247, 245)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED_700 = (178, 34, 34)

def set_fill_color(r, g, b):
    pdf.set_fill_color(r, g, b)

def set_text_color(r, g, b):
    pdf.set_text_color(r, g, b)

def set_font(name, style='', size=12):
    pdf.set_font(name, style, size)

def write_text(text, x=10, y=None, align='L'):
    if y is not None:
        pdf.set_xy(x, y)
    pdf.multi_cell(0, 6, text, align, fill=False)

# ===== COVER PAGE =====
pdf.add_page()
set_fill_color(*GREEN_700)
pdf.ln(30)

# Title area
set_font('Helvetica', 'B', 28)
set_text_color(*WHITE)
write_text('Tree Adoption App', 50, 35, 'C')

set_font('Helvetica', '', 16)
set_text_color(*GREEN_300)
write_text('A Flutter Application for Environmental Conservation', 50, 55, 'C')

pdf.ln(30)

# Project info
set_font('Helvetica', '', 12)
set_text_color(*WHITE)
info_items = [
    ('Project:', 'Tree Adoption App'),
    ('Platform:', 'Flutter (Cross-platform Mobile/Web)'),
    ('Language:', 'Dart'),
    ('State Management:', 'Provider'),
    ('Database:', 'SQLite (offline-first)'),
    ('Author:', 'Your Name'),
    ('Version:', '1.0.0'),
]

for i, (label, value) in enumerate(info_items):
    set_font('Helvetica', 'B', 11)
    write_text(f'{label}  ', 50, 80 + i * 10, 'R')
    set_font('Helvetica', '', 11)
    write_text(value, 70, 80 + i * 10, 'L')

pdf.ln(30)

# University info
set_font('Helvetica', 'I', 11)
set_text_color(*GREEN_300)
write_text('Developed as a Final Year Project', 50, pdf.get_y(), 'C')
pdf.ln(5)
write_text('for Computer Science and Engineering', 50, pdf.get_y(), 'C')

# ===== TABLE OF CONTENTS =====
pdf.add_page()
set_font('Helvetica', 'B', 16)
set_text_color(*GREEN_700)
write_text('Table of Contents', 50, 20, 'C')

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
]

set_font('Helvetica', '', 12)
set_text_color(*BLACK)
for i, (num, title) in enumerate(toc_items):
    set_font('Helvetica', '', 12)
    write_text(f'{num}.  {title}', 20, 45 + i * 12, 'L')

# ===== PAGE 1: PROJECT OVERVIEW =====
pdf.add_page()
set_font('Helvetica', 'B', 16)
set_text_color(*GREEN_700)
write_text('1. Project Overview', 20, 20)

set_font('Helvetica', '', 12)
set_text_color(*BLACK)
write_text(
    'The Tree Adoption App is a cross-platform Flutter application designed to facilitate '
    'tree adoption and environmental conservation. The application allows users to register, '
    'login, view available trees, adopt trees, and track their adopted trees through a '
    'user profile interface.',
    20, 35)

set_font('Helvetica', 'B', 12)
set_text_color(*GREEN_700)
write_text('Key Features:', 20, 55)

features = [
    'User authentication (login/register/logout)',
    'Tree adoption tracking',
    'Profile management',
    'Statistics dashboard (trees adopted)',
    'Offline data storage with SQLite',
    'Cross-platform support (Android, iOS, Web, Desktop)',
]

set_font('Helvetica', '', 11)
set_text_color(*BLACK)
for f in features:
    write_text(f'  + {f}', 25, pdf.get_y(), 'L')

# ===== PAGE 2: SYSTEM ARCHITECTURE =====
pdf.add_page()
set_font('Helvetica', 'B', 16)
set_text_color(*GREEN_700)
write_text('2. System Architecture', 20, 20)

set_font('Helvetica', '', 12)
set_text_color(*BLACK)
write_text(
    'The application follows a layered architecture with clear separation of concerns:',
    20, 35)

layers = [
    ('Presentation Layer:', 'Screens (SplashPage, LoginPage, RegisterPage, HomePage, ProfilePage) and UI Widgets'),
    ('State Management:', 'AuthProvider using Provider/CangeNotifier pattern'),
    ('Data Layer:', 'SQLite database via sqflite package with platform-specific implementations'),
]

for label, desc in layers:
    set_font('Helvetica', 'B', 11)
    write_text(label, 25, pdf.get_y(), 'L')
    set_font('Helvetica', '', 11)
    write_text(desc, 28, pdf.get_y(), 'L')
    pdf.ln(6)

set_font('Helvetica', 'B', 12)
set_text_color(*GREEN_700)
write_text('Data Flow:', 20, pdf.get_y() + 5)

write_text(
    'User Action --> Widget -> AuthProvider (ChangeNotifier) -> setState --> SQLite Database --> UI Update',
    25, pdf.get_y() + 10, 'L')

# ===== PAGE 3: FEATURE MODULES =====
pdf.add_page()
set_font('Helvetica', 'B', 16)
set_text_color(*GREEN_700)
write_text('3. Feature Modules', 20, 20)

modules = [
    ('Splash Screen:', 'Initial loading screen with progress indicator, redirects to login or home based on auth state'),
    ('Login Page:', 'Email/password authentication with simulated API call'),
    ('Register Page:', 'User registration with name, email, password confirmation'),
    ('Home Page:', 'Main dashboard displaying available trees with adopt functionality'),
    ('Profile Page:', 'User profile management with edit capability and statistics'),
]

set_font('Helvetica', '', 11)
set_text_color(*BLACK)
for i, (title, desc) in enumerate(modules):
    set_font('Helvetica', 'B', 11)
    write_text(f'{i+1}. {title}', 25, 30 + i * 28, 'L')
    set_font('Helvetica', '', 11)
    write_text(desc, 30, pdf.get_y(), 'L')
    pdf.ln(3)

# ===== PAGE 4: DATABASE DESIGN =====
pdf.add_page()
set_font('Helvetica', 'B', 16)
set_text_color(*GREEN_700)
write_text('4. Database Design', 20, 20)

set_font('Helvetica', '', 11)
set_text_color(*BLACK)

write_text('The application uses SQLite for local, offline-first data storage.', 20, 35)

tables = [
    ('users', ['id INTEGER PRIMARY KEY AUTOINCREMENT', 'name TEXT NOT NULL', 'email TEXT NOT NULL UNIQUE', 'phone TEXT', 'salt TEXT NOT NULL', 'password_hash TEXT NOT NULL', 'is_guest INTEGER NOT NULL DEFAULT 0']),
    ('vehicles', ['id INTEGER PRIMARY KEY AUTOINCREMENT', 'user_id INTEGER NOT NULL', 'name TEXT NOT NULL', 'fuel_type TEXT NOT NULL', 'tank_capacity REAL NOT NULL', 'FOREIGN KEY (user_id) REFERENCES users(id)']),
    ('fuel_logs', ['id INTEGER PRIMARY KEY AUTOINCREMENT', 'user_id INTEGER NOT NULL', 'vehicle_id INTEGER NOT NULL', 'date TEXT NOT NULL', 'odometer REAL NOT NULL', 'fuel_volume REAL NOT NULL', 'total_cost REAL NOT NULL', 'is_full_tank INTEGER NOT NULL DEFAULT 0', 'FOREIGN KEY (user_id) REFERENCES users(id)', 'FOREIGN KEY (vehicle_id) REFERENCES vehicles(id)']),
]

for table_name, columns in tables:
    set_font('Helvetica', 'B', 11)
    write_text(f'{table_name.upper()} Table:', 25, pdf.get_y(), 'L')
    set_font('Helvetica', '', 9)
    for col in columns:
        write_text(f'  - {col}', 28, pdf.get_y(), 'L')
        pdf.ln(3)
    pdf.ln(5)

# ===== PAGE 5: SCREEN NAVIGATION =====
pdf.add_page()
set_font('Helvetica', 'B', 16)
set_text_color(*GREEN_700)
write_text('5. Screen Navigation', 20, 20)

set_font('Helvetica', '', 11)
set_text_color(*BLACK)

write_text('The application uses named routes for navigation:', 20, 35)

routes = [
    ('/', 'SplashPage - Initial screen, checks auth state and navigates accordingly'),
    ('/login', 'LoginPage - User authentication'),
    ('/register', 'RegisterPage - New user registration'),
    ('/home', 'HomePage - Main dashboard with tree adoption'),
    ('/profile', 'ProfilePage - User profile and statistics'),
]

set_font('Helvetica', '', 11)
for route, desc in routes:
    write_text(f'  {route}: {desc}', 25, pdf.get_y(), 'L')
    pdf.ln(3)

# ===== PAGE 6: WIDGET LIBRARY =====
pdf.add_page()
set_font('Helvetica', 'B', 16)
set_text_color(*GREEN_700)
write_text('6. Widget Library', 20, 20)

set_font('Helvetica', '', 11)
set_text_color(*BLACK)

write_text('Reusable UI components used throughout the application:', 20, 35)

widgets = [
    'TreeCard - Card widget displaying tree information with adopt button',
    'AuthScaffold - Scaffold with consistent app bar and navigation',
    'StatCard - Statistic card displaying counters (trees adopted)',
    'MileageGauge - Gauge widget for visual representation',
    'EmptyState - Placeholder widget for empty states',
    'GlassContainer - Transparent container with rounded corners',
    'AnimatedEfficiencyGauge - Animated gauge for efficiency metrics',
    'DashboardChartToggle - Toggle for chart/view modes',
]

for w in widgets:
    write_text(f'  + {w}', 25, pdf.get_y(), 'L')
    pdf.ln(3)

# ===== PAGE 7: STATE MANAGEMENT =====
pdf.add_page()
set_font('Helvetica', 'B', 16)
set_text_color(*GREEN_700)
write_text('7. State Management', 20, 20)

set_font('Helvetica', '', 11)
set_text_color(*BLACK)

write_text('The application uses Provider for state management with a single AuthProvider:', 20, 35)

provider_features = [
    'Manages authentication state (isLoggedIn, userName, userEmail)',
    'Tracks adopted tree count (treesAdopted)',
    'Provides login(), register(), logout(), updateProfile(), addAdoptedTree() methods',
    'Uses ChangeNotifier to notify listeners of state changes',
    'Simulated API calls with Future.delayed for demonstration',
]

for f in provider_features:
    write_text(f'  + {f}', 25, pdf.get_y(), 'L')
    pdf.ln(3)

# ===== PAGE 8: INSTALLATION =====
pdf.add_page()
set_font('Helvetica', 'B', 16)
set_text_color(*GREEN_700)
write_text('8. Installation Guide', 20, 20)

set_font('Helvetica', '', 11)
set_text_color(*BLACK)

write_text('Prerequisites:', 20, 35)

requirements = [
    'Flutter SDK (latest version)',
    'Dart SDK (included with Flutter)',
    'Visual Studio Code or Android Studio',
    'Git',
]

for r in requirements:
    write_text(f'  - {r}', 25, pdf.get_y(), 'L')
    pdf.ln(3)

write_text('Steps:', 20, pdf.get_y() + 5)

steps = [
    '1. Clone the repository: git clone <repository-url>',
    '2. Navigate to project directory: cd tree_adoption',
    '3. Install dependencies: flutter pub get',
    '4. Run on device/emulator: flutter run',
    '5. Ensure device has Flutter and Dart installed',
]

for s in steps:
    write_text(f'{s}', 25, pdf.get_y(), 'L')
    pdf.ln(3)

# ===== PAGE 9: USAGE =====
pdf.add_page()
set_font('Helvetica', 'B', 16)
set_text_color(*GREEN_700)
write_text('9. Usage Instructions', 20, 20)

set_font('Helvetica', '', 11)
set_text_color(*BLACK)

write_text('Upon launching the application:', 20, 35)

usage_steps = [
    'Splash screen appears for 2 seconds, then redirects based on login status',
    'If not logged in: navigates to LoginPage',
    'If already logged in: navigates directly to HomePage',
    'Login: Enter email and password, click Login button',
    'Register: Fill in name, email, password, confirm password, click Create Account',
    'Home Page: Browse available trees, click "Adopt This Tree" to adopt',
    'Profile Page: View adopted trees count, edit profile information, logout',
]

for u in usage_steps:
    write_text(f'  - {u}', 25, pdf.get_y(), 'L')
    pdf.ln(3)

# ===== PAGE 10: CONCLUSION =====
pdf.add_page()
set_font('Helvetica', 'B', 16)
set_text_color(*GREEN_700)
write_text('10. Conclusion', 20, 20)

set_font('Helvetica', '', 11)
set_text_color(*BLACK)

write_text(
    'The Tree Adoption App demonstrates a complete Flutter application development cycle '
    'from concept to deployment. The application successfully implements offline-first data '
    'storage, user authentication, and cross-platform compatibility. The project serves as '
    'a practical example of modern mobile development practices including:',
    20, 35)

conclusion_points = [
    'Clean architecture with separation of concerns (presentation, state, data layers)',
    'Provider state management pattern for reactive UI updates',
    'SQLite database for persistent local storage',
    'Responsive UI design using Material Design principles',
    'Cross-platform codebase running on multiple platforms from a single codebase',
]

for c in conclusion_points:
    write_text(f'  + {c}', 25, pdf.get_y(), 'L')
    pdf.ln(3)

write_text(
    'The application is ready for further enhancements including backend integration, '
    'social features, and expanded tree catalog functionality.',
    20, pdf.get_y() + 5, 'C')

# Save
output_path = 'tree_adoption_project_report.pdf'
pdf.output(output_path)
print(f'PDF created: {output_path}')
print(f'Pages: {pdf.page_no()}')