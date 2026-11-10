import pypdf
pdf = pypdf.PdfReader(r'D:\tree_adoption\Fuel_consumption_tracker_final0.pdf')
print(f'Pages: {len(pdf.pages)}')
for i in range(min(3, len(pdf.pages))):
    text = pdf.pages[i].extract_text()
    print(f'Page {i}: {text[:500] if text else "empty"}')