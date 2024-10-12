# Spotify Playlist Manager

A Python script that combines songs from multiple Spotify playlists into a single playlist and removes any duplicates. The script also supports randomizing the order of tracks in the new playlist.

## Features
- Combine songs from multiple Spotify playlists into one.
- Automatically remove duplicate tracks.
- Randomize the order of tracks in the final playlist.
- Utilizes Spotify's API through Spotipy for playlist management.

## Prerequisites

Before using this program, make sure you have the following:
- Python 3.6 or higher
- A Spotify account
- Spotify Developer credentials (Client ID, Client Secret, Redirect URI)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/spotify-playlist-manager.git
   cd spotify-playlist-manager

2. Install the required Python packages:
   ```bash
   pip install spotipy
   ```

3. Set up your Spotify Developer account:
   - Go to [Spotify for Developers](https://developer.spotify.com/dashboard/applications).
   - Log in with your Spotify account.
   - Click on **Create an App** and fill in the required details.
   - After creating the app, you'll get a **Client ID** and **Client Secret**.
   - Set the **Redirect URI** in the Spotify Developer Dashboard to: `http://localhost:8888/callback/`.


4. Set up environment variables for your Spotify credentials (replace the placeholders with your actual values):

   On **Linux/macOS**:
   ```bash
   export SPOTIPY_CLIENT_ID='your_spotify_client_id'
   export SPOTIPY_CLIENT_SECRET='your_spotify_client_secret'
   export SPOTIPY_REDIRECT_URI='http://localhost:8888/callback/'
   ```

   On **Windows**;
   ```bash
   set CLIENT_ID = your_spotify_client_id
   set CLIENT_SECRET = your_spotify_client_secret
   set REDIRECT_URI = http://localhost:8888/callback/
   ```

## Usage
1. Open the script and update the playlist_ids:
  - Locate the playlist_ids variable in the script.
  - Replace the placeholder IDs with your own Spotify playlist IDs
  - example:
    ```bash
    playlist_ids = ["somestringoflettersandnumbers", "anotherstringofletters"]
    ```
2.  Run the script:
    ```bash
    python spotify-playlist-py
    ```
3. Upon running, the script will:
  - Authenticate your spotify account (you'll need to log in through a browser if running for the first time).
  - Retrieve all tracks from the specified playlists.
  - Combine them into one playlist, remove duplicates, and shuffle the track list.

4. The final playlist will be created in your Spotify account.
     
