##Purpose:
##To load and combine EPA_IDs from two separate CSV files (active_facilities.csv and inactive_facilities.csv).

def load_epa_ids(file_path):
    try:
        df = pd.read_csv(file_path)
        epa_ids = df['EPA_ID'].drop_duplicates().tolist()
        logging.info(f"Loaded {len(epa_ids)} EPA_IDs from {file_path}")
        return epa_ids
    except Exception as e:
        logging.error(f"Error loading EPA_IDs from {file_path}: {e}")
        return []
##Explanation:
##The function load_epa_ids reads the CSV file using Pandas, removes duplicate entries, and converts the EPA_ID column into a Python list. It logs the success or failure of this operation.
