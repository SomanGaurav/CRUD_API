# Flask with NGINX MONGODB and Docker 

This project is implementation of a simple **Flask** based crud api that runs behind a **nginx reverse proxy** using **Docker and Docker-Compose** .

## Pre-requisite 
Before we begin we have to make sure that 
- Docker
is installed properly on the system

## Installation 
- Start by cloning the git repoistory using the repo link :- "https://github.com/SomanGaurav/CRUD_API.git"
- Change the working directory to the project directory :- cd CRUD_API
- Build the docker containers using :- docker-compose up --build
- To test if containers are running properly send a request to :- http://localhost
  The response will be **Hello World**

  What happens is nginx is running on port 80 that forwards all the requests to the flask server . It acts like a load balancer , when there is huge amount of traffic on the server we can run multiple instaces of the container . The nginx server will help in distributing the requests among many instances . This is called **Horizontal Scaling**
- For closing the application use :- docker-compose down
  
## API-ENDPOINTS 
- API TESTING :- localhost 
- GET LIST OF USERS :- localhost/user
- GET specific USER :- localhost/user/<id>
- update specific USER :- localhost/user/<id>  PUT request alongside form data
- Create a USER :- localhost/user POST request alongside form data
- Delte a user :- localhost/user/<id> Delete request 
