# -*- coding: utf8 -*-
import pymongo
import os
import pandas
import datetime
import LatLon
import re
import datetime
from bson.objectid import ObjectId
import numpy as np
import sys
import json

Client = pymongo.MongoClient(host='127.0.0.1', port=3002);
db = Client.meteor;

def FormatRecords(r):
    s = db.Stations.find_one({'_id':r['_id_Station']})
    return {
    'type': "Feature",
    'properties': {
      'value': r['temperature']
    },
    'geometry': s['location']
  };

db.Climat.find({'date':datetime.datetime(2012,3,3,0,0,0)})

records = [FormatRecords(x) for x in db.Climat.find({'date':datetime.datetime(2011
,2,3,0,0,0)}) if x['temperature'] is not None]

Feature = {'type': "FeatureCollection", 'features': records}

with open('data.json', 'w') as outfile:
    json.dump(Feature, outfile)
