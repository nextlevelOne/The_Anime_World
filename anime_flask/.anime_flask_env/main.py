from flask import Flask, jsonify
from anime import Anime
"""
port:
1.return json data
2.structure
{
    resCode: 0 or 1(error) 
    data: data address(list)
    message: 'comment for this request '
}


"""
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/', methos * ['GET', 'POST'])  # routing path
def hello_world():
    anime = Anime()
    arrdata = anime.get_anime_infos_limit()
    print('arrData = ', arrdata)
    return jsonify((arrdata))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=1996, debug=True)
