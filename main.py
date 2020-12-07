from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, USERNAME
import spotipy
import spotipy.util as util

SCOPE = 'user-top-read'

def get_top_tracks(spotify, time_range):
    results = spotify.current_user_top_tracks(limit=50, time_range=time_range)
    results_list = sorted(results['items'], key=lambda item: item['popularity'], 
            reverse=True)
    return results_list

def main():
    token = util.prompt_for_user_token(USERNAME, SCOPE, CLIENT_ID, CLIENT_SECRET, 
        REDIRECT_URI)

    if token:
        sp = spotipy.Spotify(auth=token)
        user = sp.me()
        tracks = get_top_tracks(sp, 'medium_term')

        print('\nTop tracks for ' + user['display_name'] + ' for the past six months:\n')

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
    main()