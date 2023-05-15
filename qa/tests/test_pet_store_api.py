import pytest
import os
import logging
import httpx

import random
import json


URL = os.getenv("URL_PET_STORE_API") 


def test_positive_post():
    
    data = {
        "id": 1,
        "petId": 111,
        "quantity": 1,
        "shipDate": "2023-05-15T14:05:58.400Z",
        "status": "placed",
        "complete": True
        }
    response = httpx.post(f'{URL}', json=data)
    logging.info("create record:{data}")
    assert response.status_code == 200, "record not create!"
    assert response.json()["id"] == data.get("id"), "record dont have correct data"


def test_negative_post():
    
    data = {
        "id": "text",
        "petId": 1,
        "quantity": 1,
        "shipDate": "2023-05-15T14:05:58.400Z",
        "status": "placed",
        "complete": True
                }
    response = httpx.post(f'{URL}', json=data)
    assert response.status_code == 500
    assert "something bad happened" in response.text


def test_positive_get():
    id = 2
    data = {
        "id": id,
        "petId": 111,
        "quantity": 1,
        "shipDate": "2023-05-15T14:05:58.400Z",
        "status": "placed",
        "complete": True
        }
    
    create_response = httpx.post(f'{URL}', json=data)
    logging.info("create some record")

    response = httpx.get(f'{URL}/{id}')
    logging.info("get exist record")
    assert response.status_code == 200
    assert response.json()["id"] == id


def test_negative_get():
    id = 8
    response = httpx.get(f'{URL}/{id}')
    assert response.status_code == 404
    assert "Order not found" in response.text


def test_positive_delete():
    id = 2
    data = {
        "id": id,
        "petId": 111,
        "quantity": 1,
        "shipDate": "2023-05-15T14:05:58.400Z",
        "status": "placed",
        "complete": True
        }
    create_response = httpx.post(f'{URL}', json=data)
    assert create_response.status_code == 200
    logging.info("create some record")

    id = create_response.json()['id']
    delete_url = f'{URL}/{id}'
    delete_response = httpx.delete(delete_url)
    logging.info("delete exist record")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == str(id)

    get_response = httpx.get(delete_url)
    logging.info("check record not exist")
    assert get_response.status_code == 404, f"record:{id}, shold be not exist"

def test_negative_delete():
   
    id = "2"
    delete_url = f'{URL}/{id}'
    delete_response = httpx.delete(delete_url)
    
    assert delete_response.status_code == 404, f"record:{id}, shold be not exist"