<html>
<body>
<h2><a href="index.php">Back to home</a></h2>
<?php
require_once("sys.inc");
#$shell_out = shell_exec("/usr/local/bin/pwb/sys dev update 2>&1");
$shell_out=sys::devUpdate('');
echo "Current update log:";
$out = json_decode($shell_out);
echo "<pre>$out</pre>";
?>
<h2><a href="index.php">Back to home</a></h2>
</body>
</html>

