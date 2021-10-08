import spotipy
import os
import json
import webbrowser
#import spotipy.til as util
#import json.decoder import JSONDecoderError
from spotipy.oauth2 import SpotifyClientCredentials

#https://open.spotify.com/user/2pc6pedag0kee103hzl4i5h49?si=KIm7Rm3YQIqQR4qReOuC8w
#spotify:user:2pc6pedag0kee103hzl4i5h49
#username =sys.argv[1]
client_id = os.getenv('SPOTIPY_CLIENT_ID')
#client_secret=os.getenv('SPOTIPY_CLIENT_SECRET')
album_url='spotify:artist:5nCi3BB41mBaMH9gfr6Su0'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results=spotify.artist_top_tracks(album_url)
for track in results['tracks'][:10]:
    print('track    : '+track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()