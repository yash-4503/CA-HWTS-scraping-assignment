# CA-HWTS-scraping-assignment

Overview
This document explains the CA HWTS scraping assignment. The goal of the assignment is to:

Download Facility Data:
Retrieve two CSV files (active and inactive facilities) that contain EPA_IDs from the provided URLs.

Scrape Facility Details:
For each EPA_ID, construct a URL of the format https://hwts.dtsc.ca.gov/facility/<EPA_ID>, dynamically load the page using Selenium in headless mode, and extract key facility information (e.g., Facility Name and Address).

Output the Data:
Combine the results and export them to an output CSV file.

This solution is implemented in Python using Selenium, along with supporting libraries such as Pandas and webdriver-manager.
