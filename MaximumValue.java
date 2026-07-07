//linear search
public class MaximumValue {
    
    // Linear Search - find maximum integer in unsorted array
    public static int linearSearch(int[] arr) {
        if (arr.length == 0) return -1;  // Handle empty array
        
        int max = arr[0];  // Start with first element
        
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) {  // Compare with current maximum
                max = arr[i];    // Update if larger found
            }
        }
        return max;
    }
}
