from util import FileUtil
from computation import CorrectnessComputation

class BESTProcess:
    test_dir = 'kfold/test/'
    result_dir = 'kfold/result/'
    def compareProcess(self):
        wordseg = WordSegmentation()
        computeCorrect = CorrectnessComputation()
        
        def __init__():
            print 'best compare'
        
        
        for i in range(5):
            test_file_name = self.test_dir+'test'+str(i)
            result_file_name = self.result_dir+'result'+str(i)
            test_line = fileUtil.read_file(test_file_name)
            result_line = fileUtil.read_file(result_file_name)
            for j in range(len(test_line)):
                original_msg = test_line[j]
                result_msg = result_line[j]
                try:
                    time_libthai, out_libthai = self.wordseg.libthai(origin_data)
                    time_swath, out_swath = self.wordseg.swath(origin_data)
                    time_wordcut, out_wordcut = self.wordseg.wordcut(origin_data)
                    time_thaisemantics, out_thaisemantics = self.wordseg.thaisematic(origin_data, self.line_id)
                    time_Tlexs, out_Tlex = self.wordseg.NewTlexs(origin_data, self.line_id)
                    
#                     self.write_comput(result, out_libthai, out_swath, out_wordcut, out_thaisemantics, out_Tlex)
#                     self.write_output_time(time_libthai, time_swath, time_wordcut, time_thaisemantics, time_Tlexs)
                except Exception, e:
                    self.write_erro('main error : '+str(self.line_id)+','+str(e))
                
                
                

