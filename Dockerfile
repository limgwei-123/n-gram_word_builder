FROM python:3.11-slim

WORKDIR /app

COPY ngram_gen ./ngram_gen
COPY data ./data

CMD [ "python", "-m", "ngram_gen.cli", "data/sample_corpus.txt", "3"]