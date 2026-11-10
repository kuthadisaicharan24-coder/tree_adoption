import pypdf
pdf = pypdf.PdfReader(r'D:\tree_adoption\Fuel_consumption_tracker_final0.pdf')
for i in range(len(pdf.pages)):
    text = pdf.pages[i].extract_text()
    print(f'=== PAGE {i} ===')
    if text:
        try:
            print(text.encode('raw_unicode_escape', errors='replace')[:2000].decode('raw_unicode_escape', errors='replace'))
        except:
            print(text[:2000])
    else:
        print("empty")
    print()