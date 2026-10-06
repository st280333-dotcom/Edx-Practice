def analyze_text(text):

    words = text.split()
    
    word_count = len(words)
    char_count = len(text)
    
    avg_length = sum(len(word) for word in words) / word_count if word_count > 0 else 0
    
    return word_count, char_count, avg_length


# --- Run the Task ---
user_input = input("Enter a sentence or paragraph: ")
words, chars, avg_len = analyze_text(user_input)

print("\n--- Text Analysis Results ---")
print(f"Total Words     : {words}")
print(f"Total Characters: {chars}")
print(f"Avg Word Length : {avg_len:.2f} characters")