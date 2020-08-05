//最近出现无法访问githubraw文件的情况，解决办法如下：

/*****linux系统********/
sudo nano /etc/hosts
//在https://ping.chinaz.com/里ping raw.githubusercontent.com ，出现日本、香港等服务器IP地址，此处选择香港的151.101.76.133为例，修改hosts文件，加入：
151.101.76.133  raw.githubusercontent.com
151.101.76.133  raw.github.com
//关闭文件即可

/*******windows系统********/
//修改C:\Windows\System32\drivers\etc的hosts文件，注意该文件无法在当前路径下修改，需要拷贝出来修改，
//修改以后，将原文件删除，然后将修改后的文件拷贝进来，修改方法和linux系统相同
