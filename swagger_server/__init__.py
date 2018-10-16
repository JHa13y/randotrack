import connexion, os
from flask import send_from_directory
from flask_cors import CORS
from swagger_server import encoder
map_api_key = os.environ['MAPS_KEY']

app = connexion.App(__name__, specification_dir='./swagger/', )
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'RandoTrack'})
CORS(app.app)

@app.route('/')
def serve_homepage():
    return send_from_directory('static', 'index.html')


#app.run(port=80)