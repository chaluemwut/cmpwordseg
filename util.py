import codecs

class FileUtil:
    
    def write_file(self, file_name, message):
        with codecs.open(file_name, 'a+b', encoding='utf8') as f:
            f.write(message + '\n')
            f.close()

    def write_file_no_n(self, file_name, message):
         with codecs.open(file_name, 'a+b', encoding='utf8') as f:
            f.write(message)
            f.close()
           
    def read_file(self, file_name):
        with codecs.open(file_name, 'r', 'utf-8') as file:
            return file.readlines()
        return []
