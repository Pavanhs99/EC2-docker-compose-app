
# Multi service docker flask project

   - A simple DevOps project where a Flask web app communicates with a Bash script through a shared Docker volume. Built using Docker Compose and deployed on AWS EC2.
 
----

# Live Deployment
  
   - **EC2 Public IP**: http://13.201.190.160:5000  

   > *Note: The server may take a few seconds to respond if it's waking from sleep.*

----

# Highlights

   - Flask web interface running in one container

   - Bash script running in another container

   - Shared volume for inter-container communication

   - Logs stored in a persistent volume

   - Docker Compose to manage services

   - Deployed on AWS EC2 (Ubuntu)

----

# Tech Stack

   - Python (Flask)

   - Bash Scripting

   - Docker & Docker Compose

   - AWS EC2 (Ubuntu)

   - Linux

----

## How to run

  - git clone https://github.com/yourname/project.git

  - cd project

  - docker-compose up --build

----

# Project structure

```
   flask-final/
           |
           |__scripts/
                   |___system_info.sh
           |
           |       |___logger.sh
           |
           |       |___dockerfile
           |
           |__flask/
                   |___app.py
           |
           |       |___requirements.txt
           |
           |       |___dockerfile
           |
           |__shared_vol/    #(auto created via docker volume, excluded grom git)                                                                                                                                                                                                                                                                                                                                                                                                                                  ## How to run                                                                                                                                                                                                                                                                                                                                                                                                                         ```bash                                                                                                                                                                                                            bash scripts/system_info.sh                                                                                                                                                                                        ```                                                                                                                                                                                                                ```bash                                                                                                                                                                                                            bash scripts/logger.sh                                                                                                                                                                                             ```                                                                                                                                                                                                                ```python                                                                                                                                                                                                          python flask/app.py                                                                                                                                                                                                ```                                                                                                                                                                                                                ```bash                                                                                                                                                                                                            bash docker-compose.yml                                                                                                                                                     

           |__docker-compose.yml
           |
           |__README.md
           |
           |__.gitignore
```

----

# What i learned

   - How to create multi-container setups using Docker Compose

   - Sharing data between containers using volumes

   - Running Bash and Python services in isolation

   - Real-world EC2 deployment

   - Logging strategies using volumes

----

## Architecture Diagram

![Architecture Diagram](flask-final.drawio.png)
