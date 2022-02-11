package Leet_Code.Easy;
public class Roman_to_Integer_13 {
    public static void main(String[] args) {

        String s = "CMIX";

        System.out.println(romanToInt(s));

    }

    public static int romanToInt(String s) {

        int I = 1;
        int V = 5;
        int X = 10;
        int L = 50;
        int C = 100;
        int D = 500;
        int M = 1000;
        int number = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'I') {
                if (s.contains("IV")) {
                    int IV = 4;
                    number += IV;
                    i += 1;
                }
                else if (s.contains("IX")) {
                    int IX = 9;
                    number += IX;
                    i += 1;
                    }
                else number += I;

                }
            else if (s.charAt(i) == 'V') {
                    number += V;

                }
            else if (s.charAt(i) == 'X') {
                if (s.contains("XL")) {
                    int XL = 40;
                    number += XL;
                    i += 1;

                }
                else if (s.contains("XC")) {
                    int XC = 90;
                    number += XC;
                    i += 1;

                }
                else number += X;
                }

            else if (s.charAt(i) == 'L') {
                number += L;
                }

            else if (s.charAt(i) == 'C') {
                if (s.contains("CD")) {
                    int CD = 400;
                    number += CD;
                    i += 1;
                }
                else if (s.contains("CM")) {
                    int CM = 900;
                    number += CM;
                    i += 1;
                }
                else number += C;
                }

            else if (s.charAt(i) == 'D') {
                number += D;
                }

            else if (s.charAt(i) == 'M') {
                number += M;
                }

            }
        return number;

        }

    }