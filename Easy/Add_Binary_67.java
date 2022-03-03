package Leet_Code.Easy;

import java.math.BigInteger;

public class Add_Binary_67 {

    public static void main(String[] args) { /** accepted so 5 ms **/

        String a = "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101";//"10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101";

        String b = "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011"; //"110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011";


        System.out.println(addBinary(a,b));
    }

    public static String addBinary(String a, String b) {

        BigInteger value1 = new BigInteger(a,2);
        BigInteger value2 = new BigInteger(b,2);
        BigInteger result = value1.add(value2);

        return result.toString(2);
    }
}
