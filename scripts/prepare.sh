#!/bin/sh
#my_dir=
echo "=============================================="
echo "Installing packages..."
pkg install -y nginx
pkg install -y python3
pkg install -y php55
pkg install -y php55-extensions
pkg install -y php55-json
pkg install -y ../sys/py33-sqlite3-3.3.5_5.txz
pkg install -y sudo
pkg install -y mc
#pkg install subversion

echo "============================================="
echo " Fetching source...."
mkdir /usr/local/www/wb/
#svn co https://xp-dev.com/svn/pwb/trunk/html/ /usr/local/www/pwb/html
ln -s `pwd`/../html /usr/local/www/wb/
#mkdir /usr/local/bin/pwb
ln -s `pwd`/../sysmanager /usr/local/bin/wb
#svn co https://xp-dev.com/svn/pwb/trunk/sysmanager/ /usr/local/bin/pwb/

echo "=============================================="
echo "Config files...."
echo 'ALL ALL=NOPASSWD:/usr/local/bin/wb/sysmanager'>>/usr/local/etc/sudoers
echo 'php_fpm_enable="YES"'>>/etc/rc.conf
echo 'wb_frontend_enable="YES"'>>/etc/rc.conf

cp ../sys/conf/overlay/usr/local/etc/rc.d/wb /usr/local/etc/rc.d
cp ../sys/nginx/* /usr/local/www/pwb/

echo "============================================="
echo " Starting...."
/usr/local/etc/rc.d/php-fpm start
/usr/local/etc/rc.d/wb_frontend start