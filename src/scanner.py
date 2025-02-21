def scan_contract(contract_path):
    vulnerabilities = []
    with open(contract_path, "r") as f:
        code = f.read()
        if ".call{value:" in code and "balances" not in code.split(".call")[0]:
            vulnerabilities.append("Potential reentrancy vulnerability detected")
        if ".call" in code and "require(" not in code.split(".call")[1].split(";")[0]:
            vulnerabilities.append("Unchecked return value from .call detected")
    return vulnerabilities
