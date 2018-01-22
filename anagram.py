import sys


def is_anagram(s):
    return sorted(s[:len(s)//2]) == sorted(s[len(s)//2:])

def has_anagram(s):
    print(s)
    for i in range(len(s)-1):
        for j in range(i+2,len(s)+1, 2):
            if is_anagram(s[i:j]):
                return True
    return False

if __name__ == "__main__":
    s = sys.argv[1]
    print("{} {} an anagram".format(s,
          ['is not','is'][has_anagram(s)]))
    print("{} {} an anagram".format(s,
          ['does not contain','contains'][has_anagram(s)]))
