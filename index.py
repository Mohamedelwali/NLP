import csv
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import nltk


# Function to perform tokenization and stemming
def preprocess_text(text):
    # Tokenization
    tokens = word_tokenize(text.lower())  # Convert text to lowercase for consistency
    
    # Stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    
    return stemmed_tokens

# Read CSV file
def read_csv_file(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

# Main function
def main():
    filename = "SPAM text message 20170820 - Data.csv"  
    dataset = read_csv_file(filename)
    
    # Assuming the text is in the first column of each row
    for row in dataset:
        text = row[1]
        tokens = preprocess_text(text)
        print("Original text:", text)
        print("Preprocessed tokens:", tokens)
        print()

if __name__ == "__main__":
    main()
