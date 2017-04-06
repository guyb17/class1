#! /usr/bin/env python

from ciscoconfparse import CiscoConfParse
c_cfg = CiscoConfParse("cisco_ipsec.txt")
cryp_map = c_cfg.find_objects('group2')

for element in cryp_map:
  print element.parent.text
  print element.text
  for child in element.children:
    print child.text
