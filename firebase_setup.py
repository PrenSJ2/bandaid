import logging
from datetime import datetime, timezone, timedelta

import firebase_admin
from firebase_admin import credentials, firestore, storage

from utils import settings

tz = timezone.utc

current_time = datetime.now(timezone.utc)

cred = credentials.Certificate(settings.firebase_credentials)

app = firebase_admin.initialize_app(cred)

db = firestore.client()

firestore = firestore

# bucket_name = 'voulez-vous-97921.appspot.com'
#
# bucket = storage.bucket(bucket_name)
#
#
# def generate_signed_url(blob_name, expiration_time=timedelta(days=6)):
#     blob = bucket.blob(blob_name)
#     url = blob.generate_signed_url(version="v4", expiration=expiration_time, method="GET")
#     return url
