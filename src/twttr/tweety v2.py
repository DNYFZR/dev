# Tweety.py
# Twitter Data Analytics
import sys, re, numpy as np, pandas as pd
sys.path.append('../')

class twttr:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data: pd.DataFrame | None = None

    def get_data(self, date_columns: list | None = None, index_col: str | int | None = None):
        '''Get data from init source'''
        self.data = pd.read_csv(self.filepath, parse_dates=date_columns, index_col=index_col)
        return self

    def clean_data(self, keyword_col: str | None = None, keywords: list | None = None):
        '''Clean data for further analysis'''
        if keywords is not None and keyword_col is not None:
            
            for row in self.data[keyword_col]:
                continue

        return self

    def analyse_data(self):
        '''Analyse the data'''
        
        return self

    def collect_results(self):
        '''Aggregate the results'''
        
        return self

    def save_results(self):
        '''Save the output to csv'''
        
        return self

    def run(self, save_results: bool = False):
        '''Run the class methods sequentially'''
        self.get_data()
        self.clean_data()
        self.analyse_data()
        self.collect_results()

        if save_results:
            self.save_results()
        
        return self