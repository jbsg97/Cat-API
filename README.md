# Cat-API
API made in Python using FastAPI, it returns cat facts!, Come on, who doesn´t love cats? :heart:
## Deploy app in docker
Lets start by creating the image, enter the project folder and execute the following command in terminal:

```console
$ docker build -t cat_api .
```

Then lets run the app:
```console
$ run -d -p 8080:8080 --name cat_api cat_api
```


To view the API Documentation, enter the following link in your web browser:
http://localhost:8080/docs
