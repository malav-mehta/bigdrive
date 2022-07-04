import click


def log(message):
    click.echo("Error: {}".format(message), err=True)


def log_exit(message, code=1):
    log(message)
    exit(code)


def exit_if_error(result: dict):
    if "error" in result:
        log_exit(result["error"]["message"])
