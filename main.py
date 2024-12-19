from fastapi import FastAPI
app=FastAPI()

@app.get('/')
def home():
    return {'data':{'name':'dev'}}

@app.get('/about')
def about():
    return 'About Dev!!!'