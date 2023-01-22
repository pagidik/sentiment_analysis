from transformers import DistilBertForSequenceClassification, DistilBertTokenizer
import torch

# Load the pre-trained model and tokenizer
model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased")
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")

# Initialize a list to store the sentiment scores
sentiment_scores = []

# Loop through each review
with open("data/reviews.txt", "r") as file:
    reviews = file.readlines()
    # Encode the review
    input_ids = torch.tensor(tokenizer.encode(reviews, add_special_tokens=True)).unsqueeze(0)
    # Get the sentiment scores
    outputs = model(input_ids)
    sentiment = torch.softmax(outputs[0], dim=1).squeeze(0)
    # Append the sentiment score to the list
    sentiment_scores.append(sentiment.tolist())

# Print the sentiment scores
print(sentiment_scores)