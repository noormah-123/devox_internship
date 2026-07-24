string1 = "Listen"
string2 = "Silent"

string1 = string1.lower()
string2 = string2.lower()

if sorted(string1)==sorted(string2):
    print("Both are anagrams.")
else:
    print("Both are not anagrams.")