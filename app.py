from chalice import Chalice

app = Chalice(app_name='rekognition-chalice')


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/hello/{name}')
def hello_name(name):
    return {'hello': name}
