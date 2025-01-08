package java_algorithm;

import java.util.*;

public class Hanoi_algorithm {
    
    public static void hanoi(Integer n, String start, String goal, String buf) {
        if (n >= 2) {
            // まずn-1個の円盤をstartからbufに移動
            hanoi(n - 1, start, buf, goal);
        }
        // n番目の円盤をstartからgoalに移動
        System.out.println(n + "番の円盤を" + start + "から" + goal + "に移す");
        if (n >= 2) {
            // その後、n-1個の円盤をbufからgoalに移動
            hanoi(n - 1, buf, goal, start);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Integer n = sc.nextInt();  // 円盤の数
        Integer t = sc.nextInt();  // tは使用していませんが、入力として受け取る
        hanoi(n, "A", "C", "B");   // 3つの柱A, B, CのうちAからCに円盤を移動
    }
}