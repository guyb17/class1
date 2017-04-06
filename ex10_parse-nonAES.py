#! /usr/bin/env python

from ciscoconfparse import CiscoConfParse
c_cfg = CiscoConfParse("cisco_ipsec.txt")
cryp_map = c_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"set transform-set AES-SHA")


for element in cryp_map:
      print element.text
      for child in element.children:
         print child.text

