Installing on Linux
===================

Ubuntu
******

Ubuntu 16.04LTS
---------------

Packages:

apt install -y git screen mysql-server ghostscript libgraphicsmagick-dev xpdf dcraw redis-server ffmpeg exiftool libreoffice apache2
systemctl enable apache2.service
systemctl start apache2.service
apt-get install -y software-properties-common
add-apt-repository ppa:ondrej/php
apt install -y php7.2 libapache2-mod-php7.2 php7.2-common php7.2-mbstring php7.2-xmlrpc php7.2-gd php7.2-xml php7.2-intl php7.2-mysql php7.2-cli  php7.2-zip php7.2-curl php7.2-posix php7.2-dev php-pear php7.2-redis php7.2-gmagick php7.2-gmp

Ubuntu 18.04LTS
---------------

To come


Red Hat Enterprise Linux/CentOS
*******************************

RHEL/CentOS 7
---------------------------------

1. Enable repositories:

	a. sudo yum install http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
	b. sudo yum install http://rpms.remirepo.net/enterprise/remi-release-7.rpm
	c. sudo yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm


2. Install and configure nginx 1.16.1

	a. sudo yum install nginx
	b. sudo systemctl enable --now nginx
    c. sudo usermod -aG nginx $USER
    d. sudo chown -R nginx:nginx /usr/share/nginx

test:

go to http://yourserverip or on the local machine:

	a. cd ~
	b. wget http://localhost/index.html
	c. nano index.html

	should be "Test Page for the Nginx HTTP Server on Red Hat Enterprise Linx"

	d. ctrl+x to exit nano
	e. rm index.html

3. Configure firewall for lan access

	a. sudo firewall-cmd --new-zone=localhttp --permanent
	b. sudo firewall-cmd --zone=localhttp --add-port=80/tcp --permanent
	c. sudo firewall-cmd --zone=localhttp --add-source=x.x.x.x/24 --permanent
	d. sudo firewall-cmd --reload

	sudo firewall-cmd --new-zone=localhttp --permanent && sudo firewall-cmd --zone=localhttp --add-port=80/tcp --permanent && sudo firewall-cmd --zone=localhttp --add-source=x.x.x.x/24 --permanent && sudo firewall-cmd --reload

https://linuxize.com/post/how-to-configure-and-manage-firewall-on-centos-8/

Test: try accessing your server ip in a web browser on another machine on the same subnet, you should see the nginx test page

