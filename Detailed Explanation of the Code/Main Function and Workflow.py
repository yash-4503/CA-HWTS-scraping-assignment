# Purpose:
# This section ties together all functions: loading data, setting up Selenium, iterating through EPA_IDs, scraping details, and saving the results.

def main():
    # Load EPA_IDs from CSV files
    active_epa_ids = load_epa_ids("active_facilities.csv")
    inactive_epa_ids = load_epa_ids("inactive_facilities.csv")
    
    # Combine and deduplicate EPA_IDs
    all_epa_ids = list(set(active_epa_ids + inactive_epa_ids))
    logging.info(f"Total EPA_IDs to process: {len(all_epa_ids)}")
    
    # Set up Selenium Chrome driver in headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), 
        options=chrome_options
    )
    
    scraped_data = []
    for idx, epa_id in enumerate(all_epa_ids, start=1):
        logging.info(f"Processing {idx}/{len(all_epa_ids)}: EPA_ID {epa_id}")
        details = scrape_facility_details(driver, epa_id)
        if details:
            scraped_data.append(details)
        # Pause briefly to avoid overwhelming the server
        time.sleep(1)
    
    # Close the Selenium driver
    driver.quit()
    
    # Save the scraped data to a CSV file
    if scraped_data:
        df_output = pd.DataFrame(scraped_data)
        output_file = "hwts_facilities_output.csv"
        df_output.to_csv(output_file, index=False)
        logging.info(f"Scraping completed. Output saved to {output_file}")
    else:
        logging.info("No data scraped. Please check for errors.")

if __name__ == "__main__":
    main()


# Explanation:

# Loading Data:
# The script loads EPA_IDs from both active and inactive CSV files and combines them into one unique list.

# Selenium Setup:
# Selenium is configured to use Chrome in headless mode. This means the browser runs in the background without a visible window, which is efficient for scraping.

# Iteration and Scraping:
# The script loops through each EPA_ID, scrapes the facility details using the earlier defined function, and appends successful results to a list. A brief pause is added between requests to reduce server load.

# Output:
# After processing all EPA_IDs, the Selenium driver is closed and the scraped data is saved into a CSV file.

