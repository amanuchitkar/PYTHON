def count_keywords(file_path, keywords):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            word_list = content.split()
            count = 0
            for word in word_list:
                if word.lower() in keywords:
                    count += 1
            return count
    except FileNotFoundError:
        print("File not found.")
        return -1

# List of keywords
keywords = ["if", "else", "elif", "for", "while", "def", "class", "import", "from", "return"]

# Example usage
file_path = "keywordFinder.py"  # Replace with the path to your file
keyword_count = count_keywords(file_path, keywords)
if keyword_count != -1:
    print("Number of keywords in the file:", keyword_count)
