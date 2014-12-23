from .db.db import db

################################################################################
################################################################################
class Singleton(type):
  instance = None
  def __call__(cls, *args, **kw):
    if not cls.instance:
      cls.instance = super(Singleton, cls).__call__(*args, **kw)
    return cls.instance

################################################################################
################################################################################
class session(object, metaclass=Singleton):
  def __init__(self):
    self._isAdmin = False;
    self._user = ""
    self._sid=""
    self._isValid=False
    
  def beginSession(self, sid):
    DB= db()
    DB.removeOldSessions()
    res = DB.findSession(sid)
    if res is None:
      self._isAdmin = False
      self._user = ""
      self._sid=""
      self._isValid=False
      return False
    #{"SID": data[0], "user":data[1], "expires":data[2], "is_admin":data[3]}
    self._user = res["user"]
    self._sid = sid
    self._isAdmin = res["is_admin"] == "1"
    self._isValid = True
    
    DB.touchSession(sid)
    
    return True
  
  def createSession(self, sid, user, isAdmin):
    pass
  
  def isValid(self):
    return self._isValid
  
  def isAdmin(self):
    return self._isAdmin
  
  def user(self):
    return self._user
  
  def sid(self):
    return self._sid