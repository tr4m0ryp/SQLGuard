import subprocess
from loguru import logger

def check_sql_injection(websites):
    vulnerabilities = []
    for site in websites:
        logger.info(f"Checking site: {site}")
        try:
            result = subprocess.run(
                ["python", "sqlmap/sqlmap.py", "-u", site, "--batch", "--level=1", "--risk=1"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            if "vulnerable" in result.stdout.lower():
                logger.info(f"Vulnerable site found: {site}")
                vulnerabilities.append(site)
        except Exception as e:
            logger.error(f"Error checking site {site}: {e}")
    return vulnerabilities
