import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = '519ccb18488c40fb845d672825533b1f'
client_secret = '9a55532fed414bac8a4b4a135daf757e'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret,
                                               redirect_uri='http://localhost:8888/callback',
                                               scope='user-library-read'))

track_id = 'https://open.spotify.com/track/4lCv7b86sLynZbXhfScfm2?si=868ab13a42194e2f'

# Get audio features
audio_features = sp.audio_features([track_id])[0]


# Extract the desired features
def extract_features():
    song_duration = audio_features['duration_ms']
    acousticness = audio_features['acousticness']
    danceability = audio_features['danceability']
    energy = audio_features['energy']
    instrumentalness = audio_features['instrumentalness']
    key = audio_features['key']
    liveness = audio_features['liveness']
    loudness = audio_features['loudness']
    mode = audio_features['mode']  # Mode corresponds to major (1) or minor (0)
    speechiness = audio_features['speechiness']
    tempo = audio_features['tempo']
    time_signature = audio_features['time_signature']
    valence = audio_features['valence']

    # Print the results for testing
    # print(f"Song Duration: {song_duration} ms")
    # print(f"Acousticness: {acousticness}")
    # print(f"Danceability: {danceability}")
    # print(f"Energy: {energy}")
    # print(f"Instrumentalness: {instrumentalness}")
    # print(f"Key: {key}")
    # print(f"Liveness: {liveness}")
    # print(f"Loudness: {loudness}")
    # print(f"Mode (Major: 1, Minor: 0): {mode}")
    # print(f"Speechiness: {speechiness}")
    # print(f"Tempo: {tempo} BPM")
    # print(f"Time Signature: {time_signature}/4")
    # print(f"Valence: {valence}")
    return song_duration, acousticness, danceability, energy, instrumentalness, key, liveness, loudness, mode, speechiness, tempo, time_signature, valence


print(extract_features())
