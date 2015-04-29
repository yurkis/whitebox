import sys
import fileinput
import os
import subprocess
import tempfile
import stat

from ...result import *

################################################################################
def update(args):
  f= tempfile.NamedTemporaryFile(delete= False)
  os.chmod(f.name, 0o664)
  pid=os.fork()
  if pid>0:
    return Error(Error.UNIMPLEMENTED)
  os.system("freebsd-update fetch >"+f.name+" 2>&1")
  if len(args):
    os.system(args[0])
  f.close()
  os.unlink(f.name)