4. Install PHP 7.4.13 (along with 1.7.9 required extensions)

	a. sudo yum install php php-pecl-mcrypt php-cli php-gd php-curl php-mysqlnd php-zip php-fileinfo php-devel php-gmagick php-opcache php-process php-xml php-mbstring php-redis
	b. sudo systemctl enable --now php-fpm
	c. sudo nano /etc/php-fpm.d/www.conf
	d. change user (line 24) and group (line 26) to nginx - change listen (line 38) to /run/php-fpm/www.sock - uncomment and change listen owner (line 48) and group (line 49) to nginx
	e. sudo chown -R root:nginx /var/lib/php
	f. sudo systemctl restart php-fpm
	g. Add below to Nginx virtual host directive (line 58 on default conf) - sudo nano /etc/nginx/nginx.conf

		server {

	    # . . . other code

        location ~ \.php$ {
            root /usr/share/nginx/html;
            try_files $uri =404;
            fastcgi_pass unix:/run/php-fpm/www.sock;
            fastcgi_index index.php;
            client_max_body_size 2000M;
            fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
            fastcgi_param SCRIPT_NAME $fastcgi_script_name;
            fastcgi_param PATH_INFO $fastcgi_path_info;
            fastcgi_split_path_info ^(.+\.php)(/.+)$;
            include fastcgi_params;
        }

    h. sudo nano /etc/nginx/default.d/php.conf :

	# pass the PHP scripts to FastCGI server
	#
	# See conf.d/php-fpm.conf for socket configuration
	#
	index index.php index.html index.htm;

	location ~ \.(php|phar)(/.*)?$ {
	    fastcgi_split_path_info ^(.+\.(?:php|phar))(/.*)$;

	    fastcgi_intercept_errors on;
	    fastcgi_index  index.php;
	    include        fastcgi_params;
	    fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
	    fastcgi_param  PATH_INFO $fastcgi_path_info;
	    fastcgi_pass   php-fpm;
	}

	i. make sure the configuration doesn't through errors - sudo nginx -t
	j. sudo systemctl restart nginx
	k. sudo chcon -R -t httpd_sys_rw_content_t /usr/share/nginx
    l. sudo setsebool -P httpd_can_network_connect on

https://linuxize.com/post/install-php-7-on-centos-7/

Test: sudo -u nginx nano /usr/share/nginx/html/test.php

<?php
phpinfo();
?>

Access yourserver/test.php and you should see the php server info page.

5. Install Maria DB 5.5.68

	a. sudo yum install mariadb-server
	b. sudo systemctl enable mariadb.service
	c. sudo mysql_secure_installation

Test:

mysql -u root -p
enter mysql root user password
you should see:

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 10
Server version: 5.5.68-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

exit

(mysql error when rebuilding search index packet size reaches 128M - can be monitored by rebuilding with 'sudo -u nginx /support/bin/caUtils rebuild-search-index')

sudo nano /etc/my.cnf

add line for max_allowed_packet=512M
sudo systemctl restart mariadb

6. Install redis 6.0.9

a. sudo yum-config-manager --enable remi
b. sudo yum install redis
c. sudo systemctl start redis
d. sudo systemctl enable redis

test: sudo systemctl status redis

7. Install plugins

a. sudo yum install GraphicsMagick-devel ghostscript-devel ffmpeg ffmpeg-devel libreoffice dcraw mediainfo perl-Image-ExifTool xpdf

8. Set up php.ini for collectiveaccess

	a. sudo nano /etc/php.ini (you can use ctrl+shift+_ to specify what line to jump to)

#Line 409
memory_limit = 256M
#Line 482
display_errors=On 
#Line 694
post_max_size = 1000M
#Line 846
upload_max_filesize = 1000M

	b. sudo systemctl restart php-fpm

9. Install phpmyadmin 4.9.7

	a. cd ~
	b. curl https://files.phpmyadmin.net/phpMyAdmin/4.9.7/phpMyAdmin-4.9.7-all-languages.tar.gz | tar xzv
	c. sudo mv phpMyAdmin-4.9.7-all-languages /usr/share/nginx/html/phpmyadmin
	d. sudo cp -pr /usr/share/nginx/html/phpmyadmin/config.sample.inc.php /usr/share/nginx/html/phpmyadmin/config.inc.php
	e. sudo nano /usr/share/nginx/html/phpmyadmin/config.inc.php

Update line 17 with blowfish secret: $cfg['blowfish_secret'] = '[ get random code from https://phpsolved.com/phpmyadmin-blowfish-secret-generator/?g=[insert_php]echo%20$code;[/insert_php] ]';

	f. mysql < /usr/share/nginx/html/phpmyadmin/sql/create_tables.sql -u root -p
	enter mysql root user password
	g. sudo nano /etc/nginx/nginx.conf
	
Add line 50-54:

        # phpMyAdmin:
        location /phpmyadmin {
            root /usr/share/nginx/html;
            index index.php;
        }

 	h. ctrl-x, y, enter to exit nano
	i. make sure the configuration doesn't through errors - sudo nginx -t

	i. sudo mkdir /usr/share/nginx/html/phpmyadmin/tmp
	j. sudo chmod 777 /usr/share/nginx/html/phpmyadmin/tmp
	k. sudo chown -R nginx:nginx /usr/share/nginx/html/phpmyadmin
	l. sudo chcon -R -t httpd_sys_rw_content_t /usr/share/nginx/html/phpmyadmin
	n. sudo systemctl restart nginx 
	o. sudo systemctl restart php-fpm 

Test:

open http://yourserver/phpmyadmin in a browser on another machine.

https://www.itzgeek.com/how-tos/linux/centos-how-tos/install-phpmyadmin-with-nginx-on-rhel-8.html (modified)
https://phpsolved.com/phpmyadmin-blowfish-secret-generator/?g=5cecac771c51c

10. Prepare database for collectiveaccess

	a. log in to phpmyadmin - username: root password: [yourrootpassword]
	b. click databases at the top of the main interface on the right
	c. choose a database name - for this log using 'providence' (without the quotes)
	d. to the right of the name choose the formatting type - i chose utf8_general_ci under the utf8 category - not sure if there's something better
	e. click create
	f. at the top of the main interface click 'privileges'
	g. click "add user account"
	h. choose a username - for this log using providence - and create a strong password. not sure if some characters like ' can cause issues later on. you can leave all other settings at default - (might want to doublcheck that Grant all privileges on database providence is checked - it should be by default). scroll down and click go in the bottom right.

11. Install git and download providence

	a. sudo yum install git
	b. cd /usr/share/nginx/html
	c. sudo git clone https://github.com/collectiveaccess/providence.git providence
	c. sudo chown -R nginx:nginx providence
	d. sudo cp -pr /usr/share/nginx/html/providence/setup.php-dist /usr/share/nginx/html/providence/setup.php
	e. sudo nano /usr/share/nginx/html/providence/setup.php

Line 38: set user to providence
Line 44: set password
Line 50: set DB name
Line 58: set site name
Line 65: set admin email
Line 83: set time zone
Line 218: stacktrace enable for development

9. Setup nginx conf for providence

	a. sudo nano /etc/nginx/nginx.conf

add lines 56 - 60

        # providence:
        location /providence {
            root /usr/share/nginx/html;
            index index.php;
        }

    b. sudo nginx -t
    c. sudo systemctl restart nginx

10. Install CollectiveAccess

Appendix. Plug-ins

a. Manage->Administration
b. Configuration Check on the left
c. everything will show 'Not available' on first load for some reason. refresh the page.

11. wkhtmltopdf (0.12.1 is the latest working version with ca)

sudo yum install icu xorg-x11-fonts-75dpi

cd ~
wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.1/wkhtmltox-0.12.1_linux-centos7-amd64.rpm
sudo yum install wkhtmltox-0.12.1_linux-centos7-amd64.rpm
rm *.rpm

https://www.interserver.net/tips/kb/how-to-install-wkhtmltopdf-on-centos-and-ubuntu-server/

RHEL/CentOS 8
---------------------------------

yum -y install mariadb-server
dnf -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
dnf -y install https://rpms.remirepo.net/enterprise/remi-release-8.rpm
dnf -y install yum-utils
dnf config-manager --set-enabled remi
dnf -y install redis httpd mod_ssl
dnf -y module install php:remi-7.3 
dnf -y install git screen
dnf -y install php-cli php-gd php-curl php-mysqlnd php-zip php-fileinfo php-gmagick php-opcache php-process php-xml php-mbstring php-redis redis

dnf -y install ghostscript 

dnf install --nogpgcheck https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
dnf install --nogpgcheck https://download1.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-8.noarch.rpm
dnf config-manager --enable PowerTools

dnf -y install ffmpeg

firewall-cmd --zone=public --add-service=http  --permanent
firewall-cmd --zone=public --add-service=https  --permanent
firewall-cmd --reload

systemctl enable mariadb
systemctl start mariadb
systemctl enable httpd
systemctl start httpd
