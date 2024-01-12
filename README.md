# Setup

1. Download python virtual environment  
   ```pip install virtualenv```
1. Create a virtual env  
   ```virtualenv dev```  
   1. if powershell gives trouble, use the following command
      ```Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process```  
1. Install dependencies with pip  
   ```pip install -r requirements.txt```
1. Docker-compose up the mongodb
   ```docker-compose up -d```
1. Debug run.py   

# Deploy 
1. git push azure develop