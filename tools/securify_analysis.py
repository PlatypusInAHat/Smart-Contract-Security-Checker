import subprocess
import os
from src.utils import flatten_contract
def run_securify_analysis(contract_path, report_file):
    try:
        flattened_path = flatten_contract(contract_path)
        if not flattened_path:
            raise Exception("Failed to flatten contract")
        abs_flattened_path = os.path.abspath(flattened_path)
        cmd = (
            f"docker run --rm -v {os.path.dirname(abs_flattened_path)}:/contracts "
            f"securify2 securify /contracts/{os.path.basename(flattened_path)}"
        )
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        output = result.stdout + result.stderr
        if "VIOLATION" in output or "WARNING" in output:
            with open(report_file, "a") as f:
                f.write(f"### Securify Results for {os.path.basename(contract_path)}\n")
                f.write(f"Analyzed flattened file: {os.path.basename(flattened_path)}\n")
                f.write(f"```\n{output}\n```\n")
            print(f"Securify analysis completed for {contract_path}")
        if os.path.exists(flattened_path):
            os.remove(flattened_path)
        return output
    except Exception as e:
        print(f"Securify analysis failed for {contract_path}: {e}")
        return None
