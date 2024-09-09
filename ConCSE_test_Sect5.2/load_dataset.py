import pandas as pd
import ipdb

class LoadNLI:
    @staticmethod
    def en_train():
        train_path = '../Koglish_dataset/Koglish_NLI/parsed_train.csv' 
        train_data = pd.read_csv(train_path, sep=',')
        return train_data 
    @staticmethod
    def cross_train():
        train_path = '../Koglish_dataset/Koglish_NLI/cross_train.csv' 
        train_data = pd.read_csv(train_path, sep=',')
        return train_data
    
class LoadSTSB:
    @staticmethod
    def en_valid():
        valid_path = '../Koglish_dataset/Koglish_STS/stsb_for_Koglish/en_valid.csv' 
        valid_data = pd.read_csv(valid_path, sep=',')
        return valid_data
    def en_test():
        test_path = '../Koglish_dataset/Koglish_STS/stsb_for_Koglish/en_test.csv' 
        test_data = pd.read_csv(test_path, sep=',')
        return test_data
    
    @staticmethod
    def cross_valid():
        valid_path = '../Koglish_dataset/Koglish_STS/stsb_for_Koglish/cross_valid.csv'  
        valid_data = pd.read_csv(valid_path, sep=',')
        return valid_data
    def cross_test():
        test_path = '../Koglish_dataset/Koglish_STS/stsb_for_Koglish/cross_test.csv'  
        test_data = pd.read_csv(test_path, sep=',')
        return test_data
    
class TestLoadSTS_12:
    def __init__(self, args):
        self.eval_type = args.eval_type
    def en_test(self):
        if self.eval_type == 'transfer':
            
            test_path = '../Koglish_dataset/Koglish_STS/sts_12_16/sts12/parsed_test.csv' 
        test_data = pd.read_csv(test_path, sep=',')
        return test_data
    
    def cross_test(self):
        if self.eval_type == 'transfer':
            test_path = '../Koglish_dataset/Koglish_STS/sts_12_16/sts12/cross_test.csv' 
        test_data = pd.read_csv(test_path, sep=',')
        return test_data

class TestLoadSTS_13:
    def __init__(self, args):
        self.eval_type = args.eval_type
    def en_test(self):
        if self.eval_type == 'transfer':
            test_path = '../Koglish_dataset/Koglish_STS/sts_12_16/sts13/parsed_test.csv' 
            test_data = pd.read_csv(test_path, sep=',')
        return test_data
    
    def cross_test(self):
        if self.eval_type == 'transfer' :
            test_path = '../Koglish_dataset/Koglish_STS/sts_12_16/sts13/cross_test.csv'  
            test_data = pd.read_csv(test_path, sep=',')
        return test_data

class TestLoadSTS_14:
    def __init__(self, args):
        self.eval_type = args.eval_type
    def en_test(self):
        if self.eval_type == 'transfer':
            test_path = '../Koglish_dataset/Koglish_STS/sts_12_16/sts14/parsed_test.csv'  
            test_data = pd.read_csv(test_path, sep=',')
        return test_data
    def cross_test(self):
        if self.eval_type == 'transfer' :
            test_path = '../Koglish_dataset/Koglish_STS/sts_12_16/sts14/cross_test.csv'  
            test_data = pd.read_csv(test_path, sep=',')
        return test_data

class TestLoadSTS_15:
    def __init__(self, args):
        self.eval_type = args.eval_type
    def en_test(self):
        if self.eval_type == 'transfer':
            test_path = '../Koglish_dataset/Koglish_STS/sts_12_16/sts15/parsed_test.csv' 
            test_data = pd.read_csv(test_path, sep=',')
        return test_data
    
    def cross_test(self):
        if self.eval_type == 'transfer' :
            test_path = '../Koglish_dataset/Koglish_STS/sts_12_16/sts15/cross_test.csv'
            test_data = pd.read_csv(test_path, sep=',')
        return test_data

class TestLoadSTS_16:
    def __init__(self, args):
        self.eval_type = args.eval_type
    def en_test(self):
        if self.eval_type == 'transfer':
            test_path = '../Koglish_dataset/Koglish_STS/sts_12_16/sts16/parsed_test.csv'  
            test_data = pd.read_csv(test_path, sep=',')
        return test_data
    
    def cross_test(self):
        if self.eval_type == 'transfer' :
            test_path = '../Koglish_dataset/Koglish_STS/sts_12_16/sts16/cross_test.csv' 
            test_data = pd.read_csv(test_path, sep=',')
        return test_data

class TestLoadSICK:
    def __init__(self, args):
        self.eval_type = args.eval_type
    def en_test(self):
        if self.eval_type == 'transfer':
            test_path = '../Koglish_dataset/Koglish_STS/sick/parsed_test.csv' 
        test_data = pd.read_csv(test_path, sep=',')
        return test_data
    
    def cross_test(self):
        if self.eval_type == 'transfer' :
            test_path = '../Koglish_dataset/Koglish_STS/sick/cross_test.csv'
        test_data = pd.read_csv(test_path, sep=',')
        return test_data

    