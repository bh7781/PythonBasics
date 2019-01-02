info = {
    101: 'Chinmay',
    102: 'Nachiket',
    103: 'Uttej',
    104: 'Shubham'}

print(type(info))
print(info)
info[104] = 'Tirmya'
info[100] = 'Aniket'
print(info)

print(101 in info)
print('Chinmay' in info)

print(type(info.keys()))
print(info.keys())
print(info.values())
print(type(info.values()))

print('Chinmay' in info.values())

for k,v in info.items():
    print(k, "  ", v)
    
print(info.items())