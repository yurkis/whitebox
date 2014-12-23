<html>
<head>
<meta http-equiv="refresh" content="10">
</head>
<body>
<h2><a href="index.php">Back to home</a></h2>
<?php
  require_once('sys.inc');
  $shell_out = sys::getCPULoad();
  
  $cpuload = json_decode($shell_out);
  echo "<table width=40% border=0 cellspacing=1>";
  echo "<caption>CPU load</caption>";
  echo "<tr><td>User (%)</td><td> $cpuload->user </td></tr>";
  echo "<tr><td>Niced user (%)</td><td>$cpuload->ucer_niced </td></tr>";
  echo "<tr><td>System (%)</td><td>$cpuload->system </td></tr>";
  echo "<tr><td>Interrupt (%)</td><td>$cpuload->interrupt </td></tr>";
  echo "<tr><td>Idle (%)</td><td>$cpuload->idle </td></tr>";
  echo "</table>";
  
  echo "<br><br>Raw out:";
  echo "<pre>$shell_out</pre>";
  
  $shell_out = sys::getHDDLoad();
  $hddload = json_decode($shell_out);
  foreach( $hddload as $entry )
  {
    echo "<table width=40% border=0 cellspacing=1>";
    echo "<caption> $entry->name</caption>";
    echo "<tr><td>Read  (Kb/s)</td><td> $entry->read </td></tr>";
    echo "<tr><td>Write (Kb/s)</td><td> $entry->write </td></tr>";
    echo "<tr><td>Reads (1/s)</td><td> $entry->reads </td></tr>";
    echo "<tr><td>Writes (1/s)</td><td> $entry->writes </td></tr>";
    echo "<tr><td>Queue size</td><td> $entry->queue </td></tr>";
    echo "</table>";
  }

  echo "<br><br>Raw out:";
  echo "<pre>$shell_out</pre>";

?>