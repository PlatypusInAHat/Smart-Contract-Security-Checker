// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

import "./vulnerable.sol";

contract Complex is Vulnerable {
    function extraFunction() public pure returns (string memory) {
        return "This is a complex contract";
    }
}
