import PyPDF2
def read_pdf_two_chars(path):
    try:
        # Open the PDF file
        with open(path, 'rb') as pdf_file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)

            # Get the first page of the PDF document
            first_page = pdf_reader.getPage(0)

            # Extract the text content of the first page
            page_content = first_page.extractText()

            # Get the first two characters of the page content
            first_chars = page_content[:2]

        # Return the first two characters
        return first_chars
    except Exception:
        print("Could not read to file")
