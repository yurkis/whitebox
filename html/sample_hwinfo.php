<html>
<body>
<h2><a href="index.php">Back to home</a></h2>
<?php
  require_once('sys.inc');
  $shell_out = sys::hwInfo();
  $hwinfo = json_decode($shell_out);
  echo "<table width=90% border=0 cellspacing=1>";
  echo "<caption>Hardware info</caption>";
  echo "<tr><td>CPU</tdd><td>";
  echo $hwinfo->cpu->ident;
  echo "</td></tr>";
  echo "<tr><td>CPU cores</td><td>";
  echo $hwinfo->cpu->cores;
  echo "</td></tr></table>";
  echo "<br>Raw data:<br>";
  echo "<pre>$shell_out</pre>";
  
#  $shell_out = shell_exec("/usr/local/bin/pwb/sys sys info 2>&1");
  $shell_out = sys::sysInfo();
  $sysinfo = json_decode($shell_out);
  echo "<table width=90% border=0 cellspacing=1>";
  echo "<caption>System info</caption>";
  echo "<tr><td>Base system version</td><td> $sysinfo->base_system_version </td></tr>";
  echo "<tr><td>Uptime and load</td><td>$sysinfo->uptime</td></tr>";
  echo "</table>";
  
  echo "<br>Raw data:<br>";
  echo "<pre>$shell_out</pre>";

?>