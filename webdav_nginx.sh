#step1:安装依赖
sudo apt install nginx nginx-extras

#step2:配置nginx
mkdir /home/webdav
mkdir /home/webdavpsd

nano /etc/nginx/sites-available/webdav  #添加以下内容
server {
    listen       8080; # 端口
    server_name  webdav.Your_domain; #域名
    root /home/webdav; # 根目录
    client_body_temp_path /home/webdav/tmp;
    access_log  /home/webdav_access.log;
    error_log   /home/webdav_error.log;
    location / {
      auth_basic "Not currently available";
      auth_basic_user_file /home/webdavpsd/.htpasswd; # htpasswd验证文件

      dav_methods PUT DELETE MKCOL COPY MOVE;
      dav_ext_methods PROPFIND OPTIONS;

      create_full_put_path on;
      dav_access user:rw group:r;

      autoindex on; # 可以在浏览器打开

      #limit_except GET {
      #  allow 115.115.0.0/32; # 允许访问的IP段，可以填自己家的IP，这样就只有你家的IP可以访问，大大增加安全性。
      #  deny  all;
      }
   }
}

#step3:创建密码
cd /home/webdavpsd  #切换到root账号
printf "user:$(openssl passwd -crypt 123456)\n" >>.htpasswd #分别替换user以及123456

#重启nginx
nginx -s reload

#win10挂载
regedit #修改注册表
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WebClient\Parameters\BasicAuthLevel  #值修改为2
