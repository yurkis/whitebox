import sys
import fileinput
import os
import subprocess
import tempfile
import stat

from ...result import *


################################################################################
def list(args):
  out = []
  comm_out=subprocess.getoutput("/usr/sbin/service -l -v").split("\n")
  prefix=''
  for line in comm_out:
    if line.startswith("From "):
       prefix= line.replace("From ", "").strip().replace(":","/")
       continue
     
    script= prefix + line
    is_enabled = False
    state = "Unknown"
    pid=0
    
    is_enabled = os.system(script+" enabled >/dev/null 2>&1") == 0
    status_output = subprocess.getoutput(script+" status")
    if (status_output.find("unknown directive") < 0):
      pass
    else:
      pass
    
    entry={"service":prefix + line, "state":"unknown", "enabled":is_enabled}
    out.append(entry)
		
  		  
  
  return Result(out)