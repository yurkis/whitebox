from ...result import *

import subprocess

def list(args):  
  is_all = False
  if len(args) and (args[0].lower() == "all"):
    is_all = True
    
  val=subprocess.getoutput("pw usershow -a -P")
  strs=val.split("\n");
  out = []
  # =========== Example output: ==========
  #Login Name: root              #0            Group: wheel             #0
  #Full Name: Charlie Root
  #     Home: /root                           Class: 
  #     Shell: /bin/csh                       Office: [None]
  #Work Phone: [None]                     Home Phone: [None]
  #Acc Expire: [None]                     Pwd Expire: [None]
  #  Groups: wheel,operator  
  
  login = ""
  name = ""
  uid = 0
  main_group = ""
  home = ""
  shell = ""
  groups = []
  is_admin = False  
  
  for line in strs:
    #remove duplicated spaces
    #line = line.strip()
    #line = "  ".join(line.split())
    #spl = line.split()
    #if spl[0].lower() == "login name:":
    #  pass
    line = line.strip()
    if line.startswith("Login Name: "):
      line = line.replace("Login Name: ", "").strip()
      if len(login):
        out.append({"login":login, "name":name, "uid":uid, "main_group":main_group, "home":home, "shell":shell, "aux_groups":groups, "admin":is_admin })
        is_admin = False
      uid = 0
      main_group = shell = home = groups = ""
      login = line.split(" ")[0]
      line = line[len(login):].strip()
      
      if line.startswith("#"):
         line = line[1:].strip()     
         tmp = line.split()[0]
         uid = int(tmp)
         if uid<1000 and not is_all:
           login=""
           continue
         line = line[len(tmp):]
         line = line.strip()
      if line.startswith("Group: "):            
         line = line.replace("Group: ","").strip()
         main_group = line.split()[0].strip()
      if main_group.lower() == "wheel":
         is_admin= True
      continue
    
    if line.startswith("Full Name: "):
      name = line[len("Full Name: "):].strip()
      continue
    
    if line.startswith("Home: "):
      home = line[len("Home: "):].strip().split(" ")[0]
      continue
    
    if line.startswith("Shell: "):
      shell = line[len("Shell: "):].strip().split(" ")[0]
      continue
    
    if line.startswith("Groups: "):
      groups = line[len("Groups: "):].strip().split(",")
      
  return Result(out)

def add(args):
  return Unimplemented()

def modify(args):
  return Unimplemented()

def remove(args):
  return Unimplemented()