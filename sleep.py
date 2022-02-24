from db import db
from google.cloud import firestore

# Firestore object
sleep_record_ref = db.collection(u'sleep')

# Create Sleep Record
def createSleepRecord(userid, start_time=None, end_time=None, sleep_rating=None, dream_rating=None, sleep_event=None):
    sleep_dict = dict()
    sleep_dict['userid'] = userid
    sleep_dict['date'] = firestore.SERVER_TIMESTAMP
    sleep_dict['start_time'] = start_time
    sleep_dict['end_time'] = end_time
    sleep_dict['sleep_rating'] = sleep_rating
    sleep_dict['dream_rating'] = dream_rating
    sleep_dict['sleep_event'] = sleep_event

    # Add Sleep Record to database
    sleep_record = sleep_record_ref.add(sleep_dict)
    
    return
