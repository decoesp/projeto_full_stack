from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from app.data_processing import process_file

routes = Blueprint('routes', __name__)

uploaded_data = None

@routes.route('/upload', methods=['POST'])
def upload_file():
    global uploaded_data
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    try:
        # Processamento da planilha e cálculo de métricas
        uploaded_data = process_file(file)
        return jsonify({'success': 'File processed successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

@routes.route('/dados_mrr_churn', methods=['GET'])  # Rota para os dados MRR e Churn Rate
@cross_origin()  # Aplique cross_origin à rota
def get_dados_mrr_churn():
    global uploaded_data
    
    if uploaded_data:
        return jsonify(uploaded_data)
    else:
        return jsonify({'message': 'Os dados precisam ser carregados via upload antes de acessar esta rota.'})
