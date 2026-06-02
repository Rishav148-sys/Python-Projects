import string

def word_frequency(text):
    
    text = text.lower()

    
    text = text.translate(str.maketrans("", "", string.punctuation))

   
    words = text.split()

    
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    
    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

   
    return sorted_words[:3]


# Test text
text = """
Nepal is a beautiful country. Nepal has Mount Everest.
Everest is the highest mountain in the world.
Many tourists visit Nepal every year to see Everest and other mountains.
Nepal is known for its mountains and natural beauty.
"""

# Display results
top3 = word_frequency(text)
print("Top 3 words:")
for word, count in top3:
    print(f"  {word} — {count} times")