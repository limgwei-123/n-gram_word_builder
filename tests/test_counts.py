from ngram_gen.model import build_ngram_counts

def test_bigram_counts_simple():
  sentences = ["aba"]
  context_counts, next_counts = build_ngram_counts(sentences, n=2)

  assert next_counts[(("<s>",), "a")] == 1

  assert next_counts[(("a",), "b")] == 1

  assert next_counts[(("b",), "a")] == 1

  assert next_counts[(("a",), "</s>")] == 1