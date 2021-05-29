from re import A
import re
from flask import Flask, Blueprint,render_template, jsonify, request
from warnings import showwarning
import os
import requests
from bs4 import BeautifulSoup
from .hash_func import hashTag

import os
from flask.helpers import send_from_directory, url_for
from flask.templating import render_template
from werkzeug.utils import redirect







from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.fake
bp = Blueprint('img_gallery', __name__, url_prefix='/image')


## HTML을 주는 부분



from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle





## HTML을 주는 부분
@app.route('/')
def get_gallery():
   return render_template('image_gal/gallery.html')

@app.route('/memo', methods=['POST'])
def post_articles():
    # 1. 클라이언트로부터 데이터를 받기
    # 2. meta tag를 스크래핑하기
    # 3. mongoDB에 데이터 넣기
    return jsonify({'result': 'success', 'msg': 'POST 연결되었습니다!'})
## API 역할을 하는 부분





@app.route('/memo', methods=['POST'])
def saving():
		# 1. 클라이언트로부터 데이터를 받기
		# 2. meta tag를 스크래핑하기
		# 3. mongoDB에 데이터 넣기
    return jsonify({'result': 'success', 'msg':'POST 연결되었습니다!'})

