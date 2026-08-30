from transformers import pipeline

# Load the pretrained sentiment-analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# 5 sample sentences
sentences = [
    "I absolutely love this product.",
    "The movie was amazing and very enjoyable.",
    "The weather is okay today.",
    "I am disappointed with the service.",
    "This is the worst experience I have ever had."
]

# Run sentiment analysis
results = sentiment_pipeline(sentences)

# Display results
print("SENTIMENT ANALYSIS RESULTS")
print("--------------------------")

for sentence, result in zip(sentences, results):
    print(f"\nSentence: {sentence}")
    print(f"Sentiment: {result['label']}")
    print(f"Confidence: {result['score']:.4f}")

# Simple comparison
print("\n\nCOMPARISON")
print("----------")

positive = 0
negative = 0

for result in results:
    if result["label"] == "POSITIVE":
        positive += 1
    else:
        negative += 1

print(f"Positive sentences: {positive}")
print(f"Negative sentences: {negative}")