package Leet_Code.Easy;

import java.math.BigInteger;
import java.util.Arrays;

public class Plus_One_66 {
    public static void main(String[] args) {

        int[] digits = new int[] {1,2,3,9}; //{1,2,3,9};//{9,8,7,6,5,4,3,2,1,0};  //{1,2,3};

       System.out.println(Arrays.toString(plusOne(digits))); /** accepted SLOWLY 10 ms **/

    }

    public static int[] plusOne(int[] digits) {

    String str = "";

    for (int i = 0; i < digits.length; i++) {
        str =str + digits[i] + "";}

    BigInteger value = new BigInteger(str);
    BigInteger value1 = new BigInteger("1");
    BigInteger result = value.add(value1);
    String result1 = result.toString();
    int[] arrays = new int[result1.length()];

    for (int i = 0; i < result1.length(); i++){
        arrays[i] = (int)result1.charAt(i) - '0';
    }
        return arrays;
    }
}
