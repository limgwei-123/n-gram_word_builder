from ngram_gen.tokenize import tokenize_sentence_char_level, add_sentence_tokens

def test_char_tokenize():
  sent = "我爱你"
  tokens = tokenize_sentence_char_level(sent)
  assert tokens == ["我","爱","你"]

def test_add_sentences_tokens_trigram():
  tokens = ["我","爱","你"]
  out = add_sentence_tokens(tokens, n=3)
  assert out == ["<s>", "<s>", "我", "爱", "你", "</s>"]