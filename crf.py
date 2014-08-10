# -*- coding: utf-8 -*-

from os import listdir
from util import FileUtil
import codecs


class CRF:
    
    c_group = [u'ก', u'ข', u'ฃ', u'ค', u'ฆ', u'ง', u'จ', u'ช', u'ซ', u'ญ', u'ฎ', u'ฐ', u'ฑ', 
               u'ฒ', u'ณ', u'ด', u'ต', u'ถ', u'ท', u'ธ', u'น', u'บ', u'ป', u'พ',u'ฟ', u'ภ', u'ม', 
               u'ย', u'ร', u'ล', u'ว', u'ศ', u'ษ', u'ส', u'ฬ', u'อ']
    n_group = [u'ฅ', u'ฉ', u'ผ', u'ฝ', u'ฌ', u'ห', u'ฮ']
    v_group = [u'ะ', u'ิ', u'ี', u'ื', u'ึ', u'ุ', u'ู', u'ํ', u'า', u'ำ', u'ๅ']
    w_group = [u'เ' , u'แ' , u'โ' , u'ใ' , u'ไ']
    t_group = [u'่', u'้', u'๊', u'๋']
    s_group = [u'์', u'ๆ', u'ฯ', u'.']
    d_group = [u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9']
    q_group = [u'\'',u'-']
    p_group = [u'_']
    
    def get_group(self, char):
        if char in self.c_group:
            return 'c'
        elif char in self.n_group:
            return 'n'
        elif char in self.v_group:
            return 'v'
        elif char in self.w_group:
            return 'w'
        elif char in self.t_group:
            return 't'
        elif char in self.s_group:
            return 's'
        elif char in self.d_group:
            return 'd'
        elif char in self.q_group:
            return 'q'
        elif char in self.p_group:
            return 'p'
        else:
            return 'o'
    
    def create_train_message(self, message):
        ret_msg = ''
        lst_char = message[:]
        for j in range(len(lst_char)):
            if j == 0:
                ans = 'B'
            else:
                ans = 'I'
            message_model = lst_char[j]+' '+self.get_group(lst_char[j])+' '+ans+'\n'
            ret_msg += message_model
        return ret_msg
        
    
    def create_file_input(self, message):
        fileUtil = FileUtil()
        lst_char = message[:]
        for j in range(len(lst_char)):
            if j == 0:
                ans = 'B'
            else:
                ans = 'I'
            message_model = lst_char[j]+' '+self.get_group(lst_char[j])+' '+ans
            print message_model
            fileUtil.write_file('crf.test.data', message_model)                    
    
    def create_file_output(self, message):
        result = []
        fileUtil = FileUtil()
        
        
    def count_line(self):
        print 'count line'
        base_dir = 'best/all/'
        counter = 0
        lst_dir = listdir(base_dir)
        lst_dir.sort()
        for f in lst_dir:
            str_file = base_dir+f
            with codecs.open(str_file, 'r', 'utf-8') as file:
                lst_line = file.readlines()
                counter += len(lst_line)
                print f,',',len(lst_line)
        print 'all line ',counter
        
                    

    def create_model(self):
        base_dir = 'best/all/'
        fileUtil = FileUtil()
        for f in listdir(base_dir):
            str_file = base_dir+f
            print '****************************', str_file
            with codecs.open(str_file, 'r', 'utf-8') as file:
                for f in file.readlines():
                    lst = f.split('|')
                    for i in range(len(lst) - 1):
                        j = 0
                        str = lst[i]
#                         print str
                        lst_char = str[:]
                        for j in range(len(lst_char)):
                            if j == 0:
                                ans = 'B'
                            else:
                                ans = 'I'
                            message_model = lst_char[j]+' '+crf.get_group(lst_char[j])+' '+ans
                            print message_model
                            fileUtil.write_file('train', message_model)

# print 'Start create'
# crf = CRF()
# crf.count_line()
# crf.create_model()
# print 'End create'
