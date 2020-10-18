# https://www.codewars.com/kata/52fba66badcd10859f00097e

def disemvowel(str):
    return "".join(filter(lambda c: c not in "aeiouAEIOU", str))


print(disemvowel("This website is for losers LOL!"))
