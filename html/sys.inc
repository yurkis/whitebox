<?php

class sys
{

private function __construct(){

}

protected function __clone() {

}

const SYS_CALL_STR = '/usr/local/bin/wb/sys';

static public function getInstance() {  
  static $inst = null;
  if (is_null($inst))
  {
      $inst = new self();
  }
  return $inst;
}

protected static function sys()
{
  $fargs='';
  /*if (func_get_arg(0) == true)
  {
    session_start();
    $my_sid = session_id();
    $fargs="-sid $my_sid";
  }*/
  for ($i=1; $i<func_num_args(); $i++)
  {
    $fargs=$fargs." ".escapeshellarg(func_get_arg($i));
  }
  $ret = shell_exec(self::SYS_CALL_STR.$fargs);
  //echo "<br>".self::SYS_CALL_STR.$fargs."<br>";
  list($result, $out) = explode("\n", $ret);
  return $out;
}

public static function shutdown()
{
  return self::sys(true,'hw','shutdown');
}

public static function reboot()
{
  return self::sys(true, 'hw','reboot');
}

public static function devUpdate($callback)
{
  return self::sys(true, 'dev','update',$callback);
}

public static function hwInfo()
{
  return self::sys(true, 'hw','info');
}

public static function sysInfo()
{
  return self::sys(true, 'sys','info','basesystem');
}

public static function getHDDLoad()
{
  return self::sys(true, 'sys','info', 'hddload');
}

public static function getCPULoad()
{
  return self::sys(true, 'sys','info', 'cpuload');
}

public static function getSysCommandsList()
{
  $out= shell_exec(self::SYS_CALL_STR." listcommands");
  return $out;
}

public static function getHostname()
{
  return self::sys(false, 'sys', 'info', 'hostname');
}

public static function login($user, $passwd)
{
  session_start();
  $my_sid=session_id();
  echo "SID:$my_sid";
  self::sys(false,'auth','login', "user=$user", "password=$password", "sid=$my_sid");
}

public static function logout()
{
  return self::sys(true, 'auth', 'logout');
}

public static function getGroups()
{
  return self::sys(true, 'auth', 'groups');
}

public static function getSessions()
{
  return self::sys(true, 'auth', 'sessions');
}

public static function getShells()
{
  return self::sys(false, 'sys', 'info', 'shells');
}

}//class sys
  
?>
