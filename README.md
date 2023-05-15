# SpotifyToM3U8

This script allows you to convert Spotify playlists to .m3u8 format. It assumes that the music files are stored locally on your computer.

## Installation

1. Clone this repository:

    ```sh
    git clone https://github.com/MichelleAppel/SpotifyToM3U8
    ```

2. Enter the directory:

    ```sh
    cd SpotifyToM3U8
    ```

3. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Obtain your Spotify client ID and client secret. You can do this by creating a new app on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and copying the values from there.

2. Create a `.env` file in the root of the project directory, and add your Spotify client ID and client secret as follows:

    ```
    SPOTIFY_CLIENT_ID=<Your Spotify Client ID>
    SPOTIFY_CLIENT_SECRET=<Your Spotify Client Secret>
    ```

3. Run the script:

    ```sh
    python main.py <Spotify playlist URL> <Path to local music folder> <Output directory>
    ```

    For example:

    ```sh
    python main.py "https://open.spotify.com/playlist/7AUYU0uw5U4Y1OhLgztJQV?si=dc9cd9a71f714516" "C:/path/to/your/music/" "./output/"
    ```

## Troubleshooting

If you encounter any issues while using this script, please [open an issue](https://github.com/username/SpotifyToM3U8/issues) on this repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
