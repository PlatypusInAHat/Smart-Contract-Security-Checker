import os
from mythril.mythril import MythrilAnalyzer
def run_mythril_analysis(contract_path, report_file):
    try:
        analyzer = MythrilAnalyzer(solidity_file=contract_path, strategy="dfs")
        report = analyzer.analyze()
        if report.issues:
            with open(report_file, "a") as f:
                f.write(f"### Mythril Results for {os.path.basename(contract_path)}\n")
                f.write("| Issue | Severity | Location |\n|-------|----------|----------|\n")
                for issue in report.issues:
                    f.write(f"| {issue.title} | {issue.severity} | {issue.function} |\n")
        print(f"Mythril analysis completed for {contract_path}")
        return report
    except Exception as e:
        print(f"Mythril analysis failed for {contract_path}: {e}")
        return None
