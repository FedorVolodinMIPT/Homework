def is_palindrome(s):
    if s == s[::-1]:
        return 1
    else:
        return 0

def is_mirrored(s):
    reversed_string = s[::-1]
    mirrored_string = ''

    for i in range(len(s)):
        if reversed_string[i] in mirror_chars1:
            index = mirror_chars1.index(reversed_string[i])
            mirrored_string += mirror_chars2[index]
        elif reversed_string[i] in mirror_chars2:
            index = mirror_chars2.index(reversed_string[i])
            mirrored_string += mirror_chars1[index]
        else:
            return 0
    if mirrored_string == s:
        return 1
    else:
        return 0


string = input()

if is_palindrome(string) == 1 and is_mirrored(string) == 1:
    print(string, "is a mirrored palindrome.")
elif is_palindrome(string) == 1:
    print(string, "is a regular palindrome.")
elif is_mirrored(string) == 1:
    print(string, "is a mirrored string.")
else:
    print(string, "is not a palindrome.")
