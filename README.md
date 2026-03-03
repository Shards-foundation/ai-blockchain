# AI Content and Agent Tracking Blockchain

## Overview

This project implements a specialized blockchain designed to track the provenance and activities of AI-generated content and AI agentic agents. It provides an immutable and verifiable ledger for recording the creation, modification, ownership, and actions related to AI assets. The blockchain aims to enhance transparency, trust, and accountability within the rapidly evolving AI ecosystem.

## Features

*   **Decentralized Ledger:** A distributed network of nodes maintains a shared, tamper-proof record of all AI-related transactions.
*   **AI Content Provenance:** Tracks the origin, creation details, and history of AI-generated content (e.g., images, text, audio).
*   **AI Agent Activity Logging:** Records significant actions performed by AI agents, providing an audit trail of their operations.
*   **Smart Contract Support:** Enables the deployment of smart contracts for automated licensing, agent orchestration, and dispute resolution.
*   **Proof of Stake (PoS) Consensus:** Utilizes a PoS-like mechanism for efficient and scalable transaction validation.
*   **RESTful API:** Provides an interface for applications and users to interact with the blockchain network.
*   **Command-Line Interface (CLI):** A simple tool for basic blockchain operations and queries.

## Architecture

The blockchain consists of the following main components:

*   **Core Blockchain Engine:** Handles block creation, transaction management, and consensus (Proof of Work for simplicity in this initial implementation, but designed for PoS).
*   **AI-Specific Transaction Types:** Custom transaction types for registering AI content, registering AI agents, and logging agent actions.
*   **Ledger:** Maintains the state of registered AI content and agents.
*   **Smart Contract Layer:** Allows for the execution of custom logic on the blockchain.
*   **REST API:** Built with Flask, exposing endpoints for mining, transactions, chain retrieval, and registry lookups.
*   **CLI:** A Python-based command-line tool for interacting with the REST API.

## Getting Started

### Prerequisites

*   Python 3.8+
*   `pip` (Python package installer)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/ai-blockchain.git
    cd ai-blockchain
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Running the Blockchain Node

To start a blockchain node, navigate to the `api` directory and run:

```bash
python3 api/node.py -p 5000
```

Replace `5000` with your desired port number. You can run multiple nodes on different ports to simulate a network.

### Using the CLI

Once a node is running, you can interact with it using the CLI:

*   **Mine a new block:**

    ```bash
    python3 cli/blockchain_cli.py mine
    ```

*   **View the full chain:**

    ```bash
    python3 cli/blockchain_cli.py chain
    ```

*   **Create a new AI content registration transaction:**

    ```bash
    python3 cli/blockchain_cli.py transaction --sender "AI_Artist_01" --recipient "Blockchain" --type "REGISTER_AI_CONTENT" --payload '{"content_hash": "sha256_of_my_ai_art", "creator": "AI_Artist_01", "model": "DALL-E-3"}'
    ```

*   **Get AI content information:**

    ```bash
    python3 cli/blockchain_cli.py content sha256_of_my_ai_art
    ```

*   **Create a new AI agent registration transaction:**

    ```bash
    python3 cli/blockchain_cli.py transaction --sender "Dev_Team_Y" --recipient "Blockchain" --type "REGISTER_AI_AGENT" --payload '{"agent_id": "Agent_Beta", "developer": "Dev_Team_Y", "capabilities": ["data_analysis", "report_generation"]}'
    ```

*   **Get AI agent information:**

    ```bash
    python3 cli/blockchain_cli.py agent Agent_Beta
    ```

*   **Log an AI agent action:**

    ```bash
    python3 cli/blockchain_cli.py transaction --sender "Agent_Beta" --recipient "Blockchain" --type "AGENT_ACTION_LOG" --payload '{"agent_id": "Agent_Beta", "action_type": "DATA_PROCESSED", "action_details": {"dataset_id": "dataset_xyz"}}'
    ```

## Project Structure

```
ai-blockchain/
├── api/
│   └── node.py         # Flask REST API for the blockchain node
├── cli/
│   └── blockchain_cli.py # Command-line interface
├── core/
│   ├── blockchain.py   # Core blockchain logic (Block, Blockchain classes)
│   └── smart_contract.py # Smart contract implementation
├── tests/
│   ├── test_core.py    # Unit tests for core blockchain
│   └── test_ai_features.py # Tests for AI-specific features and smart contracts
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## License

This project is licensed under the MIT License - see the LICENSE file for details. (Note: LICENSE file not yet created)
