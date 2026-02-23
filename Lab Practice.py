dict1 = {}

dict2 = {
    1: "Abubaker",
    2: ["Ali", "Hassan", "Ismaeel"],
    3: "Najaf",
    4: "Hud"
}
dict3 = {
    "subject1": "Math",
    "subject2": "Science",
    "subject3": "English"
}
# print(len(dict2))

from collections import ChainMap
c = ChainMap(dict1, dict2, dict3)
# print(c)

# for key,value in dict3.items():
    # print(key,value)

dict1[0] = "Ismaeel"
dict1[1] = "Ali"
dict1[2] = "Abubaker"
dict1[3] = "Najaf"
dict1[4] = ["hud","Aqib","shahbaz"]
dict1[5] = {"nested": {"subject1": "Math", "subject2": "Science",}}
# print (dict1[5])

for key,value in dict1.items():
    list1 = []
    list1.append(key)
    print (list1)
  

