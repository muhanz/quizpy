# Muhan Zhang
# quizpy - Python3 wrapper for Quizlet API
# Hecho Con Amor en Miami, FL

import webbrowser, base64, requests, re, json

with open("quizlet-credentials.json") as data_file:    
    # from: https://quizlet.com/api-dashboard
    # make sure to have a json file with like so:
    # {
    #     "client_id": "XXXXXXXXXX",
    #     "client_secret": "XXXXXXXXXXXXXXXXXXXXXX",
    #     "redirect_uri": "http://www.muhanzhang.com"
    # }
    quizlet_credentials = json.load(data_file)

def authenticate_quizlet():
    # authenticate_quizlet - https://quizlet.com/api/2.0/docs/authorization-code-flow
    authorization_base_url = 'https://quizlet.com/authorize'
    token_url = 'https://api.quizlet.com/oauth/token'
    
    from requests_oauthlib import OAuth2Session
    quizlet = OAuth2Session(
        quizlet_credentials["client_id"], 
        scope='read write_set', 
        redirect_uri=quizlet_credentials["redirect_uri"])

    # Redirect user to Quizlet for authorization
    authorization_url, state = quizlet.authorization_url(authorization_base_url,
        access_type="offline", approval_prompt="force")
    # print ('Please go here and authorize,', authorization_url)
    webbrowser.open(authorization_url)

    # Get the authorization verifier code from the callback url
    redirect_response = input('Paste the full redirect URL here: ')
    generated_code = re.search("(code=)(.+)", redirect_response).group(2)

    return quizlet.fetch_token(
            token_url, 
            client_secret=quizlet_credentials["client_secret"],
            authorization_response=redirect_response)

