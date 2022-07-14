import requests

from fastapi import FastAPI
from fastapi import Path
from fastapi import HTTPException
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
        response = requests.get(f'https://cat-fact.herokuapp.com/facts/random?amount={fact_amount}', timeout=30)

        # It filters the facts only by the current year.
        current_year = str(datetime.today().year)
        facts_filtered_by_date = [
            fact for fact in response.json() if fact['updatedAt'][:4] == current_year
        ]
        return facts_filtered_by_date
    except Timeout:
        raise HTTPException(status_code=404, detail="Cat API request timed out")
