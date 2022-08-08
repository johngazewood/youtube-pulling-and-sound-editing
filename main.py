import requests
import json

api_key = 'get_from_file'
channel_id = 'UC4fZeoNxAXfbIpT3swsVh9w'
main_endpoint = 'https://www.googleapis.com/youtube/v3'


def resp_to_print(rrr, do_print=True):
    j = rrr.json()
    if do_print:
        j_str = json.dumps(j, indent=4)
        print(j_str)
    return j

def get_playlist_id():
    search_endpoint = f'{main_endpoint}/search'
    playlist_params = {'key': api_key, 
            #'part': 'doanything',
             'type': 'playlist',
             'channelId': channel_id,
             }
    resp = requests.get(search_endpoint, params=playlist_params)
    content = resp_to_print(resp)
    playlist_id = content['items'][0]['id']['playlistId']

#print('-----------------------')
#print(f'playlist id: {playlist_id}')
#videos_params = {
#        'key': api_key,
#        'channelId': channel_id, 
#        }
#playlist_endpoint = f'{main_endpoint}/playlists'
#resp2 = requests.get(playlist_endpoint, params=videos_params)
#content2 = resp2.json()
#content2_str = json.dumps(content2, indent=4)
#print(content2_str)

def get_video_ids_by_channel_id(channel_id: str):
    search_params = {
            'key': api_key,
            'channelId': channel_id,
            'type': 'video',
            'maxResults': 10,
            'order': 'date',
            }
    resp = requests.get(search_endpoint, params=search_params)
    content = resp_to_print(resp)
    for x in range(10):
        next_page_token = content['nextPageToken']
        search_params['pageToken'] = next_page_token
        resp = requests.get(search_endpoint, params=search_params)
        content = resp_to_print(resp, do_print=False)


