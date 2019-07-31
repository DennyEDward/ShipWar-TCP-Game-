import json

list = [[1,2],[3,4],5,6]
a = json.dumps(list)

print(type(a))

b =json.loads(a)
print(b,type(b))

