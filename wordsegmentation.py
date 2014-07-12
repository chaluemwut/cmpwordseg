import os, time, urllib2, sys, json

class WordSegmentation(object):

    def __init__(self):
        pass
        
    def test(self):
        print("test")
        
    def write_file(self, msg):
        f = open('in.txt','w')
        f.write(msg)
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
        return self.template_call(msg, result, "swath -u u,u <in.txt> out.txt", '|')

    def thaisematic(self, msg, result):
        request = {
                   'api_key': '547bce78d5568489b44484cc6a9fca49587a45de24d21718175823ad4027e87b',
                   'method': 'SWATH',
                   'params': [msg]
                   }
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "application/json"}
        params = json.dumps(request)
# print params
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "application/json"}
        url = 'https://www.thaisemantics.org/service/rest/'
        req = urllib2.Request(url, params)
        req.add_header('Content-type','application/x-www-form-urlencoded')
        req.add_header('Accept','application/json')
        u = urllib2.urlopen(req)
        data = u.read()
        json_data = json.loads(data)
        for sep_data in json_data['result']:
            print sep_data
        print sep_data

    def wordcut(self, msg, result):
        return self.template_call(msg, result, "wordcut <in.txt> out.txt", ' ')

    def template_call(self, msg, result, command, separator):
        trim_msg = msg.replace("//","")
        self.write_file(trim_msg)
        start_time = time.time()
        os.system(command)
        total_time = time.time() - start_time #return in seconds
        out = self.read_file()
        out_lst = out.split(separator)
        correct, wrong = self.count_answer(result, out_lst)
        return total_time, correct, wrong

    def libthai(self, msg, result):
        pass

    def Tlex(self, msg, result):
        pass
