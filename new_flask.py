from flask import render_template, request, make_response, Flask
from pymongo import MongoClient, response
from app import find_id
import gridfs
import imdb

app = Flask(__name__)
#client = MongoClient('localhost', 27017)
client = MongoClient(host='db', port=27017)

db = client.poster_name



@app.route('/posterpath/file', methods=['POST', 'GET'])
def handle_data():
    global projectpath
    projectpath = request.form['projectFilepath']
    (find_id(projectpath))
    ia = imdb.IMDb()
    search = ia.search_movie(projectpath)
    s = search
    open('../info.txt', 'w').write(str(search))
    text = open('../info.txt', 'r')
    idn = text.read()
    id = "tt" + idn[11:18]
    data = db.fs.files.find_one({'name': id})
    my_id = data['_id']
    fs = gridfs.GridFS(db)
    my_poster = fs.get(my_id).read()
    response = make_response(my_poster)
    response.content_type = "image/webp"
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index")
def index1():
    return "hello"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)