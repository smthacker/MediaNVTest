# // Input is an array of strings. Each string may contain both upper and lower case characters.
#
# // Print sum of vowel presence (a,e,i,o,u,A,E,I,O,U) in each string. Each sum to be printed on new line.
#
# // How to calculate
# // In given example, string is "baceb" so the substrings will be "b, ba, bac, bace, a, ac, ace, aceb, c, ce, ceb, e, eb, baceb" now the number of vowels in each substring will be 0, 1, 1, 2, 1, 1, 2, 2, 0, 1, 1, 1, 1, 2  and the total number will be sum of all presence which is 16.
#
# // Sample input ['baceb'] gives
# // output
# // 16
#
# // Sample input ['baceb', 'xyz'] gives
# // output
# // 16
# // 0
#
# // Sample input ['baceb', 'xyz', 'abc'] gives
# // output
# // 16
# // 0
# // 3

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

ip_array = ['Hello', 'World', 'baceb', 'xyz', 'abc']

def calculate_vowels(string):
    l = len(string)
    sum = 0
    for ind, j in enumerate(string):
        for i in range(ind, l):
            sub_string = string[ind:i+1]
            vowels_in_substr = [v for v in sub_string if v in vowels]
            sum += len(vowels_in_substr)
    print(sum)


if __name__ == '__main__':
 for x in ip_array:
     calculate_vowels(x)