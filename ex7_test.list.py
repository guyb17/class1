#! /usr/bin/env python

import yaml
import json
from pprint import pprint

   
with open("output_yml") as f:
  new_list1 = yaml.load(f)
  pprint(new_list1)

with open("output_json") as f:
  new_list2 = json.load(f)
  pprint(new_list2)
