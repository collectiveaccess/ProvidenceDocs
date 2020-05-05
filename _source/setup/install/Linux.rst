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

Packages:

yum -y install yum-utils mariadb-server ghostscript  ghostscript-devel

yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
yum -y install http://rpms.remirepo.net/enterprise/remi-release-7.rpm
yum -y install GraphicsMagick-devel

yum -y install httpd
yum-config-manager --enable remi-php73
yum -y install php php-mcrypt php-cli php-gd php-curl php-mysqlnd php-zip php-fileinfo php-devel php-gmagick php-opcache php-process php-xml php-mbstring php-redis redis

rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
yum -y install ffmpeg ffmpeg-devel 


yum -y install xpdf dcraw mediainfo git screen wkhtmltopdf
yum -y install mod_ssl openssl

systemctl enable mariadb
systemctl start  mariadb
systemctl enable httpd
systemctl start  httpd
systemctl enable redis
systemctl start  redis

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
