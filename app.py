from flask import Flask
from flask_cors import CORS
from routes.compare_bp import CompareBlueprint

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

app.register_blueprint(CompareBlueprint.compare_bp)

if __name__ == '__main__':
    app.run()

