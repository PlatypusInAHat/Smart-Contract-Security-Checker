import subprocess
import os
def run_oyente_analysis(contract_path, report_file):
    try:
        abs_contract_path = os.path.abspath(contract_path)
        cmd = (
            f"docker run --rm -v {os.path.dirname(abs_contract_path)}:/contracts "
            f"luongnguyen/oyente oyente -s /contracts/{os.path.basename(contract_path)}"
        )
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        output = result.stdout + result.stderr
        if "Vulnerability found" in output:
            with open(report_file, "a") as f:
                f.write(f"### Oyente Results for {os.path.basename(contract_path)}\n")
                f.write(f"```\n{output}\n```\n")
            print(f"Oyente analysis completed for {contract_path}")
        return output
    except Exception as e:
        print(f"Oyente analysis failed for {contract_path}: {e}")
        return None
