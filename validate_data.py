class ValidateData :
    
    def write_file(self, msg):
        print msg
        f = open('validate.txt','a+b')
        f.write(msg+'\n')
        f.close()
        
    def process_log(self, log_data):
        self.write_file('******* start *********')
        self.write_file('log in :',log_data.log_id)
        self.write_file('----- correct ')
        self.write_file(','.join(log_data.origin_data))
        self.write_file('----- libthai')
        self.write_file(','.join(log_data.libthai))
        self.write_file('----- swath')
        self.write_file(','.join(log_data.swath))  
        self.write_file('----- wordcut')
        self.write_file(','.join(log_data.wordcut))
        self.write_file('----- thaisematic')
        self.write_file(','.join(log_data.thaisematic)) 
        self.write_file('----- tlex')
        self.write_file(','.join(log_data.tlex))                                  
        self.write_file('******* end *********')
    
class LogData :
    
    _log_id = ''
    @property
    def log_id(self):
        return self._log_id
    @log_id.setter
    def log_id(self, log_id):
        self._log_id = log_id
    
    _origin_data = ''
    @property
    def origin_data(self):
        return self._origin_data
    @origin_data.setter
    def origin_data(self, origin_data):
        self._origin_data = origin_data
    
    _correct = []
    @property
    def correct(self):
        self._correct
    @correct.setter
    def correct(self, correct):
        self._correct = correct
    
    _libthai = []
    @property
    def libthai(self):
        self._libthai
    @libthai.setter
    def libthai(self, libthai):
        self._libthai = libthai
    
    _swath = []
    @property
    def swath(self):
        self._swath
    @swath.setter
    def swath(self, swath):
        self._swath = swath

    _wordcut = []
    @property
    def wordcut(self):
        self._wordcut
    @wordcut.setter
    def wordcut(self, wordcut):
        self._wordcut = wordcut
    
    _thaisematic = []           
    @property
    def thaisematic(self):
        self._thaisematic
    @thaisematic.setter
    def thaisematic(self, thaisematic):
        self._thaisematic = thaisematic

    _tlex = []           
    @property
    def tlex(self):
        self._tlex
    @tlex.setter
    def tlex(self, tlex):
        self._tlex = tlex
  

# log = LogData()
# log.origin_data = 'test data'
# log.correct = ['test','123']
# 
# print log.correct
 