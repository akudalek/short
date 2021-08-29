import logging
import os

logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

show_pagination = int(os.getenv("SHOW_PAGINATION", 5))

port = int(os.getenv("PORT", 8080))
host = os.getenv("HOST", 'localhost')
schema_db = os.getenv("SCHEMA_DB", "cats")
user_db = os.getenv("POSTGRES_USER", "postgres")
password_db = os.getenv("POSTGRES_PASSWORD", "postgres")
host_db = os.getenv("POSTGRES_HOST", "localhost")
port_db = int(os.getenv("POSTGRES_PORT", 5432))
database_db = os.getenv("POSTGRES_DB", "cats")

engine_string = f'postgresql+psycopg2://{user_db}:{password_db}@{host_db}:{port_db}/{database_db}'
