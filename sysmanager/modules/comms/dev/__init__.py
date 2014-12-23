from . import *
from . import dev

commands={"dev":{"subcomms":
	         {"update":{"admin":True, "fn": dev.do_dev_update}}
	        }        
	 }