# LinkedIn API Python3 Code Examples

This project contain three files:
1. `./linkedin_api_method_1.py`
2. `./linkedin_api_method_2.py`
3. `./proxycurl_people_profile_api_endpoint.py`

## `linkedin_api_method_1.py`

This file uses the official LinkedIn Profile API to fetch profile information of at most ONE user (per access token).
Each user must give explicit information before the application can request information of that user.

This method is available to most developers including free-tier LinkedIn developers.

## `linkedin_api_method_2.py`

This file uses the official LinkedIn Profile API to fetch profile information of **any** profile IDs.

In order to use this method, the developer must
1. have a pre-approved application.
2. Be on a paying subscription to LinkedIn Consumer Product Solution

## `proxycurl_people_profile_api_endpoint.py`

This file uses Proxycurl's LinkedIn API. A third-party alternative to LinkedIn API that is able to fulfill what LinkedIn API provides
without rate limits or approval barriers.