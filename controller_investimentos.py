import json
import mysql.connector


class controller_investimentos:
    def investimentos(self):
        db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': 'ag_2456',
        }

        # Conecta ao banco de dados
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            # Realiza a consulta
            query = 'SELECT * FROM carteira_investimentos WHERE nivel_risco= "Moderado"'
            cursor.execute(query)

            # Obtém os resultados
            result = cursor.fetchall()

            # Converte para uma lista de dicionários
            data = []
            for row in result:
                row_dict = {
                    'id': row[0],
                    'tipo_investimento': row[1],
                    'valor_min': float(row[2]),
                    'retorno_esperado': float(row[3]),
                    'nivel_risco': row[4],
                    'data_criacao': str(row[5]),
                    'data_modificacao': str(row[6]),
                }
                data.append(row_dict)

            # Salva os resultados em um arquivo JSON
            with open('carteira_investimentos.json', 'w') as json_file:
                json.dump(data, json_file, default=str)
            return data

        except mysql.connector.Error as err:
            print(f"Erro: {err}")

        finally:
            # Sempre desconecta do banco de dados, mesmo em caso de erro
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
