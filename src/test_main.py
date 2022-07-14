from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_show_cat_facts():
    response = client.get("/cat-facts/1")
    assert response.status_code == 200

def test_cat_facts_bigger_amount():
    response = client.get("/cat-facts/501")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": [
                    "path",
                    "fact_amount"
                ],
                "msg": "ensure this value is less than or equal to 500",
                "type": "value_error.number.not_le",
                "ctx": {
                    "limit_value": 500
                }
            }
        ]
    }

def test_cat_facts_lower_amount():
    response = client.get("/cat-facts/0")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": [
                    "path",
                    "fact_amount"
                ],
                "msg": "ensure this value is greater than 0",
                "type": "value_error.number.not_gt",
                "ctx": {
                    "limit_value": 0
                }
            }
        ]
    }
