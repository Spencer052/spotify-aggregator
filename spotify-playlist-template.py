import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random

# Spotify API credentials (replace with your own credentials)
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
REDIRECT_URI = 'http://localhost:8888/callback/'

# Authentication
scope = "playlist-modify-public playlist-modify-private playlist-read-private"

# Set up Spotipy's Spotify object with OAuth2
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    redirect_uri = REDIRECT_URI,
    scope = scope
))

# Playlist IDs (Replace with your own playlist IDs)
source_playlist_ids = [
    'source_playlist_id1',
    'source_playlist_id1',
    'source_playlist_id1'
    
] #add as many playlist IDs as you need
destination_playlist_id = 'your_destination_playlist'

# Get all tracks from a playlist
def get_all_tracks(playlist_id):
    tracks = []
    results = sp.playlist_items(playlist_id)
    tracks.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

# Fetch tracksfrom all source playlists and store unique track URIs
unique_track_uris = set() # Using a set to automatically handle duplicate songs

for playlist_id in source_playlist_ids:
    source_tracks = get_all_tracks(playlist_id)
    for track in source_tracks:
        unique_track_uris.add(track['track']['uri'])
        
        
# Convert the set back to a list and shuffle it
track_uris_list = list(unique_track_uris)
random.shuffle(track_uris_list)

# Split the URIs into batches of 100 (Spotify allows max 100 songs at a time)
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
        
# Add songs to the destination playlist in batches of 100
for batch in chunks(track_uris_list, 100):
    sp.playlist_add_items(destination_playlist_id, batch)
    

print("Unique songs from all playlists have been added to the destionation playlist in random order.")