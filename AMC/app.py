# 깃헙 레퍼지토리 정리하기
from scholarly import scholarly
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


# @app.route('/memo', methods=['POST'])
# def post_article():
#     # 1. 클라이언트로부터 데이터를 받기
#     # 2. meta tag를 스크래핑하기
#     # 3. mongoDB에 데이터 넣기
#     return jsonify({'result': 'success', 'msg': 'POST 연결되었습니다!'})
#

# @app.route('/book', methods=['GET'])
# def read_articles():
#     # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기(Read)
#     info = list(scholarly({}, {'_id: False'}))
#     # 2. articles라는 키 값으로 articles 정보 보내주기
#     return jsonify({'result': 'success', 'msg': 'GET 연결되었습니다!'})

@app.route('/book', methods=['GET'])
def test_get():
    title_receive = request.args.get('title_give')
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
