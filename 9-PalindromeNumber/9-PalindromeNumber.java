// Last updated: 7/29/2026, 10:14:00 AM
class Solution {
    public boolean isPalindrome(int x) {
        Stack<Character> stack = new Stack<>();
        String xString = Integer.toString(x);
        for(int i = 0; i < xString.length() ; i++){
            stack.push(xString.charAt(i));
        }
        int j = 0;
        while(!stack.isEmpty()){
            if(stack.pop() != xString.charAt(j)){
                return false;
            }
            j++;
        }
        return true;
    }

}