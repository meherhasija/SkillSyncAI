import pymupdf


def extract_text_from_pdf(pdf_file):
    try:
        pdf_bytes = pdf_file.getvalue()

        document = pymupdf.open(
            stream=pdf_bytes,
            filetype="pdf"
        )

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text.strip()

    except Exception as error:
        raise ValueError("Unable to read this PDF file.") from error