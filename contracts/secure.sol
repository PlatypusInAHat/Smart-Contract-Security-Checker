// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

contract Secure {
    mapping(address = public balances;
    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }
    function withdraw() public {
        uint balance = balances[msg.sender];
        require(balance , "Insufficient balance");
        balances[msg.sender] = 0;
        (bool sent, ) = msg.sender.call{value: balance}("");
        require(sent, "Failed to send Ether");
    }
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}
