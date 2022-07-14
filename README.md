# Cat-API
API made in Python using FastAPI, it returns cat facts!
Who doesn´t love cats?
![Cute Cat](https://ibb.co/DgFHy0F)
## Deploy app in docker
Lets start by creating the image, enter the project folder and execute the following command in terminal:
docker build -t cat_api .

Then lets run the app:
run -d -p 8080:8080 --name cat_api cat_api

To view the API Documentation, enter the following link in your web browser:
http://localhost:8080/docs
