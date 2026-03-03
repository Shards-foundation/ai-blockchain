from typing import Dict, Any, Callable, List

class SmartContract:
    def __init__(self, name: str, code: Callable):
        self.name = name
        self.code = code
        self.state: Dict[str, Any] = {}

    def execute(self, blockchain: Any, sender: str, args: Dict[str, Any]) -> Dict[str, Any]:
        return self.code(blockchain, self.state, sender, args)

class SmartContractManager:
    def __init__(self, blockchain: Any):
        self.blockchain = blockchain
        self.contracts: Dict[str, SmartContract] = {}

    def deploy_contract(self, name: str, code: Callable):
        self.contracts[name] = SmartContract(name, code)

    def call_contract(self, name: str, sender: str, args: Dict[str, Any]) -> Dict[str, Any]:
        if name not in self.contracts:
            raise ValueError(f"Contract {name} not found.")
        return self.contracts[name].execute(self.blockchain, sender, args)

# Example Smart Contract: Content Licensing
def content_licensing_contract(blockchain, state, sender, args):
    action = args.get("action")
    content_hash = args.get("content_hash")
    
    if action == "set_license":
        license_type = args.get("license_type")
        price = args.get("price")
        state[content_hash] = {"license_type": license_type, "price": price, "owner": sender}
        return {"status": "success", "message": f"License set for {content_hash}"}
    
    elif action == "purchase_license":
        if content_hash not in state:
            return {"status": "error", "message": "Content not licensed."}
        # In a real blockchain, we would check for payment here
        return {"status": "success", "message": f"License purchased for {content_hash} from {state[content_hash]['owner']}"}
    
    return {"status": "error", "message": "Invalid action."}
