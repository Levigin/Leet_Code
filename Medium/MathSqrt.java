package Leet_Code.Medium;

public class MathSqrt {

    static int n;

    public static void main(String[] args) {

        long start = System.nanoTime();

        System.out.println(mySqrt(100));

        System.out.println(mySqrt_Newton(15));

        long finish = System.nanoTime();

        System.out.println("t1 = "+ (finish-start)/1000 + "microsec");

    }

    public static long mySqrt(int x) {

        if (x==1) return 1;
        n=x;

        //1, 2, 3, .... n -> x


        return binarisearch(0, n);

    }
    public static int binarisearch(long left_border,long rigth_border){
        if (left_border>rigth_border){
            System.out.println("Bad");
            return 0;
        }

        long temp = (left_border+rigth_border)/2;

        if (temp*temp <= n && ((temp+1)*(temp+1)) > n) return (int) temp;
        else if (temp*temp < n) return binarisearch(temp, rigth_border);
        else return binarisearch(left_border, temp);

    }

    public static int mySqrt_Newton(int x){

        if (x==0) return 0;


        double sqrt_n = x;
        double sqrt_pref = x+2;

        while (true) {

            sqrt_pref = sqrt_n;
            sqrt_n = (sqrt_n + x/sqrt_n)/2;
            if (sqrt_pref-sqrt_n<0.000000001) break;

        }
      return (int) sqrt_n;
    }
}
