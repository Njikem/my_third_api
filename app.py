from flask import Flask, request
app = Flask(__name__)
import dbhelpers
import json

#philosopher get request

@app.get('/api/philosopher')
def get_philosopher():
    id = request.args.get("id")
    name = request.args.get("name")
    bio = request.args.get("bio")
    date_of_birth = request.args.get("date_of_birth")
    date_of_death = request.args.get("date_of_death")
    image_url = request.args.get("image_url")
    results = dbhelpers.run_procedure('call get_philosopher(?,?,?,?,?)', [id, name, bio, date_of_birth, date_of_death, image_url])
    if(type(results) == list):
        return json.dumps(results, default=str)
    else:
        return "sorry, something has gone wrong"
    

#philosopher post request
@app.post('/api/philosopher')
def post_philosopher():
    name = request.json.get("name")
    bio = request.json.get("bio")
    date_of_birth = request.json.get("date_of_birth")
    date_of_death = request.json.get("date_of_death")
    image_url = request.json.get("image_url")
    results = dbhelpers.run_procedure('call get_philosopher(?,?,?,?,?)', [name, bio, date_of_birth, date_of_death, image_url])
    if(type(results) == list):
        return json.dumps(results, default=str)
    else:
        return "sorry, something has gone wrong"

    
    
    
    
    #quote get request
@app.get('/quote')
def get_quote():
    content = request.json.get("content")
    id = request.json.get("id")
    name = request.json.get("name")
    results = dbhelpers.run_procedure('call quote(?,?,?)', [content, id, name])
    if(type(results) == list):
        return json.dumps(results, default=str)
    else:
        return "sorry something has gone wrong"
    

#quote post request
@app.post('/api/quote')
def post_quote():
    philosopher_id = request.json.get("philosopher_id")
    content = request.json.get("content")
    results = dbhelpers.run_procedure('call get_two_quote(?,?)', [philosopher_id, content,])
    if(type(results) == list):
        return json.dumps(results, default=str)
    else:
        return "sorry, something has gone wrong"