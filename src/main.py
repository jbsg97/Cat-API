import requests

from fastapi import(
    FastAPI, 
    Path, 
    HTTPException,
)
from typing import List
from datetime import datetime
from requests.exceptions import Timeout

from schemas.facts_schema import CatResponse


app = FastAPI()

@app.get("/cat-facts/{fact_amount}", response_model=List[CatResponse])
async def show_cat_facts(
    fact_amount: int = Path(title="Amount of facts to retrieve", gt=0, le=500)
):
    try:
        #response = requests.get('https://cat-fact.herokuapp.com/facts/random?amount={fact_amount}', timeout=5)
        response_example = [
            {
                "_id": "591f9894d369931519ce358f",
                "__v": 0,
                "text": "A female cat will be pregnant for approximately 9 weeks - between 62 and 65 days from conception to delivery.",
                "updatedAt": "2018-01-04T01:10:54.673Z",
                "deleted": False,
                "source": "api",
                "sentCount": 5
            },
            {
                "_id": "591f9854c5cbe314f7a7ad34",
                "__v": 0,
                "text": "It has been scientifically proven that stroking a cat can lower one's blood pressure.",
                "updatedAt": "2018-01-04T01:10:54.673Z",
                "deleted": False,
                "source": "api",
                "sentCount": 3
            }
        ]

        # It filters the facts only by the current year.
        current_year = datetime.today().year
        facts_filtered_by_date = [
            fact for fact in response_example if fact['updatedAt'][:4] == '2018'
        ]

        return facts_filtered_by_date
    except Timeout:
        raise HTTPException(status_code=404, detail="Cat API request timed out")
