import sqlite3
import os.path
import os
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
class db(object, metaclass=Singleton):
  #__metaclass__ = Singleton
  DB_FILE_PATH='/var/db/pwb/'
  DB_FILE_NAME='db.sqlite'
  ################################################################################
  def __init__(self):
    self._db=None
  ################################################################################
  def create(self):
    if os.path.isfile(self.DB_FILE_PATH + self.DB_FILE_NAME):
      os.remove(self.DB_FILE_PATH + self.DB_FILE_NAME)
    conn = sqlite3.connect(self.DB_FILE_PATH + self.DB_FILE_NAME)
    cur= conn.cursor()
    
    DUMP='''
	CREATE TABLE session ( 
	  SID               PRIMARY KEY
			    NOT NULL
			    UNIQUE,
	  user     CHAR     NOT NULL,
	  expires  DATETIME NOT NULL,
	  is_admin BOOLEAN  NOT NULL
			    DEFAULT ( 0 ) 
        );
	CREATE TABLE db_info ( 
	    db_ver 
	)'''
	
    comms = DUMP.split(";")
    for sql_comm in comms:
      cur.execute(sql_comm)
    
    cur.execute('INSERT INTO [db_info] ([db_ver]) VALUES (0);')
    conn.commit()	
    #conn.commit()
    conn.close()
  ################################################################################
  def open(self):
    if not os.path.exists(self.DB_FILE_PATH):
      os.makedirs(self.DB_FILE_PATH)
    if not os.path.isfile(self.DB_FILE_PATH + self.DB_FILE_NAME):
      self.create()
    self._db=sqlite3.connect(self.DB_FILE_PATH + self.DB_FILE_NAME)    
    pass
  
  ################################################################################
  def findSession(self, SID):
    c= self._db.cursor()
    c.execute('select SID, user, expires, is_admin from session where SID=?',[SID])
    data = c.fetchone()
    if data is None:
      return None
    retval = {"SID": data[0], "user":data[1], "expires":data[2], "is_admin":data[3]}
    return retval
  
  ################################################################################
  def createSession(self, SID, user, isAdmin):
    c= self._db.cursor()    
    is_adm="0"
    if isAdmin: is_adm = "1"
    c.execute("insert into session (SID, user, expires, is_admin) VALUES(?,?,datetime('now','+90 minutes'), ?)", (SID, user, is_adm))
    self._db.commit()
    
  ################################################################################
  def removeOldSessions(self):
    c= self._db.cursor()
    c.execute("delete from session where expires < datetime('now')")
    self._db.commit()
    
  ################################################################################
  def touchSession(self, sid):
    c= self._db.cursor()
    c.execute("update session set expires = datetime('now','+90 minutes') where sid=?",[sid])
    self._db.commit()
    
  ################################################################################
  def removeSession(self, sid):
    c= self._db.cursor()
    c.execute("delete from session where sid=?",[sid])
    self._db.commit()
  
  ################################################################################    
  def listSessions(self):
    self.removeOldSessions()
    c= self._db.cursor()
    c.execute("select user,datetime(expires,'-90 minutes') from session;")
    res = []
    q_res = c.fetchall()
    for line in q_res:
      res.append({"user":line[0], "last_activity":line[1]})
    return res