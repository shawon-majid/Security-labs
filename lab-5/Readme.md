## Secure SSL / TLS (HTTPS)

We have created a secure socker layer for example.com and webserverlab.com

Here webserverlab.com & example.com both points to localhost. But example.com uses our own HTML file located in /var/www/example.com/index.html and webserverlab.com uses the default index.html file located in /var/www/html/index.html

We have secured the website by becoming Root CA and then Issuing certificate to example.com and localhost

These are the screenshots of the website:

1. Setup firewall
   ![Firewall](./Screen%20Shots/1%20Setup%20firewall.png)

2. Started Apache
   ![Apache](./Screen%20Shots//2%20Started%20Apache%20Web%20Server.png)

3. Unsecured example.com
   ![Unsecured example.com](./Screen%20Shots/3%20unsecured%20example.com.png

4. Becoming RootCA
   ![RootCA](./Screen%20Shots/6%20Becoming%20RootCA.png)

5. Certificate Request for example.com
   ![Issuing certificate to example.com](./Screen%20Shots/7%20Certificate%20Request.png)

6. Issuing certificate to example.com
   ![Issuing certificate to example.com](./Screen%20Shots/8%20Certificate%20Issue%20.png)

7. Secured example.com
   ![Secured example.com](./Screen%20Shots/9%20Secure%20Example.com.png)

8. Certificate Information
   ![Certificate Information](./Screen%20Shots/10%20Certificate%20Info.png)

9. Certificate in Firefox
   ![Certificate in Firefox](./Screen%20Shots//11%20Certificate%20in%20Firefox.png)
