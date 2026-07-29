// Last updated: 7/29/2026, 10:14:05 AM
class Solution {
    public int lengthOfLongestSubstring(String s) 
    {
         int maxLength = 0;
        String currentSubstring = "";

        for (int i = 0; i < s.length(); i++)
        {
            char c = s.charAt(i);
                if (currentSubstring.contains(String.valueOf(c)))
                {
                    maxLength = Math.max(maxLength , currentSubstring.length());
                    int index = currentSubstring.indexOf(c);
                    currentSubstring = currentSubstring.substring(index+1);
                }

                currentSubstring += c;

        }

            maxLength = Math.max(maxLength , currentSubstring.length());


        return maxLength;


    }
}

