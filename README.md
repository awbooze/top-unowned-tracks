# top-unowned-tracks
A Python script that grabs a user's top tracks from their Spotify account and displays them on the command line. Created to help me decide what music to buy from my Spotify activity. In the future, I may improve this to look at the file system to see which tracks the user already owns.

## Features
* User-selectable time ranges (within the limits of the API)
    * Defaults to medium-term (about six months, as described in [the documentation](https://developer.spotify.com/documentation/web-api/reference/personalization/get-users-top-artists-and-tracks/))
    * Run `python main.py -s` or `--small` for short-term favorites
    * Run `python main.py -l` or `--long` for long-term stalwarts
* Help function: `python main.py -h` or `--help`
## Setup
* Install spotipy: `pip install spotipy --upgrade`
* Create a `config.py` file like `example_config.py` in this directory with your Spotify API information and username
* Run `python main.py`