package Leet_Code.Easy;

import Leet_Code.Medium.BinarySearce;

import java.util.Arrays;

public class Search_Insert_Position_35 {

    public static void main(String[] args) { /* accept: fast, 0 ms */

        int[] nums = new int[] {1,3,5,10};
        int target = 11;

        System.out.println(searchInsert(nums,target));

    }

    public static int searchInsert(int[] nums, int target) {

        return recursiveSeeker(nums, target, 0, nums.length-1);
    }

    public static int recursiveSeeker(int[] nums,int target,int left_border,int right_border){

        if (left_border>=right_border) {
            if (nums[left_border] == target) return left_border;
            else if (nums[right_border] < target) return right_border+1;
            else return left_border;
        }

        int pivot_index = (left_border+right_border)/2;
        int pivot_element = nums[pivot_index];

        if (pivot_element<target) return recursiveSeeker(nums,target,pivot_index+1, right_border);
        else if(pivot_element>target) return recursiveSeeker(nums, target, 0, pivot_index );
        else return pivot_index;

    }
}
