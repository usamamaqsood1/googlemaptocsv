# Define the text file name
text_file = "Delta.txt"
import pandas as pd

# Initialize a list to store the questions and scenarios
questions = []

# Open and read the text file with UTF-8 encoding
with open(text_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

    # Initialize a variable to store the current question/scenario
    current_question = ""

    for line in lines:
        # Strip leading/trailing whitespaces
        line = line.strip()

        if line:
            # If the line is not empty, append it to the current question/scenario
            current_question += line + " "
        elif current_question:
            # If a blank line is encountered and we have a current question, add it to the list
            questions.append(current_question.strip())
            current_question = ""

# Print the extracted questions and scenarios
for i, question in enumerate(questions):
    print(f"Question {i + 1}: {question}")

# You can now use this list of questions and scenarios as needed.
csv_file = "test.csv"
df = pd.DataFrame({'Question': questions})
# Save the DataFrame to a CSV file
df.to_csv(csv_file, index=False)

print(f"Questions have been saved to {csv_file}")