from sqlalchemy import create_engine
from datetime import datetime



def get_db_connection():
    server_ip   = "172.105.26.77"
    server_port = "3306"
    username    = "root"
    password    = "bkdufhsifh83724892349"
    database_name = 'elemental_analytics'
    
    return create_engine("mysql+pymysql://"+username+":"+password+"@"+server_ip+":"+server_port+"/"+database_name, pool_pre_ping=True, pool_recycle=10)

def create_or_get_nft_collection(contract, name, count=None, slug=''):
    if len(contract) > 42: contract = contract[:42]
    if len(contract) < 42:
        return None
    engine = get_db_connection()
    with engine.connect() as con:
        r = con.execute(
            "SELECT * FROM nft_collections WHERE contract_address = %s",
            (contract,)
        )
        coll = r.fetchone()
        if coll:
            return coll[0]
        r = con.execute(
            """
            INSERT INTO nft_collections 
            (collection_name, contract_address, token_count, slug) 
            VALUES (%s, %s, %s, %s)
            """,
            (name, contract, count, slug)
        )
        return r.lastrowid

# CREATE TABLE nft_metadata (
#     id INT AUTO_INCREMENT,
#     collection_id INT,
#     contract_address VARCHAR(42),
#     token_id INT,
#     timestamp INT, 
#     data JSON,
#     PRIMARY KEY (id)
# )

def insert_metadata(collection_id, contract, token_id, data):
    ts = int(datetime.now().timestamp())
    engine = get_db_connection()
    with engine.connect() as con:
        r = con.execute(
            """
            INSERT INTO nft_metadata 
            (collection_id, contract_address, token_id, data, timestamp) 
            VALUES (%s, %s, %s, %s, %s) 
            """,
            (collection_id, contract, token_id, data, ts)
        )