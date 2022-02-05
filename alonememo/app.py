from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  

app = Flask(__name__)
client = MongoClient('localhost', 27017)  
db = client.dbsparta  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/memo', methods=['POST'])
def post_article():
    url_receive = request.form['url_give']  
    comment_receive = request.form['comment_give']  
    article = {'url': url_receive, 'comment': comment_receive}
    db.articles.insert_one(article)
    return jsonify({'result': 'success'})

@app.route('/memo', methods=['GET'])
def read_articles():
    result = list(db.articles.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'articles': result})

@app.route('/api/update', methods=['POST'])
def get_memo():
    name_receive = request.form['name_give']
    memo = db.articles.find_one({'url': name_receive})
    origin_title = memo['url']
    origin_content = memo['comment']
    return jsonify({'result': 'success', 'origin_title': origin_title, 'origin_content': origin_content})

@app.route('/api/like', methods=['POST'])
def save_memo():
    recieve_title = request.form['new_title']
    recieve_content = request.form['new_content']
    recieve_origin = request.form['origin']
    db.articles.update_one({'url':  recieve_origin}, {'$set': {'url':recieve_title, 'comment':recieve_content}})
    return jsonify({'result': 'success'})

@app.route('/api/delete', methods=['POST'])
def delete_memo():
    name_receive = request.form['name_give']
    db.articles.delete_one({'url': name_receive})
    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)