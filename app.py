from flask import Flask, request
import json
from db import *



app = Flask(__name__)



@app.route('/api/simple_hash_bsiugwiuevfishlg', methods=['POST'])
def simple_hash_endpoint():
    data = request.json
    for nft in data.get('nfts', []):
        try:
            _, contract, id = nft.get('nft_id').split('.')
            coll_id = create_or_get_nft_collection(contract, '')
            insert_metadata(coll_id, contract, id, json.dumps(nft))
        except Exception as e:
            print('Error finding contract address', nft, '\n', e)
    return {'ok': True}



if __name__ == "__main__":
    app.run()