###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0
place = 0

# Count vowels in the text

while place < len(text) :
    
    char = text[place]

    if char in vowels:
        vowel_count += 1

    place += 1

print(f"The number of vowels in the text is: {vowel_count}")