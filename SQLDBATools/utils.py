# Function to return Dictionary from cursor of Queryset
# https://stackoverflow.com/a/14294314/4449743

from pypsrp.client import Client
import json
import time
import random

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

# cursor.execute("SELECT id, parent_id from test LIMIT 2");
# dictfetchall(cursor)
