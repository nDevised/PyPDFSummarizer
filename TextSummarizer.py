from nltk import sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


class TextSummarizer:
    def __init__(self, text):
        self.text = text

    def __get_lemmatized_tokens(self, text):
        lemmatizer = WordNetLemmatizer()
        return [lemmatizer.lemmatize(token) for token in word_tokenize(text.lower())]

    def __tokenize(self, text):
        return sent_tokenize(self.text)

    def __TFIDF(self, tokenized):
        return TfidfVectorizer(tokenizer=self.__get_lemmatized_tokens, stop_words=stopwords.words('english')).fit_transform(tokenized)

    def __average_TFIDF(self, values):
        greater_than_zero_count = np.count_nonzero(values)
        total = np.sum(values)
        return total / greater_than_zero_count

    def __default_threshold(self, TFIDF_res):
        average_TFIDF = np.mean(np.asarray(TFIDF_res.toarray()))
        return average_TFIDF

    def summarize(self, length_percent):
        HANDICAP = 1 - length_percent

        # Tokenize the text
        tokenized = self.__tokenize(self.text)

        # Lemmatize and ignore stop words in tokens
        TFIDF_res = self.__TFIDF(tokenized)

        # Get the threshold
        threshold = self.__default_threshold(TFIDF_res)

        summary = ""
        for i in range(TFIDF_res.shape[0]):
            if self.__average_TFIDF(TFIDF_res[i, :].toarray()[0]) >= threshold * HANDICAP:
                summary += ' ' + tokenized[i]

        return summary.strip()
