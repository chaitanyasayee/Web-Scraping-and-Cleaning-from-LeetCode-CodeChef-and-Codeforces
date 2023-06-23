# Web Scraping and Cleaning from LeetCode, CodeChef, and Codeforces

This project involves web scraping and cleaning data from LeetCode, CodeChef, and Codeforces websites. The goal is to extract problem links and relevant information from these platforms for further analysis.

## Prerequisites
- Python 3.x
- Selenium library
- BeautifulSoup library
- ChromeDriver

## Instructions

1. Install the required packages by running the following command:
   ```
   pip install selenium beautifulsoup4 webdriver_manager
   ```

2. Download the ChromeDriver executable appropriate for your operating system and Chrome browser version. Make sure to place it in the same directory as the Python script.

3. Update the ChromeDriver path in the script if necessary.

4. Run the script by executing the following command:
   ```
   python script_name.py
   ```

5. The script will scrape the desired web pages and save the extracted data into separate text files.

## LeetCode Scraping and Cleaning (script: leetcode_scraping.py)

This script scrapes problem links from a file named `lc.txt` and cleans the links by removing any unwanted patterns. The cleaned links are then saved in the `lc_problems.txt` file.

## CodeChef Scraping and Cleaning (script: codechef_scraping.py)

This script scrapes problem links from the CodeChef website and saves them in the `cc.txt` file. It then cleans the links by removing unwanted patterns and saves the cleaned links in the `cc_problems.txt` file.

## Codeforces Scraping and Cleaning (script: codeforces_scraping.py)

This script scrapes problem links from the Codeforces website and saves them in the `csf.txt` file. The links are then cleaned by removing unwanted patterns.

## LeetCode Data Extraction (script: leetcode_data_extraction.py)

This script reads the cleaned LeetCode problem links from the `lc_problems.txt` file and extracts the problem heading and body text. The extracted data is saved in separate files within the `Qdata` directory.

## CodeChef Data Extraction (script: codechef_data_extraction.py)

This script reads the cleaned CodeChef problem links from the `cc_problems.txt` file and extracts the problem heading and body text. The extracted data is saved in separate files within the `Qdata` directory.

Note: The `Qdata` directory will be created automatically if it doesn't exist.

Please make sure to place the appropriate data files (`lc.txt`, `cc.txt`, `lc_problems.txt`, `cc_problems.txt`) in the same directory as the scripts before running them.

Feel free to modify the scripts as per your requirements and add additional functionality if needed.

For any issues or questions, please reach out to through my social media handles.
