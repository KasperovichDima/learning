from explore2 import FROZENJson
import json


raw_feed = json.load(open('/home/kasper/Documents/projects/learning/fluent_python/22_dynamic_attrs/data.json'))
f = FROZENJson(raw_feed)
print(len(f.Schedule.speakers))

