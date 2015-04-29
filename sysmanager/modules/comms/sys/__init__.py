from . import *
from . import sys
from . import info
from . import services

commands={"sys":{"subcomms":
		     {"info": {"subcomms":{
	                                    "cpuload":{"fn":info.cpuload},
	                                    "hddload":{"fn":info.hddload},
	                                    "basesystem":{"fn":info.basesystem},
	                                    "shells":{"fn":info.shells},
	                                    "hostname": {"noauth":True, "fn":info.hostname},
	                                   },# info subcomms
	                      },#info
		     "update": {"admin":True, "fn":sys.update},		     
		     "services": {"subcomms":{
	                                    "list":{"admin":True,"fn":services.list},
	                                    
	                                   },# services subcomms
		                 },
		     "shutdown":{"admin":True, "shellcmd":"shutdown -h now"},
		     "reboot":{"admin":True, "shellcmd":"shutdown -r now"},
	         }}
	  }