import docx2txt

def docx2txt(docx_file_path):
    try:
        txt_file_path = "/Users/mgmetehan/Desktop/output_file.txt"
        text = docx2txt.process(docx_file_path)
        with open(txt_file_path, "w", encoding="utf-8") as f:
            f.write(text)
        f.close()
        return txt_file_path
    except Exception:
        print("Could not read to file")
