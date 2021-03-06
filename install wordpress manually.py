#Step I install LEMP environm
sudo apt update
sudo apt upgrade

sudo apt install nginx mysql-server php7.0-cli php7.0-cgi php7.0-fpm php7.0-mbstring php7.0-curl php7.0-gd php7.0-mysql php7.0-xml
sudo apt install unzip


#Step II download wordpress file
cd /tmp
sudo wget https://wordpress.org/latest.tar.gz
sudo tar xzvf latest.tar.gz
sudo cp -a /tmp/wordpress/. /var/www/wordpress


#Step III creat mysql and config
sudo mysql -u root -p       #login mysql
CREATE DATABASE wordpress;
CREATE USER 'usename'@'localhost' IDENTIFIED BY 'passwd';
GRANT ALL PRIVILEGES ON wordpress.* TO 'joey'@'localhost';
FLUSH PRIVILEGES;
EXIT


#Step IV config nginx
sudo touch /etc/nginx/sites-available/wordpress
sudo nano /etc/nginx/sites-available/wordpress
#server {
#    listen 80;
#    listen [::]:80;
#
#    server_name example.com;
#
#    root   /var/www/example;
#    index  index.html index.php;
#
#    location / {
#        try_files $uri $uri/ =404;
#    }
#    location ~ \.php$ {
#            include snippets/fastcgi-php.conf;
#            include fastcgi_params;
#            fastcgi_pass unix:/run/php/php7.0-fpm.sock;
#            fastcgi_param SCRIPT_FILENAME /var/www/example$fastcgi_script_name;
#    }
#}
sudo ln -s /etc/nginx/sites-available/wordpress /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart php7.0-fpm nginx


#Step V config wordpress
sudo cp /var/www/wordpress/wp-config-sample.php /var/www/wordpress/wp-config.php
sudo chown -R www-data:www-data /var/www/wordpress
curl -s https://api.wordpress.org/secret-key/1.1/salt/
sudo nano /var/www/wordpress/wp-config.php
#define('DB_NAME', 'wordpress');
#/** MySQL database username */
#define('DB_USER', 'wordpressuser');
#/** MySQL database password */
#define('DB_PASSWORD', 'passwd');
#. . .
#define('FS_METHOD', 'direct');     #add this line


#####it's done! you can continue by the webexplorer


##################other command

mysql_secure_installation       #inistialize the mysql

nano /etc/nginx/nginx.conf      #edit nginx to allow upload bigger file size
#add this
#http{
#    ...
#    client_max_body_size 20m;
#    ...
#    }

sudo find / -name 'php.ini'     #find php.ini file and edit the upload block to allow big file size


