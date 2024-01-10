from flask import Flask, request, jsonify
from flask_cors import CORS
from app.routes import routes
from app.data_processing import process_file

app = Flask(__name__)
CORS(app, resources={r"/upload": {"origins": "http://localhost:8080"},
                     r"/dados_mrr_churn": {"origins": "http://localhost:8080"}})

app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)
