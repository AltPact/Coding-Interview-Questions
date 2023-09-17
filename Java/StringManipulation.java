public class StringUtils {
    public static int countCharacters(String input) {
        return input.length();
    }

    public static int findSubstrings(String input, String substring) {
        int count = 0;
        int index = input.indexOf(substring);
        while (index != -1) {
            count++;
            index = input.indexOf(substring, index + 1);
        }
        return count;
    }

    public static String reverseWords(String input) {
        String[] words = input.split(" ");
        StringBuilder reversed = new StringBuilder();
        for (String word : words) {
            reversed.append(new StringBuilder(word).reverse()).append(" ");
        }
        return reversed.toString().trim();
    }

    public static void main(String[] args) {
        System.out.println(countCharacters("Hello, World!")); // Output: 13
        System.out.println(findSubstrings("Hello, World! Hello, Java!", "Hello")); // Output: 2
        System.out.println(reverseWords("Hello, World!")); // Output: "olleH, dlroW!"
    }
}