def detectCapitalUse(word: str) -> bool:
    return word == word.upper() or word == word.capitalize() or word == word.lower()

print(detectCapitalUse("USA")) # True
print(detectCapitalUse("FlaG")) # False
print(detectCapitalUse("test")) # True