import fpdf

pdf = fpdf.FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Title page
pdf.set_font('Helvetica', 'B', 25)
pdf.set_text_color(34, 139, 34)
pdf.cell(0, 15, 'Tree Adoption App', 0, 1, 'C')
pdf.set_font('Helvetica', '', 15)
pdf.set_text_color(144, 238, 144)
pdf.cell(0, 10, 'A Flutter Application for Environmental Conservation', 0, 1, 'C')
pdf.ln(20)
pdf.set_font('Helvetica', 'I', 12)
pdf.set_text_color(169, 169, 169)
pdf.cell(0, 10, 'Final Year Project - Computer Science and Engineering', 0, 1, 'C')
pdf.ln(10)

# Simple text content for now
pdf.set_font('Helvetica', '', 12)
pdf.set_text_color(0, 0, 0)

pages_content = [
    "1. Project Overview\n\nThe Tree Adoption App is a cross-platform Flutter application designed to facilitate tree adoption and environmental conservation.",
    
    "2. System Architecture\n\nThe application follows a layered architecture with clear separation of concerns: Presentation Layer, State Management Layer, and Data Layer.",
    
    "3. Feature Modules\n\nThe application includes: Splash Screen, Login Page, Register Page, Home Page, and Profile Page.",
    
    "4. Database Design\n\nUses SQLite for local, offline-first data storage with tables for users, trees, and adoptions.",
    
    "5. Screen Navigation\n\nUses Flutter named routing system for navigation between screens.",
    
    "6. Widget Library\n\nReusable UI components including TreeCard, AuthScaffold, StatCard, EmptyState, GlassContainer, and MileageGauge.",
    
    "7. State Management\n\nUses Provider package with ChangeNotifier for reactive UI updates via AuthProvider.",
    
    "8. Installation Guide\n\nPrerequisites: Flutter SDK, Dart SDK, VS Code or Android Studio, Git. Steps include: clone repo, install dependencies, run flutter run.",
    
    "9. Usage Instructions\n\nUser workflow: Launch app -> Login/Register -> Browse trees -> Adopt trees -> Manage profile.",
    
    "10. Conclusion\n\nThe app demonstrates complete Flutter development cycle with offline-first data storage, user authentication, and cross-platform compatibility.",
]

for content in pages_content:
    pdf.multi_cell(0, 6, content, 'L')
    pdf.ln(5)

# Output
pdf.output('tree_adoption_project_report.pdf')
print(f'PDF created with {pdf.page_no()} pages')