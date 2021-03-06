package Leet_Code.Easy;

public class Valid_Parentheses_20 {
    public static void main(String[] args) {

        String s = "()()";

        System.out.println(isValid(s));


    }

    public static boolean isValid(String s) {

        boolean flag = true;

        int counter1 = 0, counter2 = 0, counter3 = 0;

        for (int i=0; i<s.length();i++){

            if( s.charAt(i) == '[') counter1++;
            if( s.charAt(i) == ']') counter1--;
            if( s.charAt(i) == '(') counter1++;
            if( s.charAt(i) == ')') counter1--;
            if( s.charAt(i) == '{') counter1++;
            if( s.charAt(i) == '}') counter1--;

        }

        flag = counter1 == 0 && counter2 == 0 && counter3 == 0;

        if (!flag) return false;

        return recursive_seeker(s);
    }

    public static boolean recursive_seeker(String s){

        if (s.length() == 2) return s.charAt(0)=='{' && s.charAt(1) == '}' || s.charAt(0) == '[' && s.charAt(1) == ']'
                || s.charAt(0) == '(' && s.charAt(1) == ')';


        if (s.length() == 0) return true;

        boolean flag = false;

        for (int i=0; i < s.length()-1; ++i){

            if(i < s.length()-1 && s.charAt(i)=='{' && s.charAt(i+1)=='}'){
                if(i!=s.length()-2) {
                    s = s.substring(0, i) + s.substring(i + 2);
                    flag = true;
                    i = 0;
                }
                else s = s.substring(0,i);
            }
            if(i < s.length()-1 && s.charAt(i)=='(' && s.charAt(i+1)==')') {
                if(i!=s.length()-2) {
                    s = s.substring(0, i) + s.substring(i + 2);
                    flag = true;
                    i = 0;
                }
                else s = s.substring(0,i);
            }
            if(i < s.length()-1 && s.charAt(i)=='[' && s.charAt(i+1)==']') {
                if(i!=s.length()-2) {
                    s = s.substring(0, i) + s.substring(i + 2);
                    flag = true;
                    i = 0;
                }
                else s = s.substring(0,i);
            }
        }


        if (!flag) return false;

        return recursive_seeker(s);
    }
}
