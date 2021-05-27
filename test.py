from os import replace
from pymongo import MongoClient 
client = MongoClient('localhost', 27017)
db = client.fake

import re

image_name = "2.jpg"
# # image_name == name



def k(a):
    a = str(a)
    new_a = re.sub('[-=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]',"",a)
    new_a = new_a.replace('{','')
    new_a = new_a.replace('}','')
    new_a = new_a.replace('tag','')
    return new_a

# print(db.users.count("_id"))
# db.users.distinct("_id"); 
# # > db.users.find({"_id" : "ggreastyl0"},{_id:0,"image.tag":"F"}).pretty()
# print(db.users.aggregate( [ { $project : {_id:0, image: 1 } } ] ).pretty())
# class hashTag:
#     def show_all_hashtag(self,image_name):
a = list(db.users.find({"image.image_path":image_name},{"_id":0,"image.image_path":1,"image.tag":1}))
print(a)
a = str(a)
a = re.sub('[-=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]',"",a)
a = a.replace('{','')
a = a.replace('}','')
a = a.replace('tag','')
print(a)

a = a.split("image_path")
# print(type(a))
b = []

for i in range(1,len(a)):
    
    if image_name in a[i]:
        b.append(a[i])
        aa = a[i]
        b = aa.split(' ')
        vv = b.count('')
        for p in range(0,vv):
            b.remove('')
del b[0]
print(type(b))
print(b)


# a = hashTag()
# k = list(a.show_all_hashtag(image_name))
# print(k)
# if name in b:
# { "image" : [ { "tag" : [ "전라남도 고흥군", "크롭컷", "M" ] }, { "tag" : [ "서울특별시 송파구", "무스", "M" ] } ] }




# def k(a):
#     a = str(a)
#     new_a = re.sub('[-=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]',"",a)
#     new_a = new_a.replace('{','')
#     new_a = new_a.replace('}','')
#     new_a = new_a.replace('tag','')
#     return new_a