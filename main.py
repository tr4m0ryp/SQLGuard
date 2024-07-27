from utils.google_dork import find_websites
from utils.sql_injection_checker import check_sql_injection
from utils.report_generator import generate_report
from utils.logger import setup_logger

def main():
    setup_logger()
    search_term = input("Enter the search term: ")

    try:
        websites = find_websites(search_term)
        print("Found websites:")
        for site in websites:
            print(site)

        print("\nChecking for SQL injection vulnerabilities...")
        vulnerabilities = check_sql_injection(websites)

        print("\nGenerating report...")
        generate_report(vulnerabilities)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
