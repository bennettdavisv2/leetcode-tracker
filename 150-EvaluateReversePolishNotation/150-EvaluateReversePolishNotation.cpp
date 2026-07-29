// Last updated: 7/29/2026, 10:13:30 AM
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
    stack<int>stk;
    for(int i=0;i<tokens.size();i++){
        if(tokens[i] == "+" or tokens[i] == "-" or tokens[i] == "*" or tokens[i] == "/"){
                int num1 = stk.top(); 
                stk.pop();
                int num2 = stk.top(); 
                stk.pop();
                if(tokens[i] == "+") stk.push(num2+num1);
                else if(tokens[i] == "-") stk.push(num2-num1);
                else if(tokens[i] == "*") stk.push(num2*num1);
                else stk.push(num2/num1);
        }
        else stk.push(stoi(tokens[i]));
    }
    return stk.top();
    }
};