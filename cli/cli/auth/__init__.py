import click

import cli.auth.firebase
from ..utils import api, error, metadata


@click.command()
@click.option("--email", prompt="Email address", type=str)
@click.option("--password", prompt=True, hide_input=True, type=str)
def login(email: str, password: str) -> None:
    """Login with email and password"""
    result = firebase.auth.sign_in_with_email_and_password(email, password)
    error.exit_if_error(result)
    metadata.update_auth_config_from_sign_in(result["idToken"], email, password)

    click.echo("Successfully logged in as {}".format(metadata.get_config()["email"]))


@click.command()
@click.option("--email", prompt="Email address", type=str)
@click.password_option()
def register(email: str, password: str) -> None:
    """Register with email and password"""
    result = firebase.auth.sign_up_with_email_and_password(email, password)
    error.exit_if_error(result)
    metadata.update_auth_config_from_sign_in(result["idToken"], email, password)

    api.post("user", {
        "email": email
    })

    click.echo("Successfully registered {}".format(metadata.get_config()["email"]))


@click.command()
def user() -> None:
    """Current authenticated user email"""
    click.echo("Authenticated as: {}".format(metadata.get_config().get("email", "<not logged in>")))
