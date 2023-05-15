import pytest
import logging
import time
import os

@pytest.fixture(scope="session",autouse=True)
def _set_logging():    
    logfile = os.getenv("LOG_FILENAME")
    logging.basicConfig(
        format="%(asctime)s-%(levelname)s-%(name)s-%(message)s",
        filename=f'qa/logs/{logfile}.log', 
        level=logging.INFO,
        filemode="w"
    )

@pytest.fixture(scope="function",autouse=True)
def setup_sum_for_test():
    print("for example!")
   