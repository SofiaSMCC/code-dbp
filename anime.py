from flask import Flask
from flask import request

app = Flask(__name__)

topAnilist = [
    {"id": 0, "titulo": "Gintama: THE FINAL", "puntaje": 91, "tipo":  "movie", "season":  "THE FINAL", "generos": ["action", "comedy", "drama", "sci-fi"]},
    {"id": 1, "titulo": "Gintama", "puntaje": 90, "tipo":  "TV Show", "season":  "4", "generos": ["action", "comedy", "drama", "sci-fi"]},
    {"id": 2, "titulo": "Fruits Basket: The Final", "puntaje": 90, "tipo":  "TV Show", "season":  "3", "generos": ["comedy", "drama", "psychological", "romance"]},
    {"id": 3, "titulo": "Hagane no Renkinjutsushi: FULLMETAL ALCHEMIST", "puntaje": 90, "tipo":  "TV Show", "season":  "1", "generos": ["action", "adventure", "drama", "fantasy"]}
  ]

#method get
@app.route('/anime', methods = ['GET'])
def getList():
    return topAnilist

#method get especific
@app.route('/anime/<int:id>', methods=['GET'])
def getAnime(id):
    for anime in topAnilist:
       if (anime['id'] == id):
          return anime
       else:
          return "404. Anime no encontrado."

#method post
@app.route('/anime', methods=['POST'])
def addAnime():
    new_anime = {'id': request.json.get('id'),
                 'titulo': request.json.get('titulo'),
                 'puntaje': request.json.get('puntaje'),
                 'tipo': request.json.get('tipo'),
                 'season': request.json.get('season'),
                 'generos': request.json.get('generos')
                 }
    for anime in topAnilist:
        if(new_anime['id']==anime['id']):
            return '400.'
            break
    topAnilist.append(new_anime)
    return new_anime

#method put
@app.route('/anime/<int:id>', methods=['PUT'])
def changeAnime(id):
    for anime in topAnilist:
        if(anime['id'] == id):
            anime['id'] = request.json.get('id')
            anime['titulo'] = request.json.get('titulo')
            anime['puntaje'] = request.json.get('puntaje')
            anime['tipo'] =  request.json.get('tipo')
            anime['season'] =  request.json.get('season')
            anime['generos'] = request.json.get('generos')
            return anime
    return "202"

#method patch
@app.route('/anime/<int:id>', methods=['PATCH'])
def partialChange(id):
    change = request.get_json()
    for anime in topAnilist:
        if(anime["id"] == id):
            anime.update(change)
            return anime
    return "404. No existe el anime."

#method delete
@app.route('/anime/<int:id>', methods=['DELETE'])
def deleteAnime(id):
    for anime in topAnilist:
        if(anime["id"] == id):
            topAnilist.remove(anime)
            return topAnilist
    return "404. No existe el anime."

if __name__ == '__main__':
   app.run(debug = True)