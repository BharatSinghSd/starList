# Demo Star List

This is a simple demonstration of get, post, put, delete HTTP methods

## The Data

I have created a basic sample data of 20 stars names in JSON fomrat which i have hosted in mongodb Atlas under free server.

the data.json file in this codebase is just to show what the format of the live data looks like.
but the code uses the data from my atlas server.

To see the actual data, use the GET request after running the code.

## to execute the code

run it on your local system the way it was shown by Mr. Rohan during the live session.

uvicorn main:app

http://127.0.0.1:8000/docs/

change the port number accordingly

use the default swagger ui and test out all the HTTP methods.

# NOTE

If cloning this repo, create your own vEnv. As i have added my environment in .gitignore file (this means it wont be uploaded to the github)
