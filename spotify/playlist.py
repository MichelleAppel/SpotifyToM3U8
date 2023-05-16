from .client import get_spotify_client
from utils.text_processing import normalize_text

def get_tracks_from_spotify_playlist(playlist_id):
    """Fetches all tracks from a Spotify playlist."""
    spotify = get_spotify_client()
    
    try:
        results = spotify.playlist_items(playlist_id)
    except Exception as e:
        print(f"Failed to fetch tracks from playlist: {e}")
        return []

    tracks = [
        {
            "normalized_title": normalize_text(item['track']['name']),
            "title": item['track']['name'],
            "normalized_artist_title": normalize_text(f"{item['track']['artists'][0]['name']} - {item['track']['name']}"), 
            "artist_title": f"{item['track']['artists'][0]['name']} - {item['track']['name']}",
            "normalized_artist": normalize_text(item['track']['artists'][0]['name']),
            "artist": item['track']['artists'][0]['name']
        } 
        for item in results['items']
    ]
    
    return tracks
