package Leet_Code.Easy;

import java.util.Arrays;

public class Two_Sum_1 {
    public static void main(String[] args) {

        int[] nums = {2,7,11,15};

        int target = 9;

        System.out.println(Arrays.toString(twoSum(nums, target)));

    }

    public static int[] twoSum(int[] nums, int target) {
        int i = 0;

        int[] arrays = new int[2];
        for (i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    arrays[0] = i;
                    arrays[1] = j;
                    break;

                }

            }

        }
        return arrays;
    }
}

