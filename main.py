import requests

def get_access_token(client_id, client_secret):
    # Send a POST request to the Spotify Accounts service to get the access token
    auth_url = "https://accounts.spotify.com/api/token"
    response = requests.post(
        auth_url,
        data={
            "grant_type": "client_credentials"
        },
        auth=(client_id, client_secret)
    )
    response_json = response.json()
    access_token = response_json.get("access_token")
    return access_token

def get_playlist_tracks(playlist_id, access_token):
    # Send a GET request to the Spotify API to get the tracks of a playlist
    playlist_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(playlist_url, headers=headers)
    response_json = response.json()
    tracks = response_json.get("items", [])

    return tracks

def scrape_music_names(playlist_id, client_id, client_secret):
    access_token = get_access_token(client_id, client_secret)
    tracks = get_playlist_tracks(playlist_id, access_token)

    for track in tracks:
        track_name = track["track"]["name"]
        print(track_name)

# Set your Spotify playlist ID, client ID, and client secret here
playlist_id = "your_playlist_id"
client_id = "your_client_id"
client_secret = "your_client_secret"

scrape_music_names(playlist_id, client_id, client_secret)
