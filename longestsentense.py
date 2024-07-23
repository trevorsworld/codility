def solution(S):
    import re
    
    sentences = re.split(r'[.?!]', S)

    def word_count(sentence):

        return len([word for word in sentence.split() if word])

    max_words = max(word_count(sentence) for sentence in sentences)

    return max_words

S1 = "We test coders. Give us a try?"
S2 = "Forget CVs.. Save time . x x"

print(solution(S1))  # Output: 4
print(solution(S2))  # Output: 2