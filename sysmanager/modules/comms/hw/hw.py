import json
import subprocess
import os
from ...result import *

################################################################################
def do_hw_info(args):
  cpu=subprocess.getoutput("sysctl -n hw.model")
  cpu_cores=subprocess.getoutput("sysctl -n kern.smp.cpus")
  out={"cpu":{"ident":cpu,"cores":cpu_cores}}
  return Result(out)
  #out

################################################################################
#def do_hw(args):
#  subshellcomms = {"shutdown":"shutdown -h now",
#		   "reboot":"shutdown -r now"}
#  if args[0] in subshellcomms:
#    os.system(subshellcomms[args[0]])
#    return
#  
#  comms    = {"info":do_hw_info}
#  if args[0] in comms:
#    comms[args[0]](args[1:])
#  
#  return