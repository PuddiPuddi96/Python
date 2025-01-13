from requests import get

MOVIES_URL = 'https://api.themoviedb.org/3/search/movie'
MOVIE_URL = "https://api.themoviedb.org/3/movie/movie_id"
MOVIE_DB_API_KEY = ''

params = {
    "include_adult": "false",
    "language": "en-US",
    "api_key": MOVIE_DB_API_KEY
}
params_for_movie = {
    "language": "en-US",
    "api_key": MOVIE_DB_API_KEY
}
headers = {"accept": "application/json"}

class MovieUtils():

    def __init__(self):
        pass

    def get_movies(self, title:str):
        params['query'] = title
        response = get(MOVIES_URL, params=params, headers=headers)
        return response.json()["results"]
    
    def get_movie_info_by_id(self, movie_id):
        response = get(f"{MOVIE_URL}/{movie_id}", params=params_for_movie, headers=headers)
        return response.json()
