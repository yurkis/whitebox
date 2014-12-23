from . import *
from . import login
from . import users
from . import groups

commands={"auth":{"subcomms":
		    {
		     "login":{"fn":login.login, "noauth":True},
                     "logout":{"fn":login.logout},
                     "listsessions":{"admin":True, "fn":login.listsessions},
		     "users":{"subcomms":
		         {
			   "list":{"admin":True, "fn":users.list},
			   "add":{"admin":True, "fn":users.add},
			   "modify":{"admin":True, "fn":users.modify},
			   "remove":{"admin":True, "fn":users.remove},
			   
			 }},#auth.users subcomms
		      "groups":{"subcomms":
		         {
			   "list":{"admin":True, "fn":groups.list}   
			   
			 }#auth.users subcomms
	              }#auth.users
		    }#auth subcomms
		  }#auth 
         }#command

#commands={"sys":{"subcomms":
#		     {"info": {"subcomms":{
#	                                    "cpuload":{"fn":sys.do_sys_info_cpuload},
#	                                    "hddload":{"fn":sys.do_sys_info_hddload},
#	                                    "basesystem":{"fn":sys.do_sys_info_basesystem},
#	                                   },# info subcomms
#	                      },#info
#		     "update": {"admin":True, "fn":sys.do_sys_info_cpuload},
#		     "shutdown":{"admin":True, "shellcmd":"shutdown -h now"},
#		     "reboot":{"admin":True, "shellcmd":"shutdown -r now"},
#	         }}
#	  }