import click
import requests
import json

BASE_URL = "http://localhost:5000"

@click.group()
def cli():
    """Blockchain CLI for AI Content and Agent Tracking."""
    pass

@cli.command()
def mine():
    """Mine a new block."""
    response = requests.get(f"{BASE_URL}/mine")
    click.echo(json.dumps(response.json(), indent=4))

@cli.command()
def chain():
    """Get the full blockchain."""
    response = requests.get(f"{BASE_URL}/chain")
    click.echo(json.dumps(response.json(), indent=4))

@cli.command()
@click.option('--sender', required=True, help='Sender address.')
@click.option('--recipient', required=True, help='Recipient address.')
@click.option('--payload', required=True, help='JSON payload.')
@click.option('--type', required=True, help='Transaction type.')
def transaction(sender, recipient, payload, type):
    """Create a new transaction."""
    try:
        payload_json = json.loads(payload)
    except ValueError:
        click.echo("Error: Payload must be a valid JSON string.")
        return

    data = {
        "sender": sender,
        "recipient": recipient,
        "payload": payload_json,
        "type": type
    }
    response = requests.post(f"{BASE_URL}/transactions/new", json=data)
    click.echo(json.dumps(response.json(), indent=4))

@cli.command()
@click.argument('content_hash')
def content(content_hash):
    """Get AI content info by hash."""
    response = requests.get(f"{BASE_URL}/registry/content/{content_hash}")
    click.echo(json.dumps(response.json(), indent=4))

@cli.command()
@click.argument('agent_id')
def agent(agent_id):
    """Get AI agent info by ID."""
    response = requests.get(f"{BASE_URL}/registry/agent/{agent_id}")
    click.echo(json.dumps(response.json(), indent=4))

if __name__ == '__main__':
    cli()
