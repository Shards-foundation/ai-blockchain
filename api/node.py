from flask import Flask, jsonify, request
import sys
import os
import requests
from uuid import uuid4
from urllib.parse import urlparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.blockchain import Blockchain

# Instantiate the Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    # We run the proof of work algorithm to get the next proof...
    last_block = blockchain.last_block
    last_proof = last_block.proof
    proof = blockchain.proof_of_work(last_proof)

    # We must receive a reward for finding the proof.
    # The sender is "0" to signify that this node has mined a new coin.
    blockchain.add_transaction(
        sender="0",
        recipient=node_identifier,
        payload={"reward": 1},
        tx_type="MINING_REWARD"
    )

    # Forge the new Block by adding it to the chain
    previous_hash = last_block.hash
    block = blockchain.create_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block.index,
        'transactions': block.transactions,
        'proof': block.proof,
        'previous_hash': block.previous_hash,
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    # Check that the required fields are in the POST'ed data
    required = ['sender', 'recipient', 'payload', 'type']
    if not all(k in values for k in required):
        return 'Missing values', 400

    # Create a new Transaction
    index = blockchain.add_transaction(values['sender'], values['recipient'], values['payload'], values['type'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': [vars(b) for b in blockchain.chain],
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()

    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        # In a real P2P, we would add these to a set of nodes
        pass

    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(nodes),
    }
    return jsonify(response), 201

@app.route('/registry/content/<content_hash>', methods=['GET'])
def get_content(content_hash):
    content = blockchain.get_content_info(content_hash)
    if content:
        return jsonify(content), 200
    return jsonify({'message': 'Content not found'}), 404

@app.route('/registry/agent/<agent_id>', methods=['GET'])
def get_agent(agent_id):
    agent = blockchain.get_agent_info(agent_id)
    if agent:
        return jsonify(agent), 200
    return jsonify({'message': 'Agent not found'}), 404

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)
