import os, time

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
        pass

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
