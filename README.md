 # Mini Project 1 – Emotion WhatsApp Bot

This is a simple Python-based chatbot that detects the **emotion** behind a WhatsApp-style message and automatically responds with a suitable reply. 
It uses **VADER sentiment analysis** and custom keyword-based emotion detection logic.

 # Features

- Analyzes user input and detects emotional tone (happy, sad, neutral)
- Uses both sentiment scores and custom keyword matching
- Sends a context-aware auto-reply
- Logs each conversation to a local file (`chat_log.txt`)

# Technologies Used

- Python 3
- `nltk` (VADER SentimentIntensityAnalyzer)
- File handling for logging

# Install required packages:

  pip install nltk

# Run the script:

  python main.py

#  Example:

   Friend's Message: I passed my exams
   Sentiment Score: {'neg': 0.0, 'neu': 0.17, 'pos': 0.83, 'compound': 0.93}
   Detected Emotion: happy
   Auto-Reply: 😄 That's awesome! So happy for you!

# Files:

- main.py – Main script to run the bot
- chat_log.txt – Stores the history of conversations
- README.md – Project overview and instructions

## This is a part of Final Project:
      
  This is Mini Project 1 in a collection of emotion-based automation tools, which will be combined into a final AI-powered Emotion Dashboard for daily life task automation.



