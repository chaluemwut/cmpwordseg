# -*- coding: UTF-8 -*-
import os, time, urllib2, json
from suds.client import Client

def levenshtein_backup(a,b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n
        
    current = range(n+1)
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)
            
    return current[n]

def levenshtein(a,b):
    n, m = len(a), len(b)
    if n>m:
        max_len = n
    else:
        max_len = m
    
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n
        
    current = range(n+1)
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)
            
    return current[n]/float(max_len)

class WordSegmentation(object):

    def __init__(self):
        pass
        
    def write_file(self, msg):
        f = open('in.txt','w')
        f.write(msg)
        f.close()
    
    def write_file_th(self, msg):
        f = open('thin.txt','w')
        u = unicode(msg, "utf-8")
        f.write(u.encode('tis-620'))
        f.close()     

    def read_file(self):
        f = open('out.txt','r')
        msg = f.read()
        f.close()
        return msg

    def count_array(self, base, target):
        correct=0
        wrong=0
        for i in range(len(base)):
            ans = base[i]
            algo = base[i]
            if ans == algo:
                correct+=1
            else:
                wrong+=1
        return correct, wrong

    def count_answer(self, ans_correct, ans_algo):
        correct=0
        wrong=0
        correct, wrong = self.count_array(ans_correct, ans_algo)
        if len(ans_correct) < len(ans_algo):
            wrong = wrong+(len(ans_algo)-len(ans_correct))
        return correct, wrong

    def swath(self, msg, result):
        trim_msg = msg.replace("//","").replace("\n","")
        return self.template_call(trim_msg, result, "swath -u u,u <in.txt> out.txt", '|')

    def thaisematic(self, msg, result):
        msg = self.befor_trim(msg)
        request = {
                   'api_key': '547bce78d5568489b44484cc6a9fca49587a45de24d21718175823ad4027e87b',
                   'method': 'SWATH',
                   'params': [msg]
                   }
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "application/json"}
        params = json.dumps(request)
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "application/json"}
        url = 'https://www.thaisemantics.org/service/rest/'
        req = urllib2.Request(url, params)
        req.add_header('Content-type','application/x-www-form-urlencoded')
        req.add_header('Accept','application/json')
        start_time = time.time()
        try:
            u = urllib2.urlopen(req, timeout=60*5)
        except Exception, e:
            print 'thai semantics time out'
            raise
        data = u.read()
        json_data = json.loads(data)
        total_time = time.time() - start_time #return in seconds
        program_result = []
        for sep_data in json_data['result']:
            program_result.append(sep_data)
#         result_uni = [unicode(a, 'utf-8') for a in result]
        distance = levenshtein([unicode(a, 'utf-8') for a in result], program_result)
        return total_time, distance, program_result

    def wordcut(self, msg, result):
        trim_msg = msg.replace("//","")
        return self.template_call(trim_msg, result, "wordcut <in.txt> out.txt", ' ')

    def template_call(self, msg, result, command, separator):
        self.write_file(msg)
        start_time = time.time()
        os.system(command)
        total_time = time.time() - start_time #return in seconds
        out = self.read_file()
        out = out.replace('\n','')
        if separator == ' ':
            out_lst_tmp = out.split(separator)
            out_lst = [' ' if x == '' else x for x in out_lst_tmp]
        else:
            out_lst = out.split(separator)
        distance = levenshtein(result, out_lst)
#         correct, wrong = self.count_answer(result, out_lst)
        return total_time, distance, out_lst

    def libthai(self, msg, result):
        trim_msg = self.befor_trim(msg)
        self.write_file_th(trim_msg)
        u = unicode("./libthai", "utf-8")
        start_time = time.time()
        os.system(u.encode('tis-620'))
        total_time = time.time() - start_time #return in seconds
        f = open('thout.txt','r')
        str_out = f.read()
        f.close()
        str_out = str_out.decode('tis-620')
        program_result = str_out.split('|')
        uni_result = [unicode(a, 'utf-8') for a in result]
        d = levenshtein(uni_result, program_result)
        return total_time, d, program_result

    def Tlex(self, msg, result):
        try :
            client = Client('http://www.sansarn.com/WSeg/wsdl/BnSeg.wsdl', timeout=60*10)
        except Exception, e:
            print 'tlex time out'
            raise
        msg = self.befor_trim(msg)
        start_time = time.time()
        out = client.service.seg(msg)
        total_time = time.time() - start_time #return in seconds
        str_out = self.after_trim(out)
        str_out = str_out[:len(str_out)-1]
        program_result = str_out.split('|')
        uni_result = [unicode(a, 'utf-8') for a in result]
        d = levenshtein(uni_result, program_result)
        return total_time, d, program_result
    
    def befor_trim(self, msg):
        return msg.replace("//","").replace("\n","")
    
    def after_trim(self, msg):
        return msg.replace("\n","")

# wordseg = WordSegmentation()
# wordseg.thaisematic('วันที่ 15-16 สิงหาคม 2532\n', [])

# u = unicode('ทดสอบ','utf-8')
# u1 = unicode('ทดสอบ','utf-8')
# print u
# print levenshtein(['g', 'a'], ['g', 'a', 't'])
# wordseq = WordSegmentation()
# wordseq.Tlex('test', [])
# param = "ทดสอยได้ไหม"
# u = unicode("./libthai "+param, "utf-8")
# os.system(u.encode('tis-620'))
# f = open('thaiout.txt','r')
# msg = f.read()
# print msg.decode('tis-620')
# f.close()
# f = open('test.txt','w')
# f.write(u.encode('tis620'))
# f.close()

