#Replacing a particular word with another word in a string in python ?
"""Here on this page, we will learn to create a Python Program to Replace a Particular Word with Another Word.

Example :

Input : s = “Let’s Learn Python from Internet”, s1 = “Internet”, s2 = “PrepInsta”

Output : “Let’s Learn Python from PrepInsta” """

def modifyString(s, s1, s2):
    ans = ""
    c = -1
    for i in range(len(s)):
        if i < c:
            continue
        k = 0
        if s[i] == s1[k] and i + len(s1) <= len(s):
            z = 0
            for j in range(i, i + len(s1)):
                z = j
                if s[j] != s1[k]:
                    break
                else:
                    k += 1

            if z == i + len(s1) - 1:
                ans += s2
                c = i + len(s1)
            else:
                ans += s[i]
        else:
            ans += s[i]

    return ans


s = "Let's Learn Python from Internet"
s1 = "Internet"
s2 = "PrepInsta"
print("Original String :", s)
print("Modified String :", modifyString(s, s1, s2))