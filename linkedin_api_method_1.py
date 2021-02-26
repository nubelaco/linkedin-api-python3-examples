import requests
import secrets

LINKEDIN_CLIENT_ID = ''  # todo - fill this field up
LINKEDIN_CLIENT_SECRET = ''  # todo - fill this field up
LINKEDIN_REDIRECT_URI = ''  # todo - fill this field up


def generate_authorization_url():
    """
    Generate an authorization URL for a user to give permission to extract his/her Linkedin Profile.

    The genereated URL will take the user to a Linkedin page for which the user will be asked to give an explicit
    permission to share his profile with you (the application creator).

    Should the user agree, he/she will be redirected to `LINKEDIN_REDIRECT_URI`.
    In the redirect, two fields will appear in the URL parameter, namely `code` and `state`.

    * `state` is generated below using `secrets.token_hex(8).upper()`. This is as a form of identifier for this user.
    * `code` is the authorization_code, and can be used in `get_access_token()` to exchange for an `access_token`.

    """
    LI_AUTH_URL = 'https://www.linkedin.com/oauth/v2/authorization'
    url = requests.Request('GET', LI_AUTH_URL,
                           params={
                               'response_type': 'code',
                               'client_id': LINKEDIN_CLIENT_ID,
                               'redirect_uri': LINKEDIN_REDIRECT_URI,
                               'state': secrets.token_hex(8).upper(),
                               'scope': '%20'.join(['r_liteprofile', 'r_emailaddress', 'w_member_social']),
                           }).prepare().url
    return url


def get_access_token(authorization_code):
    """
    Given a authorization `code`, this function will return you `access_token` which can then be used to access a user's Linkedin profile.
    """
    LI_ACCESS_TOKEN_EXCHANGE_URL = 'https://www.linkedin.com/oauth/v2/accessToken'
    access_token = requests.post(LI_ACCESS_TOKEN_EXCHANGE_URL, params={
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': LINKEDIN_REDIRECT_URI,
        'client_id': LINKEDIN_CLIENT_ID,
        'client_secret': LINKEDIN_CLIENT_SECRET,
    }).json()['access_token']
    return access_token


def get_profile(access_token):
    """
    Fetches the profile of a Linkedin user who has given you his permission to view his profile
    """
    LI_PROFILE_API_ENDPOINT = 'https://api.linkedin.com/v2/me'
    r = requests.get(LI_PROFILE_API_ENDPOINT, headers={
                     'Authorization': 'Bearer ' + access_token})
    return r.json()
