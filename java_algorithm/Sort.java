package java_algorithm;
import java.util.Scanner;

public class Sort {

    static void insertionSort(int a[], int n, int h) {
        int numOfKMove = 0;
        
        for (int i = h; i < n; i++){
            int x = a[i];
            int j = i - h;

            while (j >= 0 && a[j] > x) {
                a[j + h] = a[j];
                j -= h;
                numOfKMove++;
            }

            a[j + h] = x;
        }

        System.out.println((numOfKMove));
    }

    static void shellSort(int a[], int n, int[] h, int k) {
        for (int i = 0; i < k; i++) {
            insertionSort(a, n, h[i]);
        }
    }
    public static void run(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int a[] = new int[n];
        for (int i =0; i < n; i++) {
            a[i] = sc.nextInt();
        }
            int k = sc.nextInt();

            int h[] = new int[k];
            for (int i = 0; i < k; i++){
                h[i] = sc.nextInt();
            }

            shellSort(a, n, h, k);
           
    }
    
}
