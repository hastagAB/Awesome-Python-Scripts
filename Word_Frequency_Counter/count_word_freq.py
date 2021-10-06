import argparse
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
import re
import string


def preprocess(text: str) -> str:
    """
    Pre-process the input text.
    
    - Remove punctuation
    - Remove numbers
    - Lowercase
    
    :param text: text to pre-process
    :return: the pre-processed text
    """
    # Lowercase.
    text = text.lower()
    # Remove numbers.
    text = re.sub(r"[0-9]+", "", text)
    # Remove punctuation.
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text


def run(text: str) -> FreqDist:
    """
    Count the word frequencies in a text.
    
    The text is pre-processed beforehand to remove uninformative
    tokens such as punctuation, numbers, stopwords, and to unify
    the same tokens by lowercasing the text.
    
    :param text: text to count the word frequencies in
    :return: the word frequencies in the text
    """
    # Pre-process the text.
    text = preprocess(text)
    # Tokenize the text.
    tokens = word_tokenize(text)
    # Remove stopwords.
    stop_words = set(stopwords.words("english"))
    tokens = [token for token in tokens if token not in stop_words]
    # Count the frequencies.
    freq_dist = FreqDist(tokens)
    print("Top 10 most frequent words:")
    print(freq_dist.most_common(10))
    return freq_dist
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--filepath",
        "-f",
        required=True,
        help="path to the text file"
    )
    args = parser.parse_args()
    # Open the text file.
    with open(args.filepath, "r") as f:
        text = f.read()
    # Count the frequencies.
    freq_dist = run(text)
    freq_dist_str = "\n".join([str(x) for x in freq_dist.most_common(freq_dist.B())])
    # Save the result.
    old_file_name = args.filepath.split("/")[-1].split(".")[0]
    new_file_name = old_file_name + "_freq_dist"
    new_filepath = args.filepath.replace(old_file_name, new_file_name)
    with open(new_filepath, "w") as f:
        f.write(freq_dist_str)
    print(f"\nSaved the word frequencies to '{new_filepath}'")
    

