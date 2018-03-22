#Dynamic IP Uploader

## The problem
Most of my cronjobs run on a server.
The server doesn't have a static IP (I don't want to spend money on it.)
Yet, I need to know the public IP to ssh/ VNC into it. 

### The solution
This program solves the problem of changing IP by sending text message with new IP. 
Just follow the installation steps below (5 min).
-----------

### Installation steps
- Fork it
- Pull the repo down locally on the host you want to know the IP using 
  - `git clone https://github.com/{YOUR_USERNAME}/DynamicIPUploader.git` 
- You might need to install `requests` python package.
  -  `pip install requests` 
- Setup a crontab 
  -  `crontab -e`  
  -  `@hourly cd {path/of/the/repo} && python IPUploader.py`
 - Go to github and Star this repo


### Testing
* Make sure `current_IP` file has no content, delete everything inside it otherwise.
* Execute once to confirm there are no errors
   ``` python2.7 IPUploader.py```
* Confirm `current_IP` has your publicIP and is uploaded on github.
 
