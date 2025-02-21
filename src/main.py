import os
import logging
from tools.slither_analysis import run_slither_analysis
from tools.mythril_analysis import run_mythril_analysis
from tools.echidna_test import run_echidna_test
from tools.oyente_analysis import run_oyente_analysis
from tools.securify_analysis import run_securify_analysis
logging.basicConfig(filename="analysis.log", level=logging.INFO, format="(levelname)s - (message)s")
def analyze_contracts(directory="contracts", report_file="reports/analysis_report.md"):
    if not os.path.exists("reports"):
        os.makedirs("reports")
    if os.path.exists(report_file):
        os.remove(report_file)
    with open(report_file, "w") as f:
        f.write("# Smart Contract Security Analysis Report\n\n")
    for contract_file in os.listdir(directory):
        if contract_file.endswith(".sol"):
            contract_path = os.path.join(directory, contract_file)
            logging.info(f"Starting analysis for {contract_path}")
            print(f"Analyzing {contract_path}...")
            slither_result = run_slither_analysis(contract_path, report_file)
            mythril_result = run_mythril_analysis(contract_path, report_file)
            echidna_result = run_echidna_test(contract_path, report_file)
            oyente_result = run_oyente_analysis(contract_path, report_file)
            securify_result = run_securify_analysis(contract_path, report_file)
            logging.info(f"Completed analysis for {contract_path}")
    print(f"Analysis completed. Results saved to {report_file}")
if __name__ == "__main__":
    analyze_contracts()
