from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def index():
    return {'data': { 'name': 'Kalarana'}}


@app.get('/about')
def index():
    return {'data': 'About Kalarana'}