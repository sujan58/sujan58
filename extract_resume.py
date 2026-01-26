from pdfminer.high_level import extract_text
try:
    print("Using pdfminer")
    text = extract_text("SujanVresume.pdf")
    print("---START---")
    print(text.encode('utf-8', errors='ignore').decode('utf-8'))
    print("---END---")
except Exception as e:
    print(f"Error: {e}")
