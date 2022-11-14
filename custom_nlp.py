import string
from sklearn.preprocessing import FunctionTransformer
from nltk.tokenize import word_tokenize
import numpy as np

def preprocess(docs):
    """
    Prepare data from text documents for NLP:
    - Remove all the special characters
    - Remove all single characters
    - Substitute multiple spaces with single space
    - Convert to Lowercase

    Parameters:
    docs (n x 1 array or string): Documents.

    Returns: Array of processed docs.
    """
    clean_docs = []
    for doc in docs:
        # Split text into single words (also gets rid of extra white spaces)
        words = word_tokenize(doc)
        # Convert to lower case
        words = [word.lower() for word in words]

        # Remove all single characters
        words = [word for word in words if len(word) > 2]
        
        # join words back together as a string
        words = ''.join([word+' ' for word in words])

        # remove special characters
        processed = ''.join([char for char in words if not char in string.punctuation])
        
        clean_docs.append(processed)
    return np.array(clean_docs)