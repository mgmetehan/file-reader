import helper
import pefile

# /Users/mgmetehan/Desktop/assessment-samples/
# /Users/mgmetehan/Desktop/assessment-samples/1A1AD71CA246E37E1D4EC419C9E78F8191F08F2BC7F5D6F1570772F630B666C7
path = input("Enter your path: ")
search_string = input("Enter your search string: ")
list=helper.listFilesInDir(path)

listLength=len(list)

for i in range(listLength):
    newFile = str(list[i])
    newPath = str(path + newFile)
    twoBytes=helper.readFileAllByte(newPath)
    pe = pefile.PE(newPath)
    for entry in pe.OPTIONAL_HEADER.DATA_DIRECTORY:
        print("*" * 50)
        print(pe.FILE_HEADER.Machine)
        #print(entry.name)
        for section in pe.sections:
            if twoBytes[0:2]==b"MZ" :
                if (pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_AMD64'] == pe.FILE_HEADER.Machine or pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_I386'] == pe.FILE_HEADER.Machine ):
                    if pe.NT_HEADERS.Signature == pefile.IMAGE_NT_SIGNATURE:
                        print("This file is a PE file")
                        print(newPath)
                        print(section.Name.decode('utf-8').strip('\x00'))
                        helper.searchForStringInFile(newPath, search_string.encode())
            else:
                print(newPath)
                print("This file is not a PE file")
