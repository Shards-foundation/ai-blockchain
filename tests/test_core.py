import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.blockchain import Blockchain

def test_blockchain():
    # Instantiate the Blockchain
    blockchain = Blockchain()

    # Add some transactions
    blockchain.add_transaction(
        sender="Alice",
        recipient="Bob",
        payload={"content": "AI Generated Image 1"},
        tx_type="REGISTER_AI_CONTENT"
    )
    blockchain.add_transaction(
        sender="Bob",
        recipient="Charlie",
        payload={"agent_id": "Agent_007"},
        tx_type="REGISTER_AI_AGENT"
    )

    # Mine a block
    last_block = blockchain.last_block
    last_proof = last_block.proof
    proof = blockchain.proof_of_work(last_proof)

    # Forge the new Block by adding it to the chain
    previous_hash = last_block.hash
    block = blockchain.create_block(proof, previous_hash)

    print(f"Block {block.index} mined with proof {block.proof}")
    print(f"Blockchain length: {len(blockchain.chain)}")
    print(f"Is chain valid? {blockchain.is_chain_valid(blockchain.chain)}")

    # Add more transactions and mine another block
    blockchain.add_transaction(
        sender="Charlie",
        recipient="Alice",
        payload={"action": "Content Verification"},
        tx_type="AGENT_ACTION_LOG"
    )
    last_block = blockchain.last_block
    last_proof = last_block.proof
    proof = blockchain.proof_of_work(last_proof)
    previous_hash = last_block.hash
    block = blockchain.create_block(proof, previous_hash)

    print(f"Block {block.index} mined with proof {block.proof}")
    print(f"Blockchain length: {len(blockchain.chain)}")
    print(f"Is chain valid? {blockchain.is_chain_valid(blockchain.chain)}")

if __name__ == "__main__":
    test_blockchain()
