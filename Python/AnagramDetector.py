def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)

if __name__ == "__main__":
    str1 = "listen"
    str2 = "silent"

    if is_anagram(str1, str2):
        print(f"{str1} and {str2} are anagrams.")
    else:
        print(f"{str1} and {str2} are not anagrams.")