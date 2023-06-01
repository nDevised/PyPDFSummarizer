from nltk import sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

class TextSummarizer:
    def __init__(self, text, threshold):
        self.text = text
        self.threshold = threshold
    def __get_lemmatized_tokens(self, text):
        lemmatizer = WordNetLemmatizer()
        return [lemmatizer.lemmatize(token) for token in word_tokenize(text.lower())]

    def __TFIDF(self):
        documents = sent_tokenize(self.text)
        return TfidfVectorizer(tokenizer=self.__get_lemmatized_tokens, stop_words=stopwords.words('english')).fit_transform(documents)

    def summarize(self):
        """
        Run the text summarization algorithm
        :return: None
        """
        TFIDF = self.__TFIDF()
