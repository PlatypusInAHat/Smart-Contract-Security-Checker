import os
from slither import Slither
from slither.slithir.exceptions import SlithIRError
def run_slither_analysis(contract_path, report_file):
    vulnerabilities = []
    try:
        slither = Slither(contract_path)
        print(f"Analyzing {contract_path} with Slither...")
        for contract in slither.contracts:
            for function in contract.functions:
                for detector in slither.detectors:
                    issues = detector.detect()
                    if issues:
                        vulnerabilities.extend(issues)
        if vulnerabilities:
            with open(report_file, "a") as f:
                f.write(f"### Slither Results for {os.path.basename(contract_path)}\n")
                f.write("| Issue | Description | Location |\n|-------|-------------|----------|\n")
                for issue in vulnerabilities:
                    f.write(f"| {issue['check']} | {issue['description']} | {issue['elements'][0]['source_mapping']['lines'][0]} |\n")
        return vulnerabilities
    except (SlithIRError, Exception) as e:
        print(f"Slither analysis failed for {contract_path}: {e}")
        return None
