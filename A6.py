# Implement Anagram.

def anag(s1,s2):
    list1 = list(s1)
    list2 = list(s2)

    list1.sort()
    list2.sort()

    pos = 0
    match = True

    while pos < len(s1) and match:
        if list1[pos]==list2[pos]:
            pos = pos + 1
        else:
            match = False

    return match


s1 = input("Enter string 1 ")
s2= input("enter string 2 ")

print(anag(s1,s2))
