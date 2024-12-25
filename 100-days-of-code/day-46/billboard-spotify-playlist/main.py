from song_data import SongData
from spotify_utils import SpotifyUtils

def check_format_date():
    return True

date_ok = False
date = None
while not date_ok:
    date = str(input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: "))
    if(check_format_date()):
        date_ok = True

songData = SongData(date)
song_names = songData.get_song_name()

spotifyUtils = SpotifyUtils(date=date, song_names=song_names)
spotifyUtils.create_playlist()

