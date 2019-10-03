import psycopg2
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def connect():
    try:
        connection = psycopg2.connect(
            user=os.environ.get('DB_USER', 'postgres'),
            password=os.environ.get('DB_PASSWORD', 'postgres'),
            host=os.environ.get('DB_ADDR', 'db'),
            port=os.environ.get('DB_PORT', '5432'),
            database=os.environ.get('DB_NAME', 'postgres')
        )
        print("Conexação com base da dados estabelecida!")
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Erro ao tentar conectar com a base de dados: ", error)
