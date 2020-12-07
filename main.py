from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, USERNAME
import getopt, sys
import spotipy, spotipy.util as util

SCOPE = 'user-top-read'

def get_top_tracks(spotify, term):
    results = spotify.current_user_top_tracks(limit=50, time_range=term)
    results_list = sorted(results['items'], key=lambda item: item['popularity'], 
            reverse=True)
    return results_list

def print_help_and_exit(error):
    print('\nUsage: main.py <term>')
    print("Available <term> values: '--short' or '-s', '--medium' or '-m', " + 
            "'--long' or '-l'. Defaults to medium.")

    if error:
        sys.exit(1)
    else:
        sys.exit(0)

def main(argv):
    # Parse arguments
    try:
        opts, args = getopt.getopt(argv, 'hsml', ['help','short','medium','long'])
    except getopt.GetoptError:
        print_help_and_exit(True)

    # Determine time range. Defaults to medium.
    # Term length described here: https://developer.spotify.com/documentation/web-api/reference/personalization/get-users-top-artists-and-tracks/
    term = 'medium_term'

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print_help_and_exit(False)
        elif opt in ('-s', '--short'):
            term = 'short_term'
        elif opt in ('-l', '--long'):
            term = 'long_term'
        elif opt not in ('-m', '--medium'):
            print_help_and_exit(False)

    # Get Spotify token
    token = util.prompt_for_user_token(USERNAME, SCOPE, CLIENT_ID, CLIENT_SECRET, 
        REDIRECT_URI)

    if token:
        # Create objects
        sp = spotipy.Spotify(auth=token)
        user = sp.me()
        tracks = get_top_tracks(sp, term)

        # Print results
        header = '\nTop tracks for ' + user['display_name'] + ' during the past '
        if term == 'short_term':
            header += 'four weeks'
        elif term == 'medium_term':
            header += 'six months'
        elif term == 'long_term':
            header += 'several years'
        header += ':\n'
        print(header)

        for item in tracks:
            artist_string = ''
            first = True
            for artist in item['artists']:
                if first:
                    first = False
                    artist_string = artist['name']
                else:
                    artist_string = ', '.join([artist_string, artist['name']])
            
            print(item['name'] + ' - ' + artist_string + ' - ' 
                + str(item['popularity']))
    else:
        print("Can't get token for", USERNAME)

if __name__ == '__main__':
    main(sys.argv[1:])