import nltk
import tokenize
class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        # load positive words
        self.positives = set()
        self.negatives = set()
        
        file = open('positive-words.txt','r')
        for line in file:
            if line.startswith(';'):
                continue
            self.positives.add(line.strip("\n"))
        file.close()
        # load negative words
        filen= open('negative-words.txt','r')
        for line in filen:
            if line.startswith(';'):
                continue
            self.negatives.add(line.strip("\n"))
        filen.close()

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
         
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        
        score = 0
        for token in tokens:
            if token.lower() in self.positives:
                score = score + 1
                #print(token)
            elif token.lower() in self.negatives:
                score = score - 1
                #print(token)
            else:
                score = score + 0
            
        #print(score)
        return score
        
        
