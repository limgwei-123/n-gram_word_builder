import sys
import random
from pathlib import Path

from ngram_gen.tokenize import tokenize_text_to_sentences
from ngram_gen.model import build_ngram_counts
from ngram_gen.generate import generate_text

def main():

  if len(sys.argv) < 3:
    print("Usage: python -m ngram_gen.cli <sample_corpus.txt> <n>"
    )
    sys.exit(1)

  corpus_path = Path(sys.argv[1])
  n = int(sys.argv[2])

  text = corpus_path.read_text(encoding="utf-8")
  sentences = tokenize_text_to_sentences(text)

  context_counts, next_counts = build_ngram_counts(sentences, n)

  random.seed(42)
  for _ in range(5):
    sentence = generate_text(
      n = n,
      context_counts = context_counts,
      next_counts= next_counts,

      max_len= 50
    )
    print(sentence)

if __name__ == "__main__":
  main()