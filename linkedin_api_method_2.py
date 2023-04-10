import requests

LINKEDIN_CLIENT_ID = ''  # todo - fill this field up
LINKEDIN_CLIENT_SECRET = ''  # todo - fill this field up


def get_access_token():
    """
    If you are

    1. an approved LinkedIn developer
    2. on a paid subscription to their Consumer Product

    You can use this function to fetch an `access_token` to access the API.
    """
    LI_ACCESS_TOKEN_EXCHANGE_URL = 'https://www.linkedin.com/oauth/v2/accessToken'
    access_token = requests.post(LI_ACCESS_TOKEN_EXCHANGE_URL, params={
        'grant_type': 'client_credentials',
        'client_id': LINKEDIN_CLIENT_ID,
        'client_secret': LINKEDIN_CLIENT_SECRET,
    }).json()['access_token']
    return access_token


def get_profile(access_token, profile_id):
    """
    Given an `access_token`, fetch structured data of any profile.
    """
    LI_PROFILE_API_ENDPOINT = f'https://api.linkedin.com/v2/people/{profile_id}'
    r = requests.get(LI_PROFILE_API_ENDPOINT, headers={
                     'Authorization': 'Bearer ' + access_token,
                     'X-RestLi-Protocol-Version': '2.0.0'})
    return r.json()
