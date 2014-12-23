import sys
import fileinput
import os
import subprocess

from ...result import *

################################################################################
def cpuload(args):
  val= subprocess.getoutput("iostat proc")
  strs=val.split("\n")
  vals=strs[2].split()
  idle= vals[6]
  sys=vals[4]
  user=vals[2]
  interrupt=vals[5]
  user_niced=vals[3]
    
  out={"user":user,
       "ucer_niced":user_niced,       
       "system":sys,
       "interrupt":interrupt,
       "idle":idle}
  #print (json.dumps(out))
  return Result(out)


################################################################################
#                        extended device statistics  
#device     r/s   w/s    kr/s    kw/s qlen svc_t  %b  
#ada0       0.6  20.1    15.9   252.6    0   3.6   2
def hddload(args):
  val=subprocess.getoutput("iostat -t da -x")
  strs=val.split("\n")[2:];
  out = []
  for line in strs:
    sp=line.split()
    entry={"name":sp[0],
           "reads":sp[1],
	   "writes":sp[2],
	   "read":sp[3],
	   "write":sp[4],
	   "queue":sp[5]}
    ##out[sp[0]]=entry;
    out.append(entry)
  
  #print (json.dumps(out))l
  return Result(out)
  
################################################################################
def basesystem(args):
    
  out = {"base_system_version": subprocess.getoutput("uname -r"),
	 "uptime":subprocess.getoutput("uptime")}
  #print (json.dumps(out))
  return Result(out)

################################################################################
def shells(args):
  f = open('/etc/shells')
  shells = []
  for line in f:
    line= line.strip()
    if (line == '') or (line[0] == "#"):
      continue
    shells.append(line)
  return Result(shells)

################################################################################
def hostname(args):
  return Result(subprocess.getoutput("hostname"))