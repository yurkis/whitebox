from ...result import *
from ...session import *
from ...db.db import db

import uuid
import pwd
import crypt
import subprocess

################################################################################
def login(args):
  if len(args)<2:
    return Error(Error.WRONG_PARAM)
  params = {}
  for a in args:
    arr=a.split('=')
    if len(arr)<2:
      return Error(Error.WRONG_PARAM)
    params.update({arr[0].lower():arr[1]})
  
  if ("password" not in params) or ("user" not in params):
    return Error(Error.WRONG_PARAM)
  
  #### Check login here!!!
  try:
    us=pwd.getpwnam(params["user"])
  except Exception:
    return Error(Error.AUTH_FAILED)
  else:
    if (us.pw_passwd == "*") or (us.pw_passwd == "x"):
      return Error(Error.AUTH_FAILED)
    pwd_hash=crypt.crypt(params["password"], str(us.pw_passwd))
    if pwd_hash != us.pw_passwd:
      return Error(Error.AUTH_FAILED)
  
  isAdmin = False
  out=subprocess.getoutput("pw show user yurkis -P|grep Groups:")
  out=out.replace("Groups:","")
  groups=out.split(",")
  for group in groups:
    isAdmin |=(group.strip() == "wheel") or ((group.strip() == "operator"))
  
  token=''
  
  
  if "sid" not in params:
     token=str(uuid.uuid4())
  else:
     token=params["sid"]    
  
  DB= db()
  
  res = DB.findSession(token)
  if res != None:
    if res["user"] == params["user"]:
      DB.touchSession()
      return Success()
    else:
      DB.removeSession(token)
  DB.createSession(token, params["user"], isAdmin)
  
  return Result(token)

################################################################################
def logout(args):
  #if not len(args):
  #  return Error(Error.WRONG_PARAM)
  
  #params = {}
  #for a in args:
  #  arr=a.split('=')
  #  if len(arr)<2:
  #    return Error(Error.WRONG_PARAM)
  #  params.update({arr[0].lower():arr[1]})
  
  #if "sid" not in params:
  #  return Error(Error.WRONG_PARAM)
  
  s = session()
  if not s.isValid():
    return Success()
  
  DB= db()
  
  res = DB.removeSession(s.sid())
  
  return Success()
  pass

################################################################################
def listsessions(args):
  DB= db()
  
  return Result(DB.listSessions())