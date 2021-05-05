import requests,json


def get_api():
    apikey = "58beb94f"
    ids = ['tt0944835', 'tt0848228', 'tt3076658', 'tt1502397', 'tt6450804', 'tt0120802', 'tt0328107', 'tt0118799',
           'tt0069197', 'tt7975244', 'tt1067224', 'tt7286456', 'tt2024469', 'tt1895587']
    movies = []
    for id in ids:
        response = requests.get("http://www.omdbapi.com/?apikey=" + apikey + "&i=" + id + "")
        response = json.loads(response.text)
        info = {
            'title': response['Title'],
            'year': response['Year'],
            'image': response['Poster'],
            'id': response['imdbID'],
        }
        movies.append(info)
    return movies