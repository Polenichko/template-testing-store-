import pytest
import os
import logging
import requests


URL = os.getenv("URL_PET_STORE_API") 


def test_template_post():
    data = {
        'some_data': 'example'
                }
    
    response = requests.post(f'{URL}/some_locator', json=data)
    logging.info("create some record")
    assert response.status_code == 200, "record not create"
    assert response.json()['some_data'] == 'example', "record dont have correct data"


def test_template_get():
    data = {
        'some_data': 'example'
                }
    
    create_response = requests.post(f'{URL}/some_locator', json=data)
    logging.info("create some record")

    id = create_response.json()['id']
    response = requests.get(f'{URL}/some_locator/{id}')
    logging.info("get exist record")
    assert response.status_code == 200
    assert "example" in response.text


def test_template_delete():
    data = {
        'some_data': 'example'
              }
    create_response = requests.post(f'{URL}/some_locator', json=data)
    assert create_response.status_code == 200
    logging.info("create some record")

    id = create_response.json()['id']
    delete_url = f'{URL}/some_locator/{id}'
    delete_response = requests.delete(delete_url)
    logging.info("delete exist record")
    assert delete_response.status_code == 200

    get_response = requests.get(delete_url)
    logging.info("check record not exist")
    assert get_response.status_code == 404
