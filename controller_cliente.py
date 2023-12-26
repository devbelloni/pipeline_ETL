import json
import mysql.connector
from connect import db_config


class controller_cliente():

    def __int__(self):
        host = db_config['host']
        user = db_config['user']
        password = db_config['password']
        database = db_config['database']

    def cliente(self, conta:str):
        # Conecta ao banco de dados
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            # Realiza a consulta
            query = f'SELECT * FROM clientes_ag_2456 WHERE numero_conta = "{conta}"'
            cursor.execute(query)

            # Obtém os resultados
            result = cursor.fetchall()

            # Converte para uma lista de dicionários
            data = []
            for row in result:
                row_dict = {
                'id': row[0],
                    'nome': row[1],
                    'cpf': row[2],
                    'endereco': row[3],
                    'telefone': row[4],
                    'email': row[5],
                    'saldo': float(row[6]),
                    'limite': float(row[7]),
                    'perfil': row[8],
                    'conta': row[9],
                    'numero_cartao': row[10],
                    'data_criacao': str(row[11]),
                    'data_modificacao': str(row[12]),
                }
                data.append(row_dict)

            # Salva os resultados em um arquivo JSON
            with open('cliente.json', 'w') as json_file:
                json.dump(data, json_file, default=str)
            return data

        except mysql.connector.Error as err:
            print(f"Erro: {err}")

        finally:
            # Sempre desconecta do banco de dados, mesmo em caso de erro
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
