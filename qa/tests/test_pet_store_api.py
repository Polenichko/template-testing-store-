import pytest
import os
import logging
import httpx


URL = os.getenv("URL_PET_STORE_API") 


def test_positive_post(setup_sum_for_test):
    
    setup_sum_for_test.write("test")

    data = {
        'some_data': 'example'
                }
    
    response = httpx.post(f'{URL}/some_locator', json=data)
    logging.info("create some record")
    assert response.status_code == 201, "record not create"
    assert response.json()['some_data'] == 'example', "record dont have correct data"


def test_negative_post():
    
    data = {
        'some_data': b'sum_wrong_type!'
                }
    
    response = httpx.post(f'{URL}/some_locator', json=data)
    assert response.status_code == 200
    assert "Error: wrong_type for some_data" in response.text


def test_positive_get():
    data = {
        'some_data': 'example'
                }
    
    create_response = httpx.post(f'{URL}/some_locator', json=data)
    logging.info("create some record")

    id = create_response.json()['id']
    response = httpx.get(f'{URL}/some_locator/{id}')
    logging.info("get exist record")
    assert response.status_code == 200
    assert "example" in response.text


def test_negative_get():
    id = "not exist data"
    response = httpx.get(f'{URL}/some_locator/{id}')
    assert response.status_code == 404
    assert "not exist data" in response.text


def test_positive_delete():
    data = {
        'some_data': 'example'
              }
    create_response = httpx.post(f'{URL}/some_locator', json=data)
    assert create_response.status_code == 200
    logging.info("create some record")

    id = create_response.json()['id']
    delete_url = f'{URL}/some_locator/{id}'
    delete_response = httpx.delete(delete_url)
    logging.info("delete exist record")
    assert delete_response.status_code == 200

    get_response = httpx.get(delete_url)
    logging.info("check record not exist")
    assert get_response.status_code == 404, f"record:{id}, shold be not exist"

def test_negative_delete():
   
    id = "not exist id"
    delete_url = f'{URL}/some_locator/{id}'
    delete_response = httpx.delete(delete_url)
    
    assert delete_response.status_code == 404, f"record:{id}, shold be not exist"