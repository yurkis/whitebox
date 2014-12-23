<html>
<body>
<h2><a href="index.php">Back to home</a></h2>
<?php
  $ret = shell_exec("/bin/local/bin/sudo /usr/local/bin/pwb/devpanic");
  echo "<pre>$ret</pre>";
?>