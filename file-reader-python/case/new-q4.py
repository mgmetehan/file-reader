import os
import pefile
import helper

# /Users/mgmetehan/Desktop/assessment-samples/
path = input("Enter your path: ")
search_string = input("Enter your search string: ")
byte_string = search_string.encode('utf-8')

for file_name in os.listdir(path):
    print("*" * 50)
    file_path = os.path.join(path, file_name)
    twoBytes=helper.readFileAllByte(file_path)
    if os.path.isfile(file_path):
        with open(file_path, "rb") as file:
            if twoBytes[0:2] == b"MZ":
                pe = pefile.PE(file_path)
                if (pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_AMD64'] == pe.FILE_HEADER.Machine or pefile.MACHINE_TYPE[
                    'IMAGE_FILE_MACHINE_I386'] == pe.FILE_HEADER.Machine):
                    if pe.NT_HEADERS.Signature == pefile.IMAGE_NT_SIGNATURE:
                        print("=================================================")
                        helper.searchForStringInFile(file_path, search_string.encode())
                        for section in pe.sections:
                            data = section.get_data()
                            if byte_string in data:
                                section_name = section.Name.decode().rstrip('\x00')
                                print(file_path)
                                print(section_name)
            else:
                print("This file is not a PE file")