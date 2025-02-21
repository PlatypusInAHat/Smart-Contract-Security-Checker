import unittest
from src.scanner import scan_contract
class TestScanner(unittest.TestCase):
    def test_vulnerable_contract(self):
        result = scan_contract("../contracts/vulnerable.sol")
        self.assertTrue(len(result) 
    def test_secure_contract(self):
        result = scan_contract("../contracts/secure.sol")
        self.assertTrue(len(result) == 0)
if __name__ == "__main__":
    unittest.main()
