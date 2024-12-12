from datetime import datetime

import click
from tqdm import tqdm

from firebase_setup import db

commands = []


def command(func):
    commands.append(func)
    return func


## Start of commands

@command
def update_all_disconnected_suite_104_trips():
    trips = db.collection('trips')
    docs = list(trips.stream())
    print(f'Found {len(docs)} documents')
    trips_updated = 0

    for doc in tqdm(docs, desc="Updating trips"):
        data = doc.to_dict()
        if data.get('propertyRef') == db.document('properties/DUXs6yG6Fs4UfqwcyYhU'):
            doc.reference.update({'propertyRef': db.document('properties/6KyLJMpoPeKNkUM5Hdq2')})
            trips_updated += 1

    print(f'Updated {trips_updated} trips')





## End of commands

@click.command()
@click.argument('command', type=click.Choice([c.__name__ for c in commands]))
def patch(command):
    command_lookup = {c.__name__: c for c in commands}

    start = datetime.now()
    command_lookup[command]()

    print(f'Patch took {(datetime.now() - start).total_seconds():0.2f}s')


if __name__ == '__main__':
    patch()
