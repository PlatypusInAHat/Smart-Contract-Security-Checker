// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

contract Vulnerable {
    mapping(address = public balances;
    uint256 public totalSupply;
    function deposit() public payable {
        balances[msg.sender] += msg.value;
        totalSupply += msg.value;
    }
    function withdraw() public {
        uint256 balance = balances[msg.sender];
        require(balance , "Insufficient balance");
        (bool sent, ) = msg.sender.call{value: balance}("");
        require(sent, "Failed to send Ether");
        balances[msg.sender] = 0;
    }
    function getBalance() public view returns (uint256) {
        return address(this).balance;
    }
}
