from os import pipe, replace
from pymongo import MongoClient 
client = MongoClient('localhost', 27017)
db = client.fake

import re

# image_name = "1.png"
# # image_name == name



# print(db.users.count("_id"))
# db.users.distinct("_id"); 
# # > db.users.find({"_id" : "ggreastyl0"},{_id:0,"image.tag":"F"}).pretty()
# print(db.users.aggregate( [ { $project : {_id:0, image: 1 } } ] ).pretty())
class hashTag:
    def show_all_hashtag(self,image_name):
        a = list(db.users.find({"image.image_path":image_name},{"_id":0,"image.image_path":1,"image.tag":1}))
        # print('\na',a)
        a = str(a)
        a = re.sub('[-=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]',"",a)
        a = a.replace('{','')
        a = a.replace('}','')
        a = a.replace('tag','')
        # print('aa',a,'\n\n')

        a = a.split("image_path")
        b = []

        # print(type(a))
        # del a[0]
        # print('aaa',a,'\n\n')


        for i in range(1,len(a)):
            
            if image_name in a[i]:
                b.append(a[i])
                aa = a[i]
                b = aa.split(' ')
                vv = b.count('')
                for p in range(0,vv):
                    b.remove('')
        del b[0]
        # print('bbb',b,'\n\n')
        b = tuple(b)
        # print('bbb',b,'\n\n')



        return b





















        # print('show 함수',image_)
        # print(type(image_))
        # print('이미지내임',image_)
        # # a = list(db.users.find({"image.image_path":image_name},{"_id":0,"image.image_path":1,"image.tag":1}))
        # a = list(db.users.find({"image.image_path":'2.jpg'},{"_id":0,"image.image_path":1,"image.tag":1}))

        # print('a값',a)

        # # a = list(db.users.find({'image':{'$eleMatch':'1.png'}}})

        # # 값을 못찾고 있어..image_name 을쓰면 안들어가짐... 오ㅔ?
        # print(a)
        # a = str(a)
        # a = re.sub('[-=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]',"",a)
        # a = a.replace('{','')
        # a = a.replace('}','')
        # a = a.replace('tag','')
        #     # print('show 함수 전처리',a)/

        # a = a.split("image_path")
        # print(type(a))
        # b = []

        # for i in range(1,len(a)):
            
        #     if image_ in a[i]:
        #         b.append(a[i])
        #         aa = a[i]
        #         b = aa.split(' ')
        #         vv = b.count('')
        #         for p in range(0,vv):
        #             b.remove('')
        # del b[0]
    # def k(self,im):
    #     for i in im:
    #         a = str(i)
    #         d = list(db.users.find({"image":{'$elemMactch':{'image_path':'1.jpg'}} }))
    #         print("k함수",d)