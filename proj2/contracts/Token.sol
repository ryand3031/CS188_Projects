contract Token{
    string public name;
    uint8 public decimals;
    string public symbol;
    uint256 public totalSupply;
    mapping (address => uint256) public balances;

    event Transfer(address indexed _from, address indexed _to, uint256 _value);
    event Approval(address indexed _owner, address indexed _spender, uint256 _value);
    
    constructor(uint256 _initialAmount) public{
        name = "505416119";
        symbol = "CS188";
        decimals = 18;
        totalSupply = _initialAmount;
        balances[msg.sender] = _initialAmount;
    }

    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(balances[msg.sender] >= _value);
        balances[msg.sender] -= _value;
        balances[_to] += _value;
        emit Transfer(msg.sender, _to, _value); //solhint-disable-line indent, no-unused-vars
        return true;
    }




}