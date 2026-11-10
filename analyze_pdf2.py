import pypdf
pdf = pypdf.PdfReader(r'D:\tree_adoption\Fuel_consumption_tracker_final0.pdf')
for i in range(10, 25):
    text = pdf.pages[i].extract_text()
    print(f'=== PAGE {i} ===')
    if text:
        print(text[:500])
    print()