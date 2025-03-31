import sys
import PyPDF2

def merge(file_list, output_file):
    merged_pdf = PyPDF2.PdfMerger()
    for file in file_list:
        with open(file, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            merged_pdf.append(pdf_reader)
    merged_pdf.write(output_file)

def main():
    file_list = sys.argv[1:-1]
    output_file = sys.argv[-1]
    merge(file_list, output_file)

if __name__ == "__main__":
    main()