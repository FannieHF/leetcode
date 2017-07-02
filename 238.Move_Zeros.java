public class Solution {
    public void moveZeroes(int[] nums) {
        if (nums == null || nums.length == 0)
            return;
            
        int pointer = 0;
        for (int num:nums){
            if (num != 0){
                nums[pointer] = num;
                pointer += 1;
            }
        }
        
        while(pointer<nums.length){
            nums[pointer] = 0;
            pointer ++;
        }
    }
}
