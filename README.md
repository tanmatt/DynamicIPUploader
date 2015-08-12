#dynamic_IP_notifier
Most of my cronjobs run on a server.
The server doesn't have a static IP (I don't want to spend money on it.)
Yet, I need to know the public IP to ssh into it. 
This program solves the problem of changing IP by sending text message with new IP. 

Just put your cell number in the script and you are ready to use the script. 
I have created a cronjob to run this script every hour and if there is IP change, I will get a text message.
-----------

### Installation steps
1. ssh to the server for which you want to know the IP.
2. select a directory to copy the source code.
3. move to the directory.
4. get the source code from github
  ```git clone https://github.com/tanmaythakur/dynamic_IP_notifier.git ```
5. you need to install `requests` python package.
  ``` pip install requests``` 

### Configuration
1. The changed IP is sent via a text message. You will need to enter it in this section. 
2. Move to the source code directory
   ``` cd dynamic_IP_notifier```
3. Open `notifier.py` file and change `cell_number` to your number.
4. Copy the PATH of notifier.py file.
5. Create a cron job to get hourly and reboot notifications.
```  crontab -e```
``` 0 * * * * cd /PATH/TO/dynamic_IP_notifier && /usr/local/bin/python2.7 notifier.py
@reboot cd /PATH/TO/dynamic_IP_notifier && /usr/local/bin/python2.7 notifier.py```
Save an quit.

### Testing
1. Make sure `current_IP` file has no content.
2. Execute the notifier script (after you have followed Configuration steps)
   ``` python2.7 notifier.py```
3. Expected result - text message with IP address
 
