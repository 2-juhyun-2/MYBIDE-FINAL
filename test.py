from pymongo import MongoClient 
client = MongoClient('localhost', 27017)
db = client.fake

import re



# print(db.users.count("_id"))
# db.users.distinct("_id"); 
# # > db.users.find({"_id" : "ggreastyl0"},{_id:0,"image.tag":"F"}).pretty()
# print(db.users.aggregate( [ { $project : {_id:0, image: 1 } } ] ).pretty())

a = list(db.users.find({"image.image_path":"1.png"},{"_id":0,"image.tag":1}))
a = str(a)

a = a.split("tag")
b = []
def k(a):
    a = str(a)
    new_a = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]',"",a)
    new_a = new_a.replace('{','')
    new_a = new_a.replace('}','')
    return new_a
for i in range(1,len(a)):
    k(a[i])
    b.append(k(a[i]))
b
print(b)
# { "image" : [ { "tag" : [ "전라남도 고흥군", "크롭컷", "M" ] }, { "tag" : [ "서울특별시 송파구", "무스", "M" ] } ] }