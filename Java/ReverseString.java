public class StringReversal {
    public static String reverseString(String input) {
        StringBuilder reversed = new StringBuilder(input);
        reversed.reverse();
        return reversed.toString();
    }

    public static void main(String[] args) {
        String inputStr = "Hello, World!";
        String reversedStr = reverseString(inputStr);
        System.out.println("Reversed: " + reversedStr);
    }
}