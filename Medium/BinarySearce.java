package Leet_Code.Medium;



public class BinarySearce {

    public static void main(String[] args) {

        int[] array = new int[] {-1,0,2,3,4,5,6,14,20,28,30,41};
        int target =14;
        System.out.println(search(array,target));

    }

    public static int search(int[] nums, int target){


        return recursive_seeker(nums, target, 0 , nums.length -1);
    }

    public static int recursive_seeker(int[] nums,int target, int left_border, int right_border) {

        if (left_border>=right_border) {
            if (nums[left_border] == target) return left_border;
            else return -1;
        }

        int pivot_index = (left_border+right_border)/2;
        int pivot_element = nums[pivot_index];

        if  (pivot_element == target) return pivot_index;
        else if (pivot_element<target) return recursive_seeker(nums,target, pivot_index+1, right_border) ;
        else return recursive_seeker(nums, target ,0 , pivot_index);
    }

}
