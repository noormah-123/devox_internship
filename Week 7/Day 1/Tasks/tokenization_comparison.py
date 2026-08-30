from transformers import AutoTokenizer

# Sample paragraph
text = (
    "Artificial intelligence is changing the way we work. "
    "Machine learning models can analyze data and make useful predictions."
)

# -------------------------------
# Manual Tokenization
# -------------------------------

manual_tokens = text.split()

print("MANUAL TOKENIZATION")
print("-------------------")
print(manual_tokens)
print("Number of tokens:", len(manual_tokens))


# -------------------------------
# Hugging Face Tokenization
# -------------------------------

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

hf_tokens = tokenizer.tokenize(text)

print("\nHUGGING FACE TOKENIZATION")
print("------------------------")
print(hf_tokens)
print("Number of tokens:", len(hf_tokens))


# -------------------------------
# Comparison
# -------------------------------

print("\nCOMPARISON")
print("----------")
print("Manual tokens:", len(manual_tokens))
print("Hugging Face tokens:", len(hf_tokens))

if len(manual_tokens) != len(hf_tokens):
    print(
        "\nThe Hugging Face tokenizer produces a different number "
        "of tokens because it uses subword tokenization."
    )
else:
    print("\nBoth methods produced the same number of tokens.")