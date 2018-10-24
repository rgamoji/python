#!/usr/bin/env python

import json
import ast
# I had to implement this silly hack to clean-up and format the results into a proper json structure.
# This one helped: https://stackoverflow.com/questions/25707558/json-valueerror-expecting-property-name-line-1-column-2-char-1
target={
   "Games":[]
}

with open(".rgamoji.jmg.orig", "r") as fH:
    for line in fH.readlines():
      json_input=ast.literal_eval(line)
      target["Games"].append(json_input) 
with open(".rgamoji.jmg.bkp","w") as fW:
    fW.write(json.dumps(target,indent=2))
    fW.write("\n")
