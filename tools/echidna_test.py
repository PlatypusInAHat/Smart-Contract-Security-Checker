import subprocess
import os
def run_echidna_test(contract_path, report_file):
    try:
        config_file = "echidna_config.yaml"
        with open(config_file, "w") as f:
            f.write("testLimit: 20000\n")
            f.write("testMode: property\n")
        cmd = f"echidna-test {contract_path} --config {config_file}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.stdout:
            with open(report_file, "a") as f:
                f.write(f"### Echidna Results for {os.path.basename(contract_path)}\n")
                f.write(f"```\n{result.stdout}\n```\n")
        print(f"Echidna fuzzing completed for {contract_path}")
        return result.stdout
    except Exception as e:
        print(f"Echidna test failed for {contract_path}: {e}")
        return None
