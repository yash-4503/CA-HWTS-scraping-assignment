##Purpose:
##For each EPA_ID, the script constructs the URL, loads the webpage using Selenium in headless mode, waits for the required elements to appear, and extracts the facility name and address.

def scrape_facility_details(driver, epa_id):
    url = f"https://hwts.dtsc.ca.gov/facility/{epa_id}"
    try:
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        
        # Wait for the facility title to be present
        facility_name_element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h1.facility-title"))
        )
        facility_name = facility_name_element.text.strip()

        # Locate the facility address
        address_element = driver.find_element(By.CSS_SELECTOR, "div.facility-address")
        address = address_element.text.strip()

        logging.info(f"Successfully scraped EPA_ID {epa_id}")
        return {
            "EPA_ID": epa_id,
            "Facility_Name": facility_name,
            "Address": address,
            "URL": url
        }
    except Exception as e:
        logging.error(f"Error fetching details for EPA_ID {epa_id} at {url}: {e}")
        return None

# Explanation:
# This function performs the core scraping. It:

# Constructs the URL based on the EPA_ID.

# Uses Selenium’s driver.get() to load the page.

# Waits until the facility title element (assumed to be an h1 tag with class facility-title) appears.

# Extracts the text for both the facility name and address.

# Logs the successful scrape or any error that occurs.

# Note:
# The CSS selectors (h1.facility-title and div.facility-address) are based on assumptions from the provided sample. They can be adjusted if the actual HTML structure differs.
