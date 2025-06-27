from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize analyzer
sia = SentimentIntensityAnalyzer()

# Input message
message = input("Friend's Message: ")

# Get sentiment scores
score = sia.polarity_scores(message)
print("\nSentiment Score:", score)

# Emotion override keywords
emotion_keywords = {
    'happy': ['passed', 'congrats', 'excited', 'awesome', 'great', 'joy', 'love'],
    'sad': ['nothing', 'wrong', 'tired', 'alone', 'bad', 'down', 'depressed','low'],
}

# Lowercase message for keyword match
lower_msg = message.lower()
found_emotion = None

# Check if any emotion keyword is in the message
for emo, keywords in emotion_keywords.items():
    if any(word in lower_msg for word in keywords):
        found_emotion = emo
        break

# Use keyword emotion if found, else fallback to VADER sentiment
if found_emotion:
    emotion = found_emotion
else:
    if score['compound'] >= 0.5:
        emotion = 'happy'
    elif score['compound'] <= -0.5:
        emotion = 'sad'
    else:
        emotion = 'neutral'

print("Detected Emotion:", emotion)

# Auto-reply mapping
auto_replies = {
    'happy': "😊 I'm glad you're feeling good!",
    'sad': "😢 I'm here for you. Take care!",
    'neutral': "👍 Got it. Let me know if you need anything."
}

# Generate and show reply
reply = auto_replies.get(emotion, "🤖 I'm not sure how to respond.")
print("Auto-Reply:", reply)
# Log the chat to a file with emoji-safe encoding
with open("chat_log.txt", "a", encoding="utf-8") as log:
    log.write(f"Message: {message}\n")
    log.write(f"Emotion: {emotion}\n")
    log.write(f"Reply: {reply}\n")
    log.write("-" * 40 + "\n")
