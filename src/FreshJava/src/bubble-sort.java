// Bubble sort algorithm
package src;
import java.util.Arrays;

class Main {
    static void BubbleSort(int array[]) {
        int size = array.length;
        
        // For each item in array
        for (int i = 0; i < size - 1; i++)
        
            // compare adjacent items
            for (int j = 0; j < size - i - 1; j++)
                
                if (array[j] > array[j + 1]) {
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                } 
    }
    public static void main(String args[]){
        // Base data
        int[] data = {1,11,22,312,2,7,5,9,12,36,24,17,16,2000,0};
        System.out.println("Array : ");
        System.out.println(Arrays.toString(data));
        
        // Sorted data
        Main.BubbleSort(data);
        System.out.println("Sorted Array : ");
        System.out.println(Arrays.toString(data));
    }
}