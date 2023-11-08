#!/usr/bin/python3
# Defines a function to query Reddit API to info of a subreddit.

import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts
       listed for a given subreddit.

       Returns:
           The total number of subscribers of a given subreddit,
           or 0 if the subreddit is invalid."""

    if type(subreddit) is not str:
        print(None)

    client_id = '-NIUk5MRHKUDkmiAqS36cw'
    private_key = '-jHp4khHG_S0zCWrREukb7Ybr7cJHQ'

    # request temp oauth token from reddit
    auth = requests.auth.HTTPBasicAuth(client_id, private_key)
    data = {
            'grant_type': 'password',
            'username': 'Individual_Bee1317',
            'password': 'aF4rBXx^iCc>#5b'
           }
    headers = {'User-Agent': 'redAPI/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)
    token = res.json()['access_token']
    headers['Authorization'] = 'bearer {}'.format(token)

    # using oauth token to access reddit api endpoints
    res = requests.get('https://oauth.reddit.com/r/{}/hot'.format(subreddit),
                       headers=headers)
    if res.status_code == 200:
        count = 0
        posts = res.json()['data']['children']

        for post in posts:
            print(post['data']['title'])
            count += 1
            if count == 10:
                break
    else:
        print(None)
