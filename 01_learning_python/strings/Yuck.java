import java.util.HashMap;

class Solution {
    public int firstUniqChar(String s) {
        HashMap <Character, Integer> seen = new HashMap<>();
        for(int i = 0; i < s.length() ; i++ ) {
            seen.put(s.charAt(i), seen.get(s.));
        }
    
}