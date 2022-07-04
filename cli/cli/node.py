import click
from prettytable import PrettyTable

from cli.utils import api, metadata, format


@click.command("list", help="List all nodes registered to current user")
def list_nodes():
    result = api.get("/nodes")

    table = PrettyTable()
    table.field_names = ["Node name", "Capacity", "Used space", "Status"]
    table.add_rows([
        [
            node["name"],
            format.human_file_size(node["committedBytes"]),
            format.human_file_size(node["usedBytes"]),
            "active" if node["isActive"] else "inactive"
        ]
        for node in sorted(result, key=lambda n: n["committedBytes"], reverse=True)
    ])
    click.echo(table.get_string())


@click.command("create", help="Host a new storage node from this device")
@click.option("-n", "--name", help="Name for new storage node", required=True, type=str)
@click.option("-c", "--capacity", help="Capacity for node (MB)", required=True, default=1024, type=int)
def create_node(name, capacity):
    capacity *= (1000 ** 2)

    if not click.confirm(
            f"Do you want to create node \"{name}\" with a capacity of {format.human_file_size(capacity)}"):
        click.echo("Exiting...")
        exit(0)
    if not isinstance(capacity, int):
        click.echo("Capacity must be integer", err=True)
        exit(1)

    result = api.post("/node", {
        "name": name,
        "committedBytes": capacity
    })

    metadata.add_node(result["nodeId"])
    click.echo(f"Created node {name} ({format.human_file_size(capacity)} capacity)")
