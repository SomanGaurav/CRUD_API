# The following file is the rest report of the api testing represented in pictorial form 

## Test cases 

- Request to api to list all the user in database
  Route = /user , method = get 
  ![image](https://github.com/user-attachments/assets/5565c7d5-5e35-4732-9f7c-cd98dc86f588)
- Request to api to create a new user
  Route = /user , method = post , form_params = {username , email , password}
  ![image](https://github.com/user-attachments/assets/1c9c480e-4d57-4705-8ae8-22fb65552980)
- Request to api to get info on a specific user
  Route = /user/<id> , method = get
  ![image](https://github.com/user-attachments/assets/a5a6f334-1402-469f-aad7-4f7155c9d977)
- Request to api to update info of a specific user
  Route = /user/<id> , method = put , form_params=> Any of the user attributes
  ![image](https://github.com/user-attachments/assets/fe30d150-4ce3-4240-883c-9b773d509087)
- Request to api to delete a specific user
  Route = /user/<id> , method = delete
  DB before user deletion
  ![image](https://github.com/user-attachments/assets/cb305d67-cdc0-4b96-a9ad-f807b9a80f3b)
  DB after deletion
  ![image](https://github.com/user-attachments/assets/a72c9c9b-ed96-4b0e-9432-33071b26d3c8)
  ![image](https://github.com/user-attachments/assets/ff973eb6-1358-4db5-a35d-a27636b8f46a)

