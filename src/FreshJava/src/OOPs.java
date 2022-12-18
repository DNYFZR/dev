// OOPs I spilled my Java... 
package src;

class OOPs {
    public int divider(int numerator, int denominator) {
        return numerator / denominator;
    }
    
    public static void main(String[] args) {
        // Declare vars
        int first = 42;
        int second = 21;

        // Create object of Main
        OOPs obj = new OOPs();
        int result = obj.divider(first, second);

        // Print output
        System.out.println(
            String.format("%s / %s = %s", first, second, result )
            );
    }
}
