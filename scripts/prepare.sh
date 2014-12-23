#!/bin/sh
#my_dir=
echo "=============================================="
echo "Installing packages..."
pkg install nginx
pkg install php55
pkg install php55-extensions
pkg install php55-json
pkg install mc
pkg install subversion

echo "============================================="
echo " Fetching source...."
mkdir /usr/local/www/pwb/html
svn co https://xp-dev.com/svn/pwb/trunk/html/ /usr/local/www/pwb/html
mkdir /usr/local/bin/pwb
svn co https://xp-dev.com/svn/pwb/trunk/sysmanager/ /usr/local/bin/pwb/

echo "=============================================="
echo "Config files...."
echo 'ALL ALL=NOPASSWD:/usr/local/bin/pwb/sysmanager'>>/usr/local/etc/sudoers
echo 'php_fpm_enable="YES"'>>/etc/rc.conf
echo 'pwb_enable="YES"'>>/etc/rc.conf

echo "============================================="
echo " Starting...."
/usr/local/etc/rc.d/php-fpm start
/usr/local/etc/rc.d/pwb start