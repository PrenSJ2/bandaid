from datetime import datetime
from devtools import debug

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


@command
def export_all_users():
    users = db.collection('users')
    docs = list(users.stream())
    print(f'Found {len(docs)} documents')
    users_exported = 0

    with open('users.csv', 'w') as file:
        file.write('userCity,email,display_name,photo_url,uid,created_time,bio,isHost,numberProperties,numberActiveBookings,termsandconditionsaccepted,isAdmin,company,phone_numbers,phone_number,smsOptIn,isTestAccount\n')

        for doc in tqdm(docs, desc="Exporting users"):
            data = doc.to_dict()
            file.write(f'{data.get("userCity")},{data.get("email")},{data.get("display_name")},{data.get("photo_url")},{data.get("uid")},{data.get("created_time")},{data.get("bio")},{data.get("isHost")},{data.get("numberProperties")},{data.get("numberActiveBookings")},{data.get("termsandconditionsaccepted")},{data.get("isAdmin")},{data.get("company")},{data.get("phone_numbers")},{data.get("phone_number")},{data.get("smsOptIn")},{data.get("isTestAccount")}\n')
            users_exported += 1

    print(f'Exported {users_exported} users')


@command
def export_user_emails():
    users = db.collection('users')
    docs = list(users.stream())
    print(f'Found {len(docs)} documents')
    emails_exported = 0

    with open('user_emails.csv', 'w') as file:
        for doc in tqdm(docs, desc="Exporting user emails"):
            data = doc.to_dict()
            file.write(f'{data.get("email")}\n')
            emails_exported += 1

    print(f'Exported {emails_exported} user emails')

@command
def find_trips_on_oct_31_2025():
    target_date = datetime(2025, 10, 31)
    trips = db.collection('trips')
    docs = list(trips.stream())
    print(f'Found {len(docs)} documents')
    trips_found = 0

    for doc in tqdm(docs, desc="Finding trips"):
        data = doc.to_dict()
        property_ref = data.get('propertyRef')
        if property_ref:
            property_doc = property_ref.get()
            if property_doc.id == 'vcW37l7JXVcVYecIuSN4':
                start_date = data.get('start_date')
                end_date = data.get('end_date')
                if start_date and end_date:
                    debug(f'Start date: {start_date}, End date: {end_date}')
                    start_date = datetime.strptime(start_date, '%Y-%m-%d')
                    end_date = datetime.strptime(end_date, '%Y-%m-%d')
                    if start_date <= target_date <= end_date:
                        print(f'Trip ID: {doc.id} occurs on or contains 31 October 2025')
                        trips_found += 1

    print(f'Found {trips_found} trips that occur on or contain 31 October 2025')


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
