package Leet_Code.Easy;

import java.util.Arrays;

public class Remove_Element_27 {
    public static void main(String[] args) {

        int[] nums = {3,4,4,4,2,2,4,4,4,3,4};

        int val = 4;

        System.out.println(removeElement(nums,val));

        System.out.println(Arrays.toString(nums));

    }

    public static int removeElement(int[] nums, int val) {

        int counter = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[counter] = nums[i];
                counter++;

            }
        }
        return counter;

    }
}

