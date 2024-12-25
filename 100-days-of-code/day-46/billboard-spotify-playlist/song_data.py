from requests import get
from bs4 import BeautifulSoup

BILLBOARD_BASE_URL = "https://www.billboard.com/charts/hot-100"
BILLBOARD_HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}

class SongData():

    def __init__(self, date: str):
        self.date = date

    def get_song_name(self):
        response = get(url=f"{BILLBOARD_BASE_URL}/{self.date}", headers=BILLBOARD_HEADER)
        web_page = response.text
        
        soup = BeautifulSoup(web_page, "html.parser")
        
        song_names_spans = soup.select("li ul li h3")
        return [song.getText().strip() for song in song_names_spans]
