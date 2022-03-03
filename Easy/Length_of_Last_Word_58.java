package Leet_Code.Easy;

public class Length_of_Last_Word_58 {

    public static void main(String[] args) { /** accepted fast 0 ms **/

        String s =  "luffy";    //"   fly me   to   the moon  ";  //"Hello World    "

        System.out.println(lengthOfLastWord(s));
    }
    public static int lengthOfLastWord(String s) {

        int count1 = 0;
        s = s.trim();

        for (int i = s.length()-1; i >= 0; i--){
            if (s.charAt(i) != ' ') count1++;
            else return count1;
        }
        return count1;
    }
}
