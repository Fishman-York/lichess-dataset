import psycopg2
import yaml

def connect_database():
    with open("config.yaml") as config_f:
        config_dict = yaml.safe_load(config_f)
        
    db_connection = psycopg2.connect(
        database=config_dict['database'].get('dbname'),
        user=config_dict['database'].get('user'),
        password=config_dict['database'].get('password'),
        host=config_dict['database'].get('host'),
        port=config_dict['database'].get('port')
    )
    
    return db_connection