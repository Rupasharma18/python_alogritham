anagram1=input("Enter first string:")
anagram2=input("Enter second string:")
if(sorted(anagram1)==sorted(anagram2)):
      print("The strings are anagrams.")
else:
      print("The strings aren't anagrams.")