from flask import Flask, request
from sqlalchemy import create_engine
from datetime import datetime
import json



app = Flask(__name__)

def get_db_connection():
    server_ip   = "172.105.26.77"
    server_port = "3306"
    username    = "root"
    password    = "bkdufhsifh83724892349"
    database_name = 'elemental_analytics'
    
    return create_engine("mysql+pymysql://"+username+":"+password+"@"+server_ip+":"+server_port+"/"+database_name, pool_pre_ping=True, pool_recycle=10)

def insert_api_data(data, source='sh'):
    ts = int(datetime.now().timestamp())
    engine = get_db_connection()
    with engine.connect() as con:
        r = con.execute(
            """
            INSERT INTO api_data 
            (data, timestamp, source) 
            VALUES (%s, %s, %s) 
            """,
            (data, ts, source)
        )

@app.route('/api/simple_hash_bsiugwiuevfishlg', methods=['POST'])
def simple_hash_endpoint():
    data = request.json
    print('simple hash metadata', data)
    insert_api_data(json.dumps(data))
    return {'ok': True}



if __name__ == "__main__":
    app.run()