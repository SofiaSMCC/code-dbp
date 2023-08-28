from flask import Flask
from flask import request

app = Flask(__name__)

topAnilist = [
    {'id': 0, 'titulo': 'Gintama: THE FINAL', 'puntaje': 91, 'tipo':  'movie', 'season':  'THE FINAL', 'generos': ["action", "comedy", "drama", "sci-fi"]},
    {'id': 1, 'titulo': 'Gintama', 'puntaje': 90, 'tipo':  'TV Show', 'season':  '4', 'generos': ["action", "comedy", "drama", "sci-fi"]},
    {'id': 2, 'titulo': 'Fruits Basket: The Final', 'puntaje': 90, 'tipo':  'TV Show', 'season':  '3', 'generos': ["comedy", "drama", "psychological", "romance"]},
    {'id': 3, 'titulo': 'Hagane no Renkinjutsushi: FULLMETAL ALCHEMIST', 'puntaje': 90, 'tipo':  'TV Show', 'season':  '1', 'generos"': ["action", "adventure", "drama", "fantasy"]}
  ]

#method get
@app.route('/anime', methods = ['GET'])
def getList():
    return topAnilist

#method get especific
@app.route('/anime/<int:id>', methods=['GET'])
def getAnime(id):
    for anime in topAnilist:
       if anime['id'] == id:
          return anime
    return 'Page not found', 404

#method post
@app.route('/anime', methods=['POST'])
def addAnime():
    newAnime = request.get_json()
    for anime in topAnilist:
        if newAnime['id'] == anime['id']:
            return "You can't do this action", 202
    topAnilist.append(newAnime)
    return topAnilist

#method put
@app.route('/anime/<int:id>', methods=['PUT'])
def putAnime(id):
    for anime in topAnilist:
        copy = request.get_json()
        if anime['id'] == id:
          i = 1
          for another in topAnilist:
             if another['id'] == copy['id']:
                i += 1
          if i == 2:
             return "You can't do this action", 202
          else:
             anime = copy
             return anime
#method patch
@app.route('/anime/<int:id>', methods=['PATCH'])
def partialChange(id):
    change = request.get_json()
    for anime in topAnilist:
        if anime["id"] == id:
            anime.update(change)
            return anime
    return "Page not found", 404

#method delete
@app.route('/anime/<int:id>', methods=['DELETE'])
def deleteAnime(id):
    for anime in topAnilist:
        if anime["id"] == id:
            topAnilist.remove(anime)
            return topAnilist
    return "Page not found", 404

if __name__ == '__main__':
   app.run(debug = True)
