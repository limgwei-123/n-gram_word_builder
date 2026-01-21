from collections import defaultdict

from ngram_gen.tokenize import add_sentence_tokens, tokenize_sentence_char_level

def build_ngram_counts(sentences, n:int):
    context_counts = defaultdict(int)
    next_counts = defaultdict(int)

    for sent in sentences:
        tokens = tokenize_sentence_char_level(sent)
        tokens = add_sentence_tokens(tokens, n)

        for i in range (n - 1, len(tokens)):
            context = tuple(tokens[i - (n-1):i])
            nxt = tokens[i]
            context_counts[context] += 1
            next_counts[(context, nxt)] += 1

    return context_counts, next_counts