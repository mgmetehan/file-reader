import os

def readFileByteByByte(filename):
    bytes_list = []
    with open(filename, "rb") as f:
        byte = f.read(1)
        while byte != b"":
            # Do stuff with byte.
            bytes_list.append(byte)
            byte = f.read(1)
    return bytes_list

def readFileAllByte(filename):
    with open(filename, "rb") as f:
        byte = f.read()
    return byte

def listFilesInDir(directory):
    file_list = []
    for path in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, path)):
            file_list.append(path)
    return file_list

def searchForStringInFile(file_path, search_string):
    result = readFileAllByte(file_path)
    length = len(result)
    search_len = len(search_string)
    isFind = False

    for i in range(length - search_len + 1):
        if result[i:i + search_len] == search_string:
            print("Found at offset", i)
            isFind = True
        else:
            isFind = False

    if isFind == False:
        print("MALLWARE is not found!")