# quizpy
Python3 wrapper for the Quizlet API

# getting started
1. Get your developer credentials from https://quizlet.com/api-dashboard
2. Copy the credentials and save it into json file named *quizlet-credentials.json* like so:
     `{
         "client_id": "XXXXXXXXXX",
         "client_secret": "XXXXXXXXXXXXXXXXXXXXXX",
         "redirect_uri": "http://www.muhanzhang.com"
     }`
3. Fire up the terminal, run Python3 console mode
4. "from quizpy import *"
5. Call the "authenticate_quizlet()" function; this should pop up the authorization page.
6. Click "approve", then copy and paste the redirect into the console
7. If success, you should now have a new JSON file named "access_token.json" that will be valid for 10 years (!) 
8. To see the proof in the pudding, call "create_demo_set()". If the code return is "201", navigate to your Quizlet "sets" page.
9. Profit!
