import atexit

import click

from .auth import login, register, user
from .node import create_node, list_nodes
from .utils import metadata


@click.group()
def bd() -> None:
    """BigDrive CLI tool help"""
    metadata.load_config()


@bd.group()
def auth() -> None:
    """Commands for auth"""


@bd.group()
def nodes() -> None:
    """Commands for managing nodes"""


auth.add_command(login)
auth.add_command(register)
auth.add_command(user)

nodes.add_command(create_node)
nodes.add_command(list_nodes)

atexit.register(metadata.dump_config)
