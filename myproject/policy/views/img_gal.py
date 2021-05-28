from warnings import showwarning
from flask import Blueprint,request,jsonify
import os
from flask.helpers import send_from_directory, url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from .hash_func import hashTag



from os import pipe, replace
from pymongo import MongoClient 
client = MongoClient('localhost', 27017)
db = client.fake

import re


bp = Blueprint('img_gallery', __name__, url_prefix='/image')


# 데이터 어떻게 받을 것인가?

@bp.route('/')
def home():
    
   
    # return send_from_directory('policy/image',filename), 
    return render_template('image_gal/gallery.html')
    


# @bp.route('/gallary', methods=['POST'])
# def post_articles():
#     # 1. 클라이언트로부터 데이터를 받기
#     # 2. meta tag를 스크래핑하기
#     # 3. mongoDB에 데이터 넣기
#     return jsonify({'result': 'success', 'msg': 'POST 연결되었습니다!'})

@bp.route('/gallery', methods=['POST'])
def post_articles():
    # 1. 클라이언트로부터 데이터를 받기
    # 2. meta tag를 스크래핑하기
    # 3. mongoDB에 데이터 넣기
    url_receive = request.form['url_give']
    print(url_receive)
    print(type(url_receive))
    return jsonify({'result': 'success', 'msg': 'POST 연결되었습니다!'})


@bp.route('/gallery', methods=['GET'])
def read_articles():
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기 (Read)
    # result = list(db.articles.find({}, {'_id': 0}))

    # print(url_receive)
    # 검색 값


    image_names = ['2a6e42f0-5b37-4c6d-8cb8-fc15531139d2.jpg','34d9f53a-607f-44e1-8e9f-690489962430.jpg','9b6f94aa-2c40-4ef4-819b-d4a425336874.jpg','ddc24e5c-092d-4d24-90d4-06a3d7054abd.jpg','hair.jpg','KakaoTalk_20200521_021700195.jpg','mynameisjihye.jpg']
    # image_names  모든 이미지 리스트

    image_list = ['9b6f94aa-2c40-4ef4-819b-d4a425336874.jpg','ddc24e5c-092d-4d24-90d4-06a3d7054abd.jpg','hair.jpg']
    # 검색한 해시태그가 있는 이미지명 


    # print(image_list[1])
    result=[]
    # print(len(image_list))

    hash_tag     = []
    images_path = []

    for image_ in image_list:
        if image_ in image_names:
            images_path.append(image_)
            hash_tag.append(hashTag().show_all_hashtag(image_))
    print('hash_tag',hash_tag)
    
    return jsonify({'result': 'success', 'articles': result, 'image_list':image_list,'hash_tag':hash_tag})



# @bp.route('/gallary', methods=('GET'))
# def get_gallery():
#     # print(os.getcwd())
#     args_dict = request.args.get('keyword')

#     print(args_dict)
#     # print(type(args_dict))

#     image_names = os.listdir('policy/image')
#     images_path = []
#     ad = []


#     if args_dict == None:
#         args_dict = os.listdir('policy/image')
#         return render_template('image_gal/gallery.html', image_names = image_names)
#     else:

#         image_list = ['1.jpg','2.jpg']

#         image_='2.jpg'
 



#         for image_ in image_list:
#             if image_ in image_names:
#                 images_path.append(image_)
#                 ad.append(hashTag().show_all_hashtag(image_))
#         print('ad',ad)

    
#     # return print(image_names)
#     return render_template('image_gal/gallery.html', image_names = images_path ,hash_tags =ad)



# C:\Users\hann1\Documents\카카오톡 받은 파일\myproject\policy\image