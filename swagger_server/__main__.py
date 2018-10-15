#!/usr/bin/env python3

import connexion
from flask import send_from_directory
from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/', static_url_path='/static')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'RandoTrack'})

    @app.route('/')
    def serve_homepage():
        return send_from_directory('../static', 'index.html')


    app.run(port=8080)




if __name__ == '__main__':
    main()
