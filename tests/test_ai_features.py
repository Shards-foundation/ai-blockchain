import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.blockchain import Blockchain
from core.smart_contract import SmartContractManager, content_licensing_contract

def test_ai_features():
    # Instantiate the Blockchain
    blockchain = Blockchain()

    # 1. Register AI Content
    content_hash = "sha256_of_ai_image_123"
    blockchain.add_transaction(
        sender="AI_Artist_01",
        recipient="Blockchain",
        payload={"content_hash": content_hash, "creator": "AI_Artist_01", "model": "StableDiffusion-v1.5"},
        tx_type="REGISTER_AI_CONTENT"
    )

    # 2. Register AI Agent
    agent_id = "Agent_Alpha"
    blockchain.add_transaction(
        sender="Dev_Team_X",
        recipient="Blockchain",
        payload={"agent_id": agent_id, "developer": "Dev_Team_X", "capabilities": ["image_generation", "text_analysis"]},
        tx_type="REGISTER_AI_AGENT"
    )

    # 3. Log Agent Action
    blockchain.add_transaction(
        sender="Agent_Alpha",
        recipient="Blockchain",
        payload={"agent_id": agent_id, "action_type": "CONTENT_GENERATED", "action_details": {"content_hash": content_hash}},
        tx_type="AGENT_ACTION_LOG"
    )

    # Mine a block to process transactions
    last_block = blockchain.last_block
    last_proof = last_block.proof
    proof = blockchain.proof_of_work(last_proof)
    blockchain.create_block(proof, last_block.hash)

    # Verify Registry
    print(f"Content Info: {blockchain.get_content_info(content_hash)}")
    print(f"Agent Info: {blockchain.get_agent_info(agent_id)}")
    print(f"Agent Logs: {blockchain.get_agent_logs(agent_id)}")

    # 4. Test Smart Contract
    scm = SmartContractManager(blockchain)
    scm.deploy_contract("Licensing", content_licensing_contract)

    # Set License
    result = scm.call_contract("Licensing", "AI_Artist_01", {"action": "set_license", "content_hash": content_hash, "license_type": "CC-BY-4.0", "price": 10})
    print(f"Smart Contract Result (Set License): {result}")

    # Purchase License
    result = scm.call_contract("Licensing", "User_Bob", {"action": "purchase_license", "content_hash": content_hash})
    print(f"Smart Contract Result (Purchase License): {result}")

if __name__ == "__main__":
    test_ai_features()
