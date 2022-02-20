package Leet_Code.Easy;

import java.util.Objects;

public class Implement_strStr_28 {

    public static void main(String[] args) {

        String haystack = "mississippi"; // "hello";

        String needle = "z";

        System.out.println(strStr(haystack, needle));

    }
    public static int strStr(String haystack, String needle) {

        return haystack.indexOf(needle);
    }
}
