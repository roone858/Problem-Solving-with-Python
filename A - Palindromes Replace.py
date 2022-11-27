
def isPossiblePalindrome(str):
    n = len(str)
    for i in range(n // 2):
        if (str[i] != '?' and
                str[n - i - 1] != '?' and
                str[i] != str[n - i - 1]):
            return False

    return True

def smallestPalindrome(str):
    if (not isPossiblePalindrome(str)):
        return "Not Possible"
    n = len(str)
    str = list(str)
    for i in range(n):
        if (str[i] == '?'):
            if (str[n - i - 1] != '?'):
                str[i] = str[n - i - 1]
            else:
                str[i] = str[n - i - 1] = 'a'
    return str


word = input().lower()
print(''.join(smallestPalindrome(word)))

'''
word = list(input().lower())
check = True

j = len(word)-1
i = 0
while (i <= j):

    if (i == j-1) and (word[i] == "?") and (word[j] == "?"):
        word[i] = "a"
        word[j] = "a"
    if (i == j) and (word[i] == "?"):
        word[i] = "a"
    if word[i] == "?":
        word[i] = word[j]
    if word[j] == "?":
        word[j] = word[i]

    i = i+1
    j = j-1

for x in range(len(word)):
    if word[len(word)-1 - x] != word[x]:
        check = False

if check:
    print("".join(word))
else:
    print(-1)



'''




