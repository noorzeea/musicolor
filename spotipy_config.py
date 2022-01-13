import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from config import Config

spotify_app = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=Config.get("APP_CLIENT_ID"),
        client_secret=Config.get("APP_CLIENT_SECRET")
    )
)

# results = spotify_app.search(q='weezer', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])
