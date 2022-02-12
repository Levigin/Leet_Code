package Leet_Code.Easy;

import java.util.Arrays;

public class Remove_Duplicates_from_Sorted_Array_20 {
    public static void main(String[] args) {

        int[] nums = {1, 1,2,3,4,4,4,4,5,5,98};

        System.out.println(removeDuplicates(nums)); //{1,2,3,4,5,6,_,_,_}

        System.out.println(Arrays.toString(nums));

    }

    public static int removeDuplicates(int[] nums) {

        int counter = 1;

        for (int i = 0; i < nums.length-1; i++)
            if (nums[i] != nums[i+1]){
                nums[counter++] = nums[i+1];

            }
        return counter;

    }

}

