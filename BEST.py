from util import FileUtil
from computation import CorrectnessComputation
from util import *
from CallerProgram import CallerProgram
import time

class BESTProcess:
    test_dir = 'kfold/test/'
    result_dir = 'kfold/result/'
    caller = CallerProgram()
    computeCorrect = CorrectnessComputation()
    fileUtil = FileUtil()
    
    def __init__(self):
        print 'best corpus'
    
    def compareProcess(self):
        model_path = 'kfold/model/'
        for i in range(1,5):
            model_path = model_path+'model'+str(i)
            test_file_name = self.test_dir+'test'+str(i)
            result_file_name = self.result_dir+'result'+str(i)
            test_line = self.fileUtil.read_file(test_file_name)
            result_line = self.fileUtil.read_file(result_file_name)  
            print 'i '+str(i)+' file '+test_file_name, result_file_name
            for j in range(len(test_line)):
                self.line_id = str(i)+' - '+str(j)
                origin_data = test_line[j]
                result_msg = StringUtil.remove_ne(result_line[j])
                result_lst = result_msg.split('|')[:-1]
                try:
                    time_libthai, out_libthai = self.caller.libthai(origin_data)
                    time_swath, out_swath = self.caller.swath(origin_data)
                    time_wordcut, out_wordcut = self.caller.wordcut(origin_data)
                    time_thaisemantics, out_thaisemantics = self.caller.thaisematic(origin_data, self.line_id)
                    time_Tlexs, out_Tlex = self.caller.NewTlexs(origin_data, self.line_id)
                    time_crf, out_crf = self.caller.crfpp(origin_data, model_path)
    
                        # computation
                    p_libthai, r_libthai, f_libthai = self.computeCorrect.precision_recall_f1(out_libthai, result_lst)
                    p_swath, r_swath, f_swath = self.computeCorrect.precision_recall_f1(out_swath, result_lst)
                    p_wordcut, r_wordcut, f_wordcut = self.computeCorrect.precision_recall_f1(out_wordcut, result_lst)
                    p_thaisemantics, r_thaisemantics, f_thaisemantics = self.computeCorrect.precision_recall_f1(out_thaisemantics, result_lst)
                    p_Tlexs, r_Tlexs, f_Tlex = self.computeCorrect.precision_recall_f1(out_Tlex, result_lst)
                    p_crf, r_crf, f_crf = self.computeCorrect.precision_recall_f1(out_crf, result_lst)
                        
                    pipe_data_correct = [str(p_libthai), str(r_libthai), str(f_libthai),
                                     str(p_swath), str(r_swath), str(f_swath),
                                     str(p_wordcut), str(r_wordcut), str(f_wordcut),
                                     str(p_thaisemantics), str(r_thaisemantics), str(f_thaisemantics),
                                     str(p_Tlexs), str(r_Tlexs), str(f_Tlex),
                                     str(p_crf), str(r_crf), str(f_crf)]
                    pipe_msg_correct = ','.join(pipe_data_correct)
                    print 'i '+str(i)+' - j '+str(j), ' correct ',pipe_msg_correct
                    out_file_correct = 'logs/result/correct'+str(i)+'.csv'
                    self.fileUtil.write_file(out_file_correct, pipe_msg_correct)
                        
                    pipe_data_time = [str(time_libthai), str(time_swath),
                                          str(time_wordcut), str(time_thaisemantics),
                                          str(time_Tlexs), str(time_crf)]
                    pipe_msg_time = ','.join(pipe_data_time)
                    print 'i '+str(i)+' - j '+str(j),' time ',pipe_msg_time
                    out_file_time = 'logs/result/time'+str(i)+'.csv'
                    self.fileUtil.write_file(out_file_time, pipe_msg_time)                  
                except Exception, e:
                    self.fileUtil.write_file('error.txt','main error : '+str(self.line_id)+','+str(e))            

print '************** Start *****************'
start_time = time.time()
best = BESTProcess()
best.compareProcess()
total_time = time.time() - start_time #return in seconds
print 'Execution time : ',total_time*0.000277778,' Hour'
print '**************** End *****************'