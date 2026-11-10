import pypdf
pdf = pypdf.PdfReader(r'D:\tree_adoption\Fuel_consumption_tracker_final0.pdf')
print(f'Total pages: {len(pdf.pages)}')
# Get first 10 pages text to understand structure
for i in range(min(10, len(pdf.pages))):
    text = pdf.pages[i].extract_text()
    print(f'=== PAGE {i} ===')
    if text:
        print(text[:500])
    print()