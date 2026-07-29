// Last updated: 7/29/2026, 10:13:59 AM
class Solution {
    public int romanToInt(String s) {
        int count = 0;
    Map<Character, Integer> RomanMap = new HashMap<Character, Integer>();
        RomanMap.put('I',1);
        RomanMap.put('V',5);
        RomanMap.put('X',10);
        RomanMap.put('L',50);
        RomanMap.put('C',100);
        RomanMap.put('D',500);
        RomanMap.put('M',1000);

        Queue<Character> RomanQ = new LinkedList<>();
        for(int i = 0; i < s.length(); i++){
            RomanQ.add(s.charAt(i));
        }
        while(!RomanQ.isEmpty()){
            Character first = RomanQ.poll();
            if(RomanQ.isEmpty()){
                return count + RomanMap.get(first);
            }
            Character second = RomanQ.peek();
            if(first == 'I' && second == 'V'){
                count += 4;
                RomanQ.remove();
            }
            else if(first == 'I' && second == 'X'){
                count += 9;
                RomanQ.remove();

            }
            else if(first == 'X' && second == 'L'){
                count += 40;
                RomanQ.remove();
            }
            else if(first == 'X' && second == 'C'){
                count += 90;
                RomanQ.remove();
            }
            else if(first == 'C' && second == 'D'){
                count += 400;
                RomanQ.remove();
            }
            else if(first == 'C' && second == 'M'){
                count += 900;
                RomanQ.remove();
            }
            else{
                count += RomanMap.get(first);
            }
        }
        return count;
    }
}