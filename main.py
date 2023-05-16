import os
import argparse
from spotify.client import get_spotify_client
from spotify.playlist import get_tracks_from_spotify_playlist
from utils.text_processing import normalize_text

def create_m3u8_file(tracks, music_folder, output_file):
    """Creates an m3u8 playlist file from a list of track names.
    
    Args:
        tracks (list): A list of track dictionaries.
        music_folder (str): Path to the folder containing the music files.
        output_file (str): Path to the output m3u8 file.
        
    Returns:
        None
    """
    missing_tracks = []
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("#EXTM3U\n")
        for track in tracks:
            track_found = False
            for root, dirs, files in os.walk(music_folder):
                for file in files:
                    normalized_file = normalize_text(file)
                    if track['normalized_artist'] in normalized_file and track['normalized_title'] in normalized_file:
                        f.write(os.path.join(root, file) + "\n")
                        track_found = True
                        break
            if not track_found:
                missing_tracks.append(track['artist_title'])
    
    if missing_tracks:
        print("The following tracks were not found in your music library and have not been added to the playlist:")
        for track in missing_tracks:
            print(f"- {track}")

def main():
    parser = argparse.ArgumentParser(description="Convert a Spotify playlist to m3u8 format.")
    parser.add_argument("playlist_id", help="The Spotify playlist ID.")
    parser.add_argument("music_folder", help="Path to the folder containing the music files.")
    parser.add_argument("output_dir", help="Directory to save the output m3u8 file.")
    args = parser.parse_args()

    spotify = get_spotify_client()

    tracks = get_tracks_from_spotify_playlist(args.playlist_id)
    if not tracks:
        return

    playlist_info = spotify.playlist(args.playlist_id)
    playlist_name = playlist_info['name']
    output_file = os.path.join(args.output_dir, f"{playlist_name}.m3u8")

    print(args.music_folder)

    create_m3u8_file(tracks, args.music_folder, output_file)
    print(f"Playlist has been saved to {output_file}")

if __name__ == "__main__":
    main()
