import pandas as pd
import ipdb

class LoadSST2:
    @staticmethod
    def en2en():
        train_path = '../Koglish_dataset/Koglish_GLUE/sst2/parsed_train.csv'
        valid_path = '../Koglish_dataset/Koglish_GLUE/sst2/parsed_valid.csv'
        test_path = '../Koglish_dataset/Koglish_GLUE/sst2/parsed_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
    @staticmethod
    def en2cross():
        train_path = '../Koglish_dataset/Koglish_GLUE/sst2/parsed_train.csv'
        valid_path = '../Koglish_dataset/Koglish_GLUE/sst2/parsed_valid.csv'
        test_path = '../Koglish_dataset/Koglish_GLUE/sst2/cross_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data, valid_data, test_data
    @staticmethod
    def cross2cross():
        train_path = '../Koglish_dataset/Koglish_GLUE/sst2/cross_train.csv'
        valid_path = '../Koglish_dataset/Koglish_GLUE/sst2/cross_valid.csv'
        test_path = '../Koglish_dataset/Koglish_GLUE/sst2/cross_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data, valid_data, test_data
    
class LoadMRPC:
    @staticmethod
    def en2en():
        train_path = '../Koglish_dataset/Koglish_GLUE/mrpc/parsed_train.csv'
        valid_path = '../Koglish_dataset/Koglish_GLUE/mrpc/parsed_valid.csv'
        test_path = '../Koglish_dataset/Koglish_GLUE/mrpc/parsed_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
    @staticmethod
    def en2cross():
        train_path = '../Koglish_dataset/Koglish_GLUE/mrpc/parsed_train.csv'
        valid_path = '../Koglish_dataset/Koglish_GLUE/mrpc/parsed_valid.csv'
        test_path = '../Koglish_dataset/Koglish_GLUE/mrpc/cross_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
    @staticmethod
    def cross2cross():
        train_path = '../Koglish_dataset/Koglish_GLUE/mrpc/cross_train.csv'
        valid_path = '../Koglish_dataset/Koglish_GLUE/mrpc/cross_valid.csv'
        test_path = '../Koglish_dataset/Koglish_GLUE/mrpc/cross_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
class LoadCOLA:
    @staticmethod
    def en2en():
        train_path = '../Koglish_dataset/Koglish_GLUE/cola/parsed_train.csv'
        valid_path = '../Koglish_dataset/Koglish_GLUE/cola/parsed_valid.csv'
        test_path = '../Koglish_dataset/Koglish_GLUE/cola/parsed_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
    @staticmethod
    def en2cross():
        train_path = '../Koglish_dataset/Koglish_GLUE/cola/parsed_train.csv'
        valid_path = '../Koglish_dataset/Koglish_GLUE/cola/parsed_valid.csv'
        test_path = '../Koglish_dataset/Koglish_GLUE/cola/cross_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
    @staticmethod
    def cross2cross():
        train_path = '../Koglish_dataset/Koglish_GLUE/cola/cross_train.csv'
        valid_path = '../Koglish_dataset/Koglish_GLUE/cola/cross_valid.csv'
        test_path = '../Koglish_dataset/Koglish_GLUE/cola/cross_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
class LoadRTE:
    @staticmethod
    def en2en():
        train_path = '../Koglish_dataset/Koglish_GLUE/rte/parsed_train.csv'
        valid_path = '../Koglish_dataset/Koglish_GLUE/rte/parsed_valid.csv'
        test_path = '../Koglish_dataset/Koglish_GLUE/rte/parsed_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
    @staticmethod
    def en2cross():
        train_path = '../Koglish_dataset/Koglish_GLUE/rte/parsed_train.csv'
        valid_path = '../Koglish_dataset/Koglish_GLUE/rte/parsed_valid.csv'
        test_path = '../Koglish_dataset/Koglish_GLUE/rte/cross_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
    @staticmethod
    def cross2cross():
        train_path = '../Koglish_dataset/Koglish_GLUE/rte/cross_train.csv'
        valid_path = '../Koglish_dataset/Koglish_GLUE/rte/cross_valid.csv'
        test_path = '../Koglish_dataset/Koglish_GLUE/rte/cross_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data

class LoadSTSB:
    @staticmethod
    def en2en():
        train_path = '../Koglish_dataset/Koglish_GLUE/stsb/parsed_train.csv'
        valid_path = '../Koglish_dataset/Koglish_GLUE/stsb/parsed_valid.csv'
        test_path = '../Koglish_dataset/Koglish_GLUE/stsb/parsed_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
    @staticmethod
    def en2cross():
        train_path = '../Koglish_dataset/Koglish_GLUE/stsb/parsed_train.csv'
        valid_path = '../Koglish_dataset/Koglish_GLUE/stsb/parsed_valid.csv'
        test_path = '../Koglish_dataset/Koglish_GLUE/stsb/cross_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
    @staticmethod
    def cross2cross():
        train_path = '../Koglish_dataset/Koglish_GLUE/stsb/cross_train.csv'
        valid_path = '../Koglish_dataset/Koglish_GLUE/stsb/cross_valid.csv'
        test_path = '../Koglish_dataset/Koglish_GLUE/stsb/cross_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
    
class LoadQNLI:
    @staticmethod
    def en2en():
        train_path = '../Koglish_dataset/Koglish_GLUE/qnli/parsed_train.csv'
        valid_path = '../Koglish_dataset/Koglish_GLUE/qnli/parsed_valid.csv'
        test_path = '../Koglish_dataset/Koglish_GLUE/qnli/parsed_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
    @staticmethod
    def en2cross():
        train_path = '../Koglish_dataset/Koglish_GLUE/qnli/parsed_train.csv'
        valid_path = '../Koglish_dataset/Koglish_GLUE/qnli/parsed_valid.csv'
        test_path = '../Koglish_dataset/Koglish_GLUE/qnli/cross_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
    @staticmethod
    def cross2cross():
        train_path = '../Koglish_dataset/Koglish_GLUE/qnli/cross_train.csv'
        valid_path = '../Koglish_dataset/Koglish_GLUE/qnli/cross_valid.csv'
        test_path = '../Koglish_dataset/Koglish_GLUE/qnli/cross_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data


    
