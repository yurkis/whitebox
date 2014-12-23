import json


class BaseResult:
  
  def __init__(self, isSuccess, payload):
    self._isSuccess = isSuccess
    self._Payload = payload
  
  def isSuccess(self):
    return self._isSuccess
  
  def out(self):
    if self._isSuccess:
       print("OK")
       print(json.dumps(self._Payload))
    else:
       print("ERROR")
       print(self._Payload)
       
class Result(BaseResult):
  def __init__(self, payload):
    BaseResult.__init__(self, True, payload)
    
class Error(BaseResult):
  def __init__(self, name):
     BaseResult.__init__(self, False, name)
     
  INTERNAL_ERROR = "INTERNAL_ERROR"
  WRONG_PARAM    = "WRONG_PARAM"
  UNAUTORIZED    = "UNAUTHORIZED"
  UNIMPLEMENTED  = "UNIMPLEMENTED"
  ROOT_REQUIRED  = "ROOT_REQUIRED"
  AUTH_FAILED    = "AUTH_FAILED"
  
  
class Success(BaseResult):
  def __init__(self):
    BaseResult.__init__(self, True, None)
    
class Unimplemented(BaseResult):
  def __init__(self):
    BaseResult.__init__(self, False, Error.UNIMPLEMENTED)
