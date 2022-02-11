package Leet_Code.Easy;

public class Palindrome_Number_9 {

    public static void main(String[] args) {

        System.out.println(isPalindrome(121));

    }

    public static boolean isPalindrome(int x){ // accept 7 ms

        String s = Integer.toString(x);

        for (int i = 0; 2*i < s.length(); i++){

            if(s.charAt(i) != s.charAt(s.length()-1-i)) return false;

        }

        return true;
    }
}
