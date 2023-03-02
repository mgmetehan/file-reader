import os

dir_path = "/Users/mgmetehan/Desktop/chomar/"
res = []

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
print(res)



