def analyze_paragraph(text):
   
    text = text.lower()

   
    punctuation = ".,!?;:-_\"'"
    for symbol in punctuation:
        text = text.replace(symbol, " ")

  
    words = text.split()

  
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] = freq_dict[word] + 1
        else:
            freq_dict[word] = 1

   
    most_frequent_word = ""
    max_count = 0

    for word in freq_dict:
        if freq_dict[word] > max_count:
            max_count = freq_dict[word]
            most_frequent_word = word

   
    longest_repeated_word = ""
    max_length = 0

    for word in freq_dict:
        if freq_dict[word] > 1:  
            if len(word) > max_length:
                max_length = len(word)
                longest_repeated_word = word
            elif len(word) == max_length and word < longest_repeated_word:
                
                longest_repeated_word = word

    return most_frequent_word, max_count, longest_repeated_word



input_text = "The cat sat. The CAT ran! The dog barked, but the cat slept."
top_word, count, longest_word = analyze_paragraph(input_text)

print("Most frequent word:", f"'{top_word}' ({count} times)")
print("Longest repeated word:", f"'{longest_word}'.")
