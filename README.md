# top-unowned-tracks
A short little Python script that grabs a user's top tracks from their Spotify account and displays them on the command line. Created to help me decide what music to buy from my Spotify activity. In the future, I may make the time period customizable and look at the file system to see which tracks the user already owns.

## Setup
* Install spotipy: `pip install spotipy --upgrade`
* Create a `config.py` file like `example_config.py` in this directory with your Spotify API information and username
* Run `python main.py`