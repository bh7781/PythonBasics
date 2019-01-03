emp = '{"id" : "101", "name" : "Chinmay", "Age" : "25"}'

import json
data = json.loads(emp)
print(type(data))
print(data, '\n\n')

for k,v in data.items():
    print(k, '    ', v)