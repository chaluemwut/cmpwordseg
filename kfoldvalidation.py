from os import listdir
import glob
import fnmatch
from util import FileUtil
from crf import CRF
import random
import numpy as np
from sklearn.cross_validation import KFold

class KFoldValidataion:
    base_dir_out = 'kfold/'
#     best_corpus = {'article':16990,
#                    'encyclopedia':50631,
#                    'news':31234,
#                    'novel':50140}
    fileUtil = FileUtil()
    crf = CRF()
    corpus = []
    
    def remove_ne(self, message):
        return message.replace('<NE>', '').replace('</NE>', '').replace('<AB>', '').replace('</AB>', '')
    
    def create_result_data(self, message):
        self.fileUtil.write_file_no_n(self.base_dir_out + 'result/result' + str(self.fold_number), message)
    
    def create_test_data(self, message):
        test_message = self.remove_ne(message)
        lst_msg = test_message.split('|')[:-1]
        file_msg = ''.join(lst_msg)
        self.fileUtil.write_file(self.base_dir_out + 'test/test' + str(self.fold_number), file_msg)
        
    def create_train_data(self, message):
        test_message = self.remove_ne(message)
        lst_message = test_message.split('|')
        for i in range(len(lst_message) - 1):
            sep_message = lst_message[i]
            train_message = self.crf.create_train_message(sep_message)
            self.fileUtil.write_file_no_n(self.base_dir_out + 'train/train' + str(self.fold_number), train_message)

    def create_kfold(self):
        best_dir = 'best/all/'
        for f in listdir(best_dir):
            str_file = best_dir + f
            line = self.fileUtil.read_file(str_file)
            self.corpus = self.corpus + line
             
        random.shuffle(self.corpus)
        kf = KFold(len(self.corpus), n_folds=5)
        self.fold_number = 1;
        for train, test in kf:
            for data_train in train:
                print 'train ', data_train , self.corpus[data_train]
                self.create_train_data(self.corpus[data_train])
            for data_test in test:
                print 'test ', data_test, self.corpus[data_test]
                self.create_result_data(self.corpus[data_test])
                self.create_test_data(self.corpus[data_test])
            self.fold_number = self.fold_number + 1

kFold = KFoldValidataion()
kFold.create_kfold()
