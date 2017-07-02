import java.util.HashSet;

public class Solution {
    public int distributeCandies(int[] candies) {
        
        HashSet<Integer> hset = 
               new HashSet<Integer>();
        
        int len = candies.length;
        int max = len/2;
        for (int num:candies){
            hset.add(num);
        }
        
        return Math.min(hset.size(),max);
    }
}
