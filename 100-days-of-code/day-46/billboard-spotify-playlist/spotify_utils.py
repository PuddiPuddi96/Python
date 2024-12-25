import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

class SpotifyUtils():

    def __init__(self, date: str, song_names):
        load_dotenv()
        self.sp = None
        self.__init_spotify_auth()
        self.user_id = self.sp.current_user()["id"]
        self.date = date
        self.song_names = song_names
        
        
    def __init_spotify_auth(self):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri="http://example.com",
                client_id=os.environ['SPOTIFY_CLIENT_ID'],
                client_secret=os.environ['SPOTIFY_CLIENT_SECRET'],
                show_dialog=True,
                cache_path="token.txt",
                username=os.environ['SPOTIFY_USERNAME']
            )
        )

    def __get_song_uris(self):
        song_uris = []
        year = self.date.split("-")[0]
        for song in self.song_names:
            result = self.sp.search(q=f"track:{song} year:{year}", type="track")
            try:
                uri = result["tracks"]["items"][0]["uri"]
                song_uris.append(uri)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")
        return song_uris
    
    def create_playlist(self):
        playlist = self.sp.user_playlist_create(user=self.user_id, name=f"{self.date} Billboard 100", public=False)
        self.sp.playlist_add_items(playlist_id=playlist["id"], items=self.__get_song_uris())
