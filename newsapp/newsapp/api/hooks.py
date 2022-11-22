from newsdataapi import NewsDataApiClient

# API key authorization, Initialize the client with your API key

# API KEY REVOKED, GET YOURS FROM:
# https://newsdata.io/api-key
api = NewsDataApiClient(apikey="pub_7077e9879739b77c8226dd9f41c58fddafa0")
data = {"q": "", "language": "en"}

def get_latest():
    response = api.news_api(language="en")
    return response
