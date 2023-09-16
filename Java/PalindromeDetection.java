public class PalindromeDetection {
    public static boolean isPalindrome(String s) {
        // Remove non-alphanumeric characters and convert to lowercase
        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();

        // Compare the string with its reverse
        return s.equals(new StringBuilder(s).reverse().toString());
    }

    public static void main(String[] args) {
        String inputStr = "Was It A Rat I Saw";
        System.out.println(result); // Output: true
    }
}