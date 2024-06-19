def palindrome(input_string):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    char_count = [0] * 26
    for char in input_string:
        char_count[alpha.index(char)] += 1
    print(char_count)
    palindrome_base = ''
    middle_char = ''
    for index, count in enumerate(char_count):
        palindrome_base += alpha[index] * (count // 2)
        if count % 2 == 1 and middle_char == '':
            middle_char = alpha[index]

    palindrome = palindrome_base + middle_char + palindrome_base[::-1]
    return palindrome

N = int(input())
string = input()
print(palindrome(string))

