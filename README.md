# Cat-API
API made in Python using FastAPI, it returns cat facts!, Come on, who doesn´t love cats? :heart:
## Deploy app in docker
Lets start by creating the image, clone the github repository and then enter the project folder and execute the following command in terminal:

```console
docker build -t cat_api .
```

Then lets run the app:
```console
run -d -p 8080:8080 --name cat_api cat_api
```

To view the API Documentation, enter the following link in your web browser:
http://localhost:8080/docs

## Deploy on localhost
Clone the github repository, then lets a virtualenv in the folder directory to install requirements("pip install virtualenv" if you dont have it.)

Create and virtualenv:
```console
virtualenv venv
```

Lets install requierements:
```console
pip install -r requirements.txt
```

Activate venv:
```console
.\venv\Scripts\activate
```

Run project using uvicorn:
```console
cd .\src\
uvicorn main:app --reload
```


To view the API Documentation, enter the following link in your web browser:
http://localhost:8080/docs