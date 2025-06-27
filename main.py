import spacy
import csv

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load your meal plan (from .txt for now)
with open("meal_plan.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Process the text
doc = nlp(text)

# Keywords to detect ingredients and their categories
ingredient_categories = {
    "vegetables": ["tomato", "potato"],
    "grains": ["rice", "chapati", "idli", "dosa"],
    "spices": ["masala", "chutney", "sambar"]
}

# Flat list for detection
all_ingredients = [item for sublist in ingredient_categories.values() for item in sublist]

# Extract and categorize
unique_ingredients = set()
categorized = {}

for token in doc:
    word = token.text.lower()
    if word in all_ingredients:
        unique_ingredients.add(word)

# Group by category
for category, items in ingredient_categories.items():
    categorized[category] = [item for item in unique_ingredients if item in items]

# Write to CSV
with open("grocery_list.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Category", "Ingredient"])
    for category, items in categorized.items():
        for item in sorted(items):
            writer.writerow([category.capitalize(), item])

print("✅ Grocery list saved as grocery_list.csv")
