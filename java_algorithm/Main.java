package java_algorithm;
//整数nと、要素数nの数列A、整数kを与えて、Aにkが何個含まれているのかを求めるコード
//Aの数列は半角で入力し、数字の間を開けるのも半角。

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 配列のサイズ n を入力
        int n = sc.nextInt();
        
        // 配列 a を作成し、n 個の整数を受け取る
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        // 検索対象の値 k を入力
        int k = sc.nextInt();

        // k の出現回数をカウントするための変数
        int numOfK = 0;

        // 配列 a の要素を1つずつ確認し、k と一致するか判定
        for (int value : a) {
            if (value == k) {
                // k と一致した場合はカウントを増やす
                numOfK++;
            }
        }

        // k の出現回数を出力
        System.out.println(numOfK);
    }
}