## TASK 1

We want to prevent any user from accessing http://example.com and if someone access it, they should be redirected to https://example.com

We did that by changing the default configuration file of the webserver. We added the following lines to the default configuration file of the webserver.

```bash
sudo nano /etc/apache2/sites-available/example.com.conf
```

```bash
<VirtualHost *:80>
ServerAdmin admin@example.com
ServerName example.com
ServerAlias www.example.com
DocumentRoot /var/www/example.com/html
ErrorLog ${APACHE_LOG_DIR}/error.log
CustomLog ${APACHE_LOG_DIR}/access.log combined

RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{SERVER_NAME}/$1 [R,L]

</VirtualHost>

```

## TASK 2

Now we want to implement authentication for the website using apache

We did that by changing the default configuration file of the webserver. We added the following lines to the default configuration file of the webserver.

```bash
sudo nano /etc/apache2/sites-available/example.com.conf
```

```bash
   <Directory "/var/www/html">
        AuthType Basic
        AuthName "Restricted Content"
        AuthUserFile /etc/apache2/.htpasswd
        Require valid-user
    </Directory>
```

```bash
sudo htpasswd -c /etc/apache2/.htpasswd shawon
```

Now we can access the website by using the username and password.

## TASK 3

Now we will implement more advanced authentication for the website using apache & MySQL

We did that by changing the default configuration file of the webserver. We added the following lines to the default configuration file of the webserver.

```bash
sudo nano /etc/apache2/sites-available/example.com.conf
```

```bash
    DBDriver mysql
    DBDParams "dbname=apache user=root pass=cse"
    DBDMin 4
    DBDKeep 8
    DBDMax 20
    DBDExptime 300
    <Directory "/var/www/example.com/html">
        AuthType Basic
        AuthName "My Server"
        AuthBasicProvider socache dbd
        AuthnCacheProvideFor dbd
        AuthnCacheContext my-server
        Require valid-user
        AuthDBDUserPWQuery "SELECT password FROM users WHERE username = %s"
    </Directory>
```

After setting username and password in the MySQL database, we can access the website by using the username and password.

### Screenshots

1. http to https redirection
   ![image](./Screenshots/1%20http%20to%20https%20redirection.png)
2. Adding user and password
   ![image](./Screenshots/2%20Adding%20user%20and%20password.png)
3. List of users and their hashed password
   ![image](./Screenshots/3%20List%20of%20users%20and%20their%20hashed%20password.png)
4. Asking for authentication
   ![image](./Screenshots/4%20Asking%20for%20authentication.jpeg)
5. Providing Wrong Credential
   ![image](./Screenshots/5%20Providing%20Wrong%20Credential.jpeg)
6. Providing Correct Credential
   ![image](./Screenshots/6%20MySQL%20Secure%20Installation.png)
7. MySQL Running
   ![image](./Screenshots/7%20MySQL%20Running.png)
8. MySQL Authentication
   ![image](./Screenshots/8%20MySQL%20Authentication.png)
