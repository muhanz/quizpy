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

    with open('access_token.json', 'w') as outfile:
        json.dump(quizlet.fetch_token(
            token_url, 
            client_secret=quizlet_credentials["client_secret"],
            authorization_response=redirect_response), outfile)
        return "JSON token saved!"



def create_demo_set():
    with open("access_token.json") as data_file:    
        token = json.load(data_file)

    # https://quizlet.com/api/2.0/docs/sets
    # Adding Sets
    url = 'https://api.quizlet.com/2.0'

    # getting the Chinese text
    cn = open('demo-text-cn.txt', 'r')
    cn_lines = cn.readlines()

    # getting the English text
    en = open('demo-text-en.txt', 'r')
    en_lines = en.readlines()

    # #POST /sets - Add a new set
    headers = {'Authorization': 'Bearer ' + token["access_token"]}
    payload = {
        'title':'道德经 - Dao De Jing',
        'terms': cn_lines,
        'definitions': en_lines,
        'lang_terms': 'zh-CN', 
        'lang_definitions': 'en'
    }
    call = requests.post(url+"/sets", headers=headers, json=payload)
    return call