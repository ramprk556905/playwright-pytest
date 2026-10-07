# import os
# import re
# import sys
# from collections.abc import Generator
# from pathlib import Path


# import pytest
# from playwright.sync_api import Playwright
# from dotenv import load_dotenv

# def pytest_addoption(parser):
#     parser.addoption(INPUT_DATA,
#                      action = 'store',
#                      default = rf'{os.getcwd()}\test_input_data.yml',
#                      help='Specify the location of the YAML file from which to read input data')
    

# @pytest.fixture(scope='function')
# def setup(playwright:Playwright):
#     browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
#     page = browser.new_page(no_viewport=True)
#     page.set_default_timeout(50000)
#     page.goto('')
#     yield page
#     browser.close()