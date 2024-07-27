def generate_report(vulnerabilities):
    with open("report.txt", "w") as report_file:
        for site in vulnerabilities:
            report_file.write(f"{site}\n")
    print(f"Report generated with {len(vulnerabilities)} vulnerable sites.")
