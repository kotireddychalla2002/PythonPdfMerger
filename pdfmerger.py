import PyPDF2

def merge(*args):
    merged_pdf = PyPDF2.PdfFileMerger()
    for file in args:
        with open(file, 'rb') as f:
            pdf_reader = PyPDF2.PdfFileReader(f)
            merged_pdf.append(pdf_reader)
    merged_pdf.write('mergedPdf.pdf')