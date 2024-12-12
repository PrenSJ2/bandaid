from datetime import datetime

import click

commands = []


def command(func):
    commands.append(func)
    return func



@click.command()
@click.argument('command', type=click.Choice([c.__name__ for c in commands]))
def patch(command):
    command_lookup = {c.__name__: c for c in commands}

    start = datetime.now()
    command_lookup[command]()

    print(f'Patch took {(datetime.now() - start).total_seconds():0.2f}s')


if __name__ == '__main__':
    patch()
