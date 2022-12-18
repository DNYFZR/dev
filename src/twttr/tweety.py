# Twitter Analytics Class
import pandas as pd, re

class TwitterAnalytics:
    """
        This class will take a twitter analytics download of data 'by-tweet'.
        It also takes an optional list of words / characters to identify if they are present in the tweet text 
    """
    
    def __init__(self, dataset, text_column, min_word_len, search_chars = None, keep_cols = None):
        self.dataset = dataset
        self.text = text_column
        self.min_len = min_word_len
        self.search_chars = search_chars
        self.keep_cols = keep_cols

        
    def __read_data(self):
        if self.keep_cols is not None:
            self.data = pd.read_csv(self.dataset, parse_dates=['time'], usecols=self.keep_cols)
        else:
            self.data = pd.read_csv(self.dataset, parse_dates=['time'])


    def __drop_cols(self):
        drop_cols = [
            'app opens', 'app installs','email tweet', 'dial phone', 'promoted impressions', 'promoted engagements',
            'promoted engagement rate', 'promoted retweets', 'promoted replies', 'promoted likes', 'promoted user profile clicks', 
            'promoted url clicks','promoted hashtag clicks', 'promoted detail expands','promoted permalink clicks', 
            'promoted app opens','promoted app installs', 'promoted follows', 'promoted email tweet',
            'promoted dial phone', 'promoted media views','promoted media engagements']

        for col in self.data.columns:
            if col in drop_cols:
                del self.data[col]
                

    def __clean_data(self):
        # Add Date Column (Mon = 1)
        self.data['day_no'] = self.data['time'].dt.dayofweek + 1

        # Day of month
        self.data['month_day'] = self.data['time'].dt.day

        # Round to nearest hour
        hours = {}
        for i in self.data['time'].to_numpy():
            if i.minute < 30:
                j = i.hour 
            else:
                j = i.hour + 1
            if j == 0:
                j = 24
            hours.update({i:j})
        
        self.data['hour'] = self.data['time'].map(hours)


    def __tokenize_text(self):
        tokens = [i.replace('\n', ' ').lower().split(' ') for i in self.data[self.text].to_list()]

        for i, row_tokens in enumerate(tokens):
            new_row_tokens = []
            for t in row_tokens:
                t = t.strip().replace("'", "")
                if len(t) >= self.min_len:
                    new_row_tokens.append(t)
            tokens[i] = new_row_tokens

        self.data['tokens'] = tokens
    

    def __tag_text_containing(self, character):
        items = []
        char_list = self.data[self.text].to_list()
        
        for chars in char_list:
            if re.search(character, chars):
                items.append(1)
            else:
                items.append(0)

        self.data[f'tweet_{character}'] = items
        
        
    def run_analytics(self):
        # Extract
        self.__read_data()

        # Transform
        if self.keep_cols is not None:
            self.__drop_cols()
            
        self.__clean_data()

        if self.search_chars is not None:
            self.__tokenize_text()

            # Add identifier cols
            for char in self.search_chars:
                self.__tag_text_containing(char)

        return self.data

if __name__ == '__main__':
    # import os
    import datetime as dt
    from time import time
    date = dt.datetime.strftime(dt.datetime.today(), '%Y-%m-%d')
    
    start = time()
    search_terms = ['@', '#', 'python', 'sql', 'data', 'analytics', 'data engineer', 'machine learning']
    
    output = TwitterAnalytics(r'data/AllTweets.csv', 'Tweet text', search_chars=search_terms, min_word_len=3).run_analytics()

    print(f'Script completed: {round(time() - start, 1)}s')
    output.to_csv(f'data/TwitterAnalyticsClass_{date}.csv')
