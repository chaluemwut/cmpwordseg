
class CorrectnessComputation:
    
    def precision_recall_f1(self, OutputWord, RefWord):
#         print 'Out word',OutputWord
#         print 'Ref word',RefWord
        if len(OutputWord) == 0:
            return 0, 0, 0
        s_OutputWord = set(OutputWord)
        s_RefWord = set(RefWord)
        Corr = s_OutputWord.intersection(s_RefWord)
        precision = float(len(Corr)) / len(OutputWord)
        recall = float(len(Corr)) / len(RefWord)
        if precision+recall == 0:
            return precision, recall, 0
        f = float(2*precision*recall)/float(precision+recall)
        return precision, recall, f