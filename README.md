# Smart Grocery List Generator:

This Python mini project automatically extracts ingredients from your weekly meal plan and generates a clean, categorized grocery list.

# Features:
-  NLP-powered ingredient extraction using **spaCy**
-  Removes duplicates and sorts alphabetically
- Tags ingredients into categories like:
  - 🥦 **Vegetables**
  - 🍞 **Grains**
  - 🥫 **Spices**
- Outputs to a CSV file (`grocery_list.csv`)

## 🛠 Requirements:
Install dependencies with:

pip install -r requirements.txt


# How It Works:
1. Add your weekly meal plan in `meal_plan.txt`.
2. Run the script:
   ```bash
   python main.py
   ```
3. You'll get a neatly organized `grocery_list.csv`.

# Files:
- `main.py` – Core script
- `meal_plan.txt` – Weekly meal plan input
- `grocery_list.csv` – Output file
- `requirements.txt` – Required packages

#  Author:

[Nirupama1009](https://github.com/Nirupama1009)

# To Do Next:
- Add GUI using Tkinter
- Add quantity estimation
- Add PDF download support
