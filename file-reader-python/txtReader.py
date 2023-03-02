def read_txt_two_chars(path):
    try:
        f = open(path, "r")
        result = f.read(2)
        f.close()
        return result
    except Exception:
        print("Could not read to file")


