import os
import argparse
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

def get_spotify_client():
    """Initialize the Spotify client."""
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_tracks_from_spotify_playlist(spotify, playlist_id):
    """Fetches all tracks from a Spotify playlist."""
    try:
        results = spotify.playlist_items(playlist_id)
    except Exception as e:
        print(f"Failed to fetch tracks from playlist: {e}")
        return []

    tracks = [f"{item['track']['artists'][0]['name']} - {item['track']['name']}" for item in results['items']]
    return tracks

def create_m3u8_file(tracks, music_folder, output_file):
    """Creates an m3u8 playlist file from a list of track names."""
    with open(output_file, 'w') as f:
        f.write("#EXTM3U\n")
        for track in tracks:
            for root, dirs, files in os.walk(music_folder):
                for file in files:
                    if track in file:
                        f.write(os.path.join(root, file) + "\n")

def main():
    parser = argparse.ArgumentParser(description="Convert a Spotify playlist to m3u8 format.")
    parser.add_argument("playlist_id", help="The Spotify playlist ID.")
    parser.add_argument("music_folder", help="Path to the folder containing the music files.")
    parser.add_argument("output_dir", help="Directory to save the output m3u8 file.")
    args = parser.parse_args()

    spotify = get_spotify_client()

    tracks = get_tracks_from_spotify_playlist(spotify, args.playlist_id)
    if not tracks:
        return

    # Fetch the playlist name for the output file
    playlist_info = spotify.playlist(args.playlist_id)
    playlist_name = playlist_info['name']
    output_file = os.path.join(args.output_dir, f"{playlist_name}.m3u8")

    print(args.music_folder)

    create_m3u8_file(tracks, args.music_folder, output_file)
    print(f"Playlist has been saved to {output_file}")

if __name__ == "__main__":
    main()
