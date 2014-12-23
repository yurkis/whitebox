from ...result import *

import subprocess

def list(args):  
  hide_sys=True
  if len(args) and args[0].lower() == "all":
    hide_sys = False
  result = []
  f = open('/etc/group')
  for line in f:
    line= line.strip()
    if (line == '') or (line[0] == "#"):
      continue
    items = line.split(':')
    if (int(items[2]) <1000) and (hide_sys):
      continue
    users=[]
    if len(items)>3:
      users = items[3].split(',')
    result.append({"name":items[0], "gid":items[2], "users":users})
  
  return Result(result)