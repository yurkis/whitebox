from . import *
from . import sys
from . import info

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
		     "shutdown":{"admin":True, "shellcmd":"shutdown -h now"},
		     "reboot":{"admin":True, "shellcmd":"shutdown -r now"},
	         }}
	  }