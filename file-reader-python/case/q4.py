import helper
import pefile

# /Users/mgmetehan/Desktop/assessment-samples/
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
        if twoBytes[0:2]==b"MZ" or pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_AMD64'] == pe.FILE_HEADER.Machine or pefile.MACHINE_TYPE['IMAGE_FILE_MACHINE_I386'] == pe.FILE_HEADER.Machine :
            print("This file is a PE file")
            print(newPath)
            for section in pe.sections:
                print(section.Name.decode('utf-8').strip('\x00'))
            helper.searchForStringInFile(newPath, search_string.encode())
        else:
            print(newPath)
            print("This file is not a PE file")