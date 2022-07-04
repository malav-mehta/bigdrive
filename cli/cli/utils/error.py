import click


def log(message: str) -> None:
    click.echo(f"Error: {message}", err=True)


def log_exit(message: str, code: int = 1) -> None:
    log(message)
    exit(code)


def exit_if_error(result: dict) -> None:
    if "error" in result:
        log_exit(result["error"]["message"])
