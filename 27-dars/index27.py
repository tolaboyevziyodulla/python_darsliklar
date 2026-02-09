import json
# import googlemaps
# from apikey import APIKEY

# gmaps = googlemaps.Client(key=APIKEY)
# data = gmaps.geocode('O\'rta Chirchiq, Toshkent, Uzbekistan')
# g = json.dumps(data[0], indent = 4, sort_keys = True)
# print(g)

x = 10
x_json = json.dumps(x)

y = 5.5
y_json = json.dumps(y)

m = True
m_json = json.dumps(m)
print(m_json)

nums = (12, 45, 23, 78)
nums_json = json.dumps(nums)
print(nums_json)
print(type(nums_json))

with open('nums.json', 'w') as file:
    json.dump(nums, file)

bemor = {
    'name' : 'ALijon Valiyev',
    'family' : False,
    'age' : 12,
    'allergy' : None,
    'medisins' : [
        {'name' : 'Analgin Dimidrol', 'result' : 0.4},
        {'name' : 'Paratsetamol', 'result' : 4.0}
    ]
}
# bemor_json = json.dumps(bemor)
bemor_json = json.dumps(bemor, indent = 4)
print(bemor_json)

with open('bemor.json', 'w') as file:
    json.dump(bemor, file, indent = 4)

bemor2 = json.loads(bemor_json)
print(bemor2)
print(type(bemor2))

filename = 'bemor.json'
with open(filename) as file:
    bemor = json.load(file)

print(bemor)