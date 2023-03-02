import helper
# /Users/mgmetehan/Desktop/chomar/C-ProtStajyerproje.pdf
# b"MALLWARE"
path = input("Enter your path: ")
search_string = input("Enter your search string: ")
result=helper.searchForStringInFile(path, search_string.encode())
