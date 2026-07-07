//BRUTE FORCE OR EXHAUSTIVE SEARCH ALGORITHM 
//corrected code
public class Main {
    public static void main(String[] args) {
        int[] arr = {2, 7, 11, 15};
        int target = 9;
        int[] result = PairSum(arr, target);
        System.out.println(Arrays.toString(result)); // [0, 1]
    }

    public static int[] PairSum(int[] arr, int target) {
        for (int i = 0; i <= arr.length - 2; i++) {
            for (int j = i + 1; j <= arr.length - 1; j++) {
                if (arr[i] + arr[j] == target) {  // == not =
                    return new int[] {i, j};      // Return array of indices
                }
            }
        }
        return new int[] {};  // Return empty array if not found
    }
}

//my initial code
public class Main{
    public static void main (String[] args) {

        public static int[] PairSum(int[] arr,int target){
            int arr[0] = i;
            int arr[1] = j;

            for (int i=o, i<=arr.length-2, i++){
                for (int j=1, i<=arr.length-1, j++){
                    if (arr[i] + arr[j] = target)
                        return int (arr[i],arr[j]);
                    else 
                        return ("not found");
                }
            }
        }
    }
}

