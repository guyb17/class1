#! /usr/bin/env python

import yaml
import json

a_dict = {
  'name': 'a10-adc-01',
  'ip' : '10.10.10.10',
  'acos_ver': '4.1.1P2',
}

a_list = [
  'string1',
  'string2',
  a_dict
]
   
with open("output_yml", "w") as f:
  f.write(yaml.dump(a_list, default_flow_style=False))

with open("output_json", "w") as f:
  json.dump(a_list, f) 
