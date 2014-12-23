import subprocess
from ...result import *

################################################################################
def do_dev_update(args):
  #print("\n\nUpdating sysmanager...")
  out_sysman=subprocess.getoutput("svn up /usr/local/bin/pwb")
  #print (out_sysman)
  
  #print ("\n\nUpdating html...")
  out_html=subprocess.getoutput("svn up /usr/local/www/pwb/html")
  return (Result(out_html + "\n\n" + out_sysman))

