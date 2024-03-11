import nltk

def tokenize_text(text, choice):
  tokens = []
  if choice == 1:
    tokens = nltk.word_tokenize(text)
  elif choice == 2:
    tokens = nltk.sent_tokenize(text)
  elif choice == 3:
    tokens = text.split()
  else:
    print("Invalid choice. Please enter 1, 2, or 3.")
  return tokens

def main():
  nltk.download('punkt')

  text = input("Enter your text: ")
  print("\nChoose an option:")
  print("1. Print tokenized words")
  print("2. Print tokenized sentences")
  print("3. Print output using split function")
  choice = int(input("Enter your choice: "))

  tokens = tokenize_text(text, choice)
  print("\nOutput:")
  print(tokens)

if __name__ == "__main__":
  main()

"""
the text is: NLTK is a leading platform for building Python programs to work with human language data. NLTK is available for Windows, Mac OS X, and Linux. Best of all, NLTK is a free, open source, community-driven project.
"""

