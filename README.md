# Cat-API
API made in Python using FastAPI, it returns cat facts!
Who doesn´t love cats?
![Cute Cat](https://www.pexels.com/photo/white-and-grey-kitten-on-brown-and-black-leopard-print-textile-45201/)
## Deploy app in docker
Lets start by creating the image, enter the project folder and execute the following command in terminal:
docker build -t cat_api .

Then lets run the app:
run -d -p 8080:8080 --name cat_api cat_api

To view the API Documentation, enter the following link in your web browser:
http://localhost:8080/docs
