import os
import subprocess
from solcx import compile_files, install_solc
import shutil
def flatten_contract(contract_path, output_dir="flattened"):
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        install_solc("0.8.0")
        output_file = os.path.join(output_dir, f"flattened_{os.path.basename(contract_path)}")
        if shutil.which("truffle-flattener"):
            cmd = f"truffle-flattener {contract_path} > {output_file}"
            subprocess.run(cmd, shell=True, check=True)
        else:
            compiled = compile_files([contract_path], solc_version="0.8.0")
            with open(output_file, "w") as f:
                for contract in compiled:
                    f.write(compiled[contract]["bin"])
        return output_file
    except Exception as e:
        print(f"Flattening failed for {contract_path}: {e}")
        return None
def read_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found")
    with open(file_path, "r") as f:
        return f.read()
def write_report(file_path, content):
    with open(file_path, "a") as f:
        f.write(content + "\n")
def is_valid_solidity_file(file_path):
    return file_path.endswith(".sol") and os.path.isfile(file_path)
