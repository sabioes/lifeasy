import fitz

def extract_text_from_pdf(pdf_file):
    text = ""
    doc = fitz.open(pdf_file)
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

def compare_pdfs(pdf1, pdf2):
    text1 = extract_text_from_pdf(pdf1)
    text2 = extract_text_from_pdf(pdf2)

    if text1 == text2:
        print("The PDFs are identical.")
    else:
        # Perform text comparison or analysis here
        # For example, you can use difflib to get differences between the two texts
        from difflib import unified_diff
        diff = unified_diff(text1.splitlines(), text2.splitlines())

        # Print the differences
        for line in diff:
            print(line)

if __name__ == "__main__":
    
    PDF_FOLDER = "pdfs/"

    CLUSTER_REPORT = "cluster_report_mkvfat.pdf"
    SYSTEM_REQUIREMENTS = "pasx-332-system-requirements.pdf"

    pdf_file1 = PDF_FOLDER + CLUSTER_REPORT
    pdf_file2 = PDF_FOLDER + SYSTEM_REQUIREMENTS

    compare_pdfs(pdf_file1, pdf_file2)