
import re

def tokenize_text_to_sentences(text: str):
    sents = re.split(r"[。？！\n]", text)
    sents = [s.strip() for s in sents if s.strip()]
    return sents

def tokenize_sentence_char_level(sent: str):
    sent = re.sub(r"\s+", "", sent)
    return list(sent)

def add_sentence_tokens(tokens, n):
    return ["<s>"] * (n - 1) + tokens + ["</s>"]