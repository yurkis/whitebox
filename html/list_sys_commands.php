<html>
<body>
<h2><a href="index.php">Back to home</a></h2>
<?php
require_once("sys.inc");
#$shell_out = shell_exec("/usr/local/bin/pwb/sys dev update 2>&1");
$shell_out=sys::getSysCommandsList();
echo "Current supported sys commands:";
echo "<pre>$shell_out</pre>";
?>
<h2><a href="index.php">Back to home</a></h2>
</body>
</html>
