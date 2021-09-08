pragma solidity =0.7.3;
 
contract FirstContract {
 
    uint256 number;
    string[] names;
    mapping(string => uint) phonenos;


    function addPhonenos(string memory _name, uint _pno) public {
        phonenos[_name] = _pno;
    }

    function showPhoneno(string memory _name) public view returns (uint) {
        return phonenos[_name];
    }

    function setNumber(uint256 _num) public {
        number = _num;
    }
 
 
    function getNumber() public view returns (uint256){
        return number;
    }
}
