import hashlib
import json
import time
from typing import List, Dict, Any, Optional

class Block:
    def __init__(self, index: int, transactions: List[Dict[str, Any]], timestamp: float, previous_hash: str, proof: int = 0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.proof = proof
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        block_string = json.dumps({
            "index": self.index,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "proof": self.proof
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def __repr__(self):
        return f"Block(index={self.index}, hash={self.hash})"

class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.pending_transactions: List[Dict[str, Any]] = []
        # AI-specific state (Ledger)
        self.ai_content_registry: Dict[str, Dict[str, Any]] = {}
        self.ai_agent_registry: Dict[str, Dict[str, Any]] = {}
        self.agent_action_logs: List[Dict[str, Any]] = []
        # Create the genesis block
        self.create_block(proof=100, previous_hash='1')

    def create_block(self, proof: int, previous_hash: str) -> Block:
        block = Block(
            index=len(self.chain) + 1,
            transactions=self.pending_transactions,
            timestamp=time.time(),
            previous_hash=previous_hash,
            proof=proof
        )
        # Process transactions to update the ledger state
        self._process_transactions(self.pending_transactions)
        self.pending_transactions = []
        self.chain.append(block)
        return block

    def _process_transactions(self, transactions: List[Dict[str, Any]]):
        for tx in transactions:
            tx_type = tx.get("type")
            payload = tx.get("payload")
            if tx_type == "REGISTER_AI_CONTENT":
                content_hash = payload.get("content_hash")
                if content_hash:
                    self.ai_content_registry[content_hash] = payload
            elif tx_type == "REGISTER_AI_AGENT":
                agent_id = payload.get("agent_id")
                if agent_id:
                    self.ai_agent_registry[agent_id] = payload
            elif tx_type == "AGENT_ACTION_LOG":
                self.agent_action_logs.append(tx)

    def add_transaction(self, sender: str, recipient: str, payload: Dict[str, Any], tx_type: str) -> int:
        transaction = {
            "sender": sender,
            "recipient": recipient,
            "payload": payload,
            "type": tx_type,
            "timestamp": time.time()
        }
        self.pending_transactions.append(transaction)
        return self.last_block.index + 1

    @property
    def last_block(self) -> Block:
        return self.chain[-1]

    def proof_of_work(self, last_proof: int) -> int:
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof: int, proof: int) -> bool:
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def is_chain_valid(self, chain: List[Block]) -> bool:
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            if block.previous_hash != last_block.hash:
                return False
            if not self.valid_proof(last_block.proof, block.proof):
                return False
            last_block = block
            current_index += 1
        return True

    def get_content_info(self, content_hash: str) -> Optional[Dict[str, Any]]:
        return self.ai_content_registry.get(content_hash)

    def get_agent_info(self, agent_id: str) -> Optional[Dict[str, Any]]:
        return self.ai_agent_registry.get(agent_id)

    def get_agent_logs(self, agent_id: str) -> List[Dict[str, Any]]:
        return [log for log in self.agent_action_logs if log["payload"].get("agent_id") == agent_id]
