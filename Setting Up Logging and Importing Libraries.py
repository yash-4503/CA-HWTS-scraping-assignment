##Purpose:
##To initialize logging (for tracking progress and errors) and import necessary modules such as pandas for data handling, selenium for web automation, and webdriver_manager to manage the ChromeDriver automatically.

import time
import logging
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)

Explanation:
This block sets up logging to print timestamps, log levels, and messages. It also imports all the libraries that will be used throughout the script.
