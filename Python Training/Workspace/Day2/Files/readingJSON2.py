import json

fp = open('file1.json')

data = json.load(fp)
print(type(data), '\n\n')

for k,v in data.items() :
    print(k, '    ', v)