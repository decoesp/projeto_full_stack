import pandas as pd

def process_file(file_path):
    # Carregar os dados do arquivo CSV
    if file_path.filename.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    elif file_path.filename.endswith('.csv'):
        # Tente ler o arquivo CSV usando diferentes codificações
        encodings = ['utf-8', 'latin1']  # Adicione outras codificações se necessário
        df = None
        for encoding in encodings:
            try:
                break  # Se a leitura for bem-sucedida, pare o loop
            except UnicodeDecodeError:
                pass  # Se a codificação não funcionar, tente a próxima
        if df is None:
            raise ValueError('Não foi possível ler o arquivo CSV')

    else:
        raise ValueError('Formato de arquivo inválido')
    
    # Filtrar os dados para ativos e cancelados
    ativos = df[df['status'] == 'Ativa']
    cancelados = df[df['status'] == 'Cancelada']

    # Calcular MRR para ativos
    mrr_data_ativos = {}
    total_ativos = 0  # Contador total de clientes ativos

    for _, row in ativos.iterrows():
        date = str(row['data início'])[:7]
        if date not in mrr_data_ativos:
            mrr_data_ativos[date] = {'total_mrr': 0, 'total_clientes': 0, 'ativos': 0, 'cancelados': 0}

        mrr_data_ativos[date]['total_mrr'] += row['quantidade cobranças'] * row['valor']
        mrr_data_ativos[date]['total_clientes'] += 1  # Adicionar um cliente
        mrr_data_ativos[date]['ativos'] += 1  # Adicionar um cliente ativo
        total_ativos += 1  # Adicionar um cliente

    for month, values in mrr_data_ativos.items():
        mrr_data_ativos[month]['MRR'] = values['total_mrr'] / values['total_clientes'] if values['total_clientes'] != 0 else 0
        mrr_data_ativos[month]['total_clientes'] = total_ativos  # Definir o total de clientes

    print("MRR Data Ativos:")
    print(mrr_data_ativos)

    # Calcular churn rate para cancelados
    churn_data_cancelados = {}
    total_cancelados = 0  # Contador total de clientes cancelados

    for _, row in cancelados.iterrows():
        date = str(row['data cancelamento'])[:7]
        if date not in churn_data_cancelados:
            churn_data_cancelados[date] = {'cancelamentos': 0, 'total_clientes': 0, 'ativos': 0, 'cancelados': 0}

        churn_data_cancelados[date]['cancelamentos'] += row['quantidade cobranças']
        churn_data_cancelados[date]['total_clientes'] += 1  # Adicionar um cliente
        churn_data_cancelados[date]['cancelados'] += 1  # Adicionar um cliente cancelado
        total_cancelados += 1  # Adicionar um cliente cancelado

    for month, values in churn_data_cancelados.items():
        churn_data_cancelados[month]['churn_rate'] = (values['cancelamentos'] / total_ativos) * 100 if total_ativos != 0 else 0
        churn_data_cancelados[month]['total_clientes'] = total_ativos  # Definir o total de clientes
        churn_data_cancelados[month]['ativos'] = total_ativos - total_cancelados  # Definir o número de clientes ativos

    print("\nChurn Data Cancelados:")
    print(churn_data_cancelados)

    data_for_frontend = {
        'MRR': mrr_data_ativos,
        'ChurnRate': churn_data_cancelados
    }

    return data_for_frontend
