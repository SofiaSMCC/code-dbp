from flask import Flask
from flask import request

app = Flask(__name__)

topAnilist = [
    {
      "id": 0,
      "titulo": "Gintama: THE FINAL",
      "puntaje": 91,
      "tipo":  "movie",
      "season":  "THE FINAL",
      "generos": ["action", "comedy", "drama", "sci-fi"]
    },
    {
      "id": 1,
      "titulo": "Gintama",
      "puntaje": 90,
      "tipo":  "TV Show",
      "season":  "4",
      "generos": ["action", "comedy", "drama", "sci-fi"]
    },
    {
      "id": 2,
      "titulo": "Fruits Basket: The Final",
      "puntaje": 90,
      "tipo":  "TV Show",
      "season":  "3",
      "generos": ["comedy", "drama", "psychological", "romance"]
    },
    {
      "id": 3,
      "titulo": "Hagane no Renkinjutsushi: FULLMETAL ALCHEMIST",
      "puntaje": 90,
      "tipo":  "TV Show",
      "season":  "1",
      "generos": ["action", "adventure", "drama", "fantasy"]
    }
  ]


#method get
@app.route('/anime', methods = ['GET'])
def get():
    return topAnilist

#method get especific
@app.route('/anime/<int:id>', methods=['GET'])
def get_anime(id):
    for anime in topAnilist:
       if (anime['id'] == id):
          return anime

#method post
@app.route('/anime', methods=['POST'])
def add_anime():
    new_anime = {'id': request.json['id'],
                 'titulo': request.json['titulo'],
                 'puntaje': request.json['puntaje'],
                 'tipo':  request.json['tipo'],
                 'season':  request.json['season'],
                 'generos': request.json['generos']
                 }
    topAnilist.append(new_anime)
    return topAnilist

#method put
@app.route('/anime/<int:id>', methods=['PUT'])
def change_anime(id):
    for anime in topAnilist:
        if(anime["id"] == id):
            anime['id'] = request.json['id']
            anime['titulo'] = request.json['titulo']
            anime['puntaje'] = request.json['puntaje']
            anime['tipo'] =  request.json['tipo']
            anime['season'] =  request.json['season']
            anime['generos'] = request.json['generos']
            return anime

#method patch
#@app.route('/anime/<int:id>', methods=['PATCH'])
#def partial_change_anime(id):
#    for anime in topAnilist:
#        if(anime["id"] == id):
#
#    return topAnilist


#method delete
@app.route('/anime/<int:id>', methods=['DELETE'])
def delete_anime(id):
    for anime in topAnilist:
        if(anime["id"] == id):
            topAnilist.remove(anime)
    return topAnilist


if __name__ == '__main__':
   app.run(debug = True)