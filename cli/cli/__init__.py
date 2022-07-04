import atexit

import click

from .auth import login, register, user
from .utils import metadata


@click.group()
def bd():
    """BigDrive CLI tool help"""
    metadata.load_config()


@bd.group()
def auth():
    """Commands for auth"""


auth.add_command(login)
auth.add_command(register)
auth.add_command(user)

atexit.register(metadata.dump_config)
