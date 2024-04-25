import requests

# TODO: Make requesting url region specific

def handle_http_response(response):
    """Handle common HTTP errors based on response status codes."""
    if response.status_code == 200:
        return response.json() 
    error_messages = {
        400: "Bad request - Check your parameters.",
        401: "Unauthorized - Check your API key.",
        403: "Forbidden - You might not have the necessary permissions for this resource.",
        404: "Data not found - No matching data found.",
        405: "Method not allowed - HTTP method used is not valid for this endpoint.",
        415: "Unsupported media type - The content type of the request is incorrect.",
        429: "Rate limit exceeded - You have made too many requests.",
        500: "Internal server error - Problem with the server.",
        502: "Bad gateway - Issue between servers.",
        503: "Service unavailable - The server is down or undergoing maintenance.",
        504: "Gateway timeout - Request to the server timed out."
    }
    raise Exception(error_messages.get(response.status_code, f"Unexpected error: {response.status_code} - {response.text}"))


def get_puuid(api_key, game_name, tagline):
    url = f"https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tagline}"
    headers = {'X-Riot-Token': api_key}
    response = requests.get(url, headers=headers)
    return handle_http_response(response).get('puuid')

# Recent 1 match ids
def get_recent_match_ids(api_key, puuid):
    url = f"https://sea.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=10"
    headers = {'X-Riot-Token': api_key}
    response = requests.get(url, headers=headers)
    return handle_http_response(response)[:1] 

def get_match_detail(api_key, match_id):
    url = f"https://sea.api.riotgames.com/lol/match/v5/matches/{match_id}"
    headers = {'X-Riot-Token': api_key}
    response = requests.get(url, headers=headers)
    return handle_http_response(response)


def fetch_match_history(api_key, game_name, tagline):
    puuid = get_puuid(api_key, game_name, tagline)
    match_ids = get_recent_match_ids(api_key, puuid)
    match_details = []
    for match_id in match_ids:
        match_details.append(get_match_detail(api_key, match_id))
    return match_details