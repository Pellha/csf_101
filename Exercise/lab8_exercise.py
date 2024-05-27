def find_first_repeating_character(s):
    # Dictionary to store the count of each character encountered
    char_count = {}
    
    # Iterate through the characters in the string
    for char in s:
        # Check if the character is already encountered
        if char in char_count:
            # If yes, print the character along with its memory address
            print(f"First repeating character: {char}, Memory Address: {id(char)}")
            return char, id(char)  # Return the character and its memory address
        else:
            # If not, update the count of the character
            char_count[char] = 1
    
    # If no repeating character is found, return None
    return None

# Test the function
s = "abcdefgabc"
result = find_first_repeating_character(s)
if result is None:
    print("No repeating character found.")