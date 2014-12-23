#from . import sys
#from . import hw
#from . import dev

#oomands = {"sys":
#	      {"info":
#	        {"cpuload":sys.do_sys_info_cpuload,
#	         "hddload":sys.do_sys_info_hddload},
#	       "update":sys.do_sys_update
#	      },
#	    "dev":
#	      {"update":dev.do_dev_update},
#	    "hw": 
#	      {"info":hw.do_hw_info}
#	    }
#
#commands = {"sys":{"subcomms":
#		     {"info": {"subcomms":{
#	                                    "cpuload":{"fn":sys.do_sys_info_cpuload},
#	                                    "hddload":{"fn":sys.do_sys_info_hddload},
#	                                   },# info subcomms
#	                      },#info
#		     "update": {"Admin":True, "fn":sys.do_sys_info_cpuload}}
#	         }, #sys subcomms		 
#        "hw":{"subcomms":
#		 {"info":{"fn":hw.do_hw_info}}
#	      },
#	"dev":{"subcomms":
#	         {"update":{"admin":True, "fn": dev.do_dev_update}}
#	      }        
#	}

#commands = {sys.commands, hw.commands, dev.commands}             