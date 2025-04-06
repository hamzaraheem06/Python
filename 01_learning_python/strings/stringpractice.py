# Python program to sort the characters in a string

my_str = "Hello, this is your captain speaking! Please fasten up your belt, as we are ready to take off."

# def sort_string(user_str: str) -> str:
    

# Python program to remove duplicate characters from a string

def sort_string(user_str: str)-> str:
    # can use bubble sort algorithm, or use built in sorted function
    return "".join(sorted(user_str))

seen = ""

for letter in my_str[:]: # looping over a copy of original string
    if letter not in seen: # to avoid checking for same character twice
        seen += letter
        let_count = my_str.count(letter) # getting the number of occurances
        if  let_count > 1: # removing if more than once
            my_str = my_str[::-1].replace(letter, "", let_count - 1)[::-1] # what this does is reverse the string and then replace the letter with "" i.e. remove it for count - 1 times i.e. only one occurance remains. and then reverses the string back. this makes that the occurances are removed from end and not from start

# print(my_str)

# Python program to remove all non-alphabetic characters from a string

def rem_non_alpha(user_str: str) -> str:
    if user_str.isalpha():
        return user_str

    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    alphabets = alphabets + alphabets.upper()

    seen = ""
    newStr = user_str
    for ch in user_str:
        if ch not in seen and ch not in alphabets:
            seen += ch
            newStr = newStr.replace(ch, "")
        
    return newStr

# print(rem_non_alpha("adk23434adfj23343jkdfasdf"))

def is_anagram(str1: str, str2: str)->bool:
        if len(str1) != len(str2):
            return False
        
        str1 = str1.lower()
        str2 = str2.lower()

        letters1 = set() # using sets to check, because set doesnt account the order in which elements appear
        letters2 = set()

        for i in range(0, len(str1)):
            letters1.add(str1[i])
            letters2.add(str2[i])
        
        if letters1 == letters2:
            return True
        else:
            return False
    
# print(is_anagram("eat", "ate"))


def reverseWords( s: str) -> str:
    words = s.split()
    
    for i in range(len(words) - 1):
        swapped = False
        for j in range(len(words) - i - 1):
            if words[j][0] > words[j+1][0]:
                words[j], words[j+1] = words[j+1], words[j] 
                swapped = True
        if not swapped: break        

    return " ".join(words)

print(reverseWords("the sky is blue"))