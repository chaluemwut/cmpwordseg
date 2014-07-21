import sys, os, time
from wordsegmentation import WordSegmentation

# spacial char 
# <minus> -
# <space>
# <left_parenthesis> (
# <right_parenthesis> )
# <equal> =
# new line \\
# <quotation> "
# <full_stop> .

class MainCompare:
	
	def convert_result(self, next_data):
		if next_data == '<space>/PUNC\n':
			return ' '
		elif next_data == '<minus>/PUNC\n':
			return '-'
		elif next_data == '<left_parenthesis>/PUNC\n':
			return '('
		elif next_data == '<right_parenthesis>/PUNC\n':
			return ')'
		elif next_data == '<quotation>/PUNC\n':
			return '"'
		elif next_data == '<full_stop>/PUNC\n':
			return '.'
		else :
			return next_data[:next_data.index("/")]
		
	
	def process_data(self, start):
		data = []
		for line in open('orchid97.crp.utf').readlines():
			data.append(line)

		counter = start
		wordseg = WordSegmentation()
		for orchid_data in range(start, len(data)):
			self.line_id = counter
			orchid_data = data[counter]
			first_char, line_data = orchid_data[:1], orchid_data[1:2]
			if '%' == first_char:
				counter = counter+1
				continue
			
			if first_char == '#' and line_data.isdigit() and data[counter+1][:1] == '%':
				counter = counter+1
				continue

			if first_char == '#' and line_data.isdigit() :
				self.resume_write(counter)
				counter = counter+1
				origin_data = data[counter]
				if origin_data[-2:] == '\\\n':
					counter = counter+1
					next_data = data[counter]
					origin_data = origin_data + next_data
					while next_data[-2:] == '\\\n':
						counter = counter+1
						next_data = data[counter]
						origin_data = origin_data + next_data
				counter = counter+1
				print origin_data
				next_data = data[counter]
				result = []
				while next_data != '//\n':
					result_data = self.convert_result(next_data)
					result.append(result_data)
					counter = counter+1
					if counter >= 431325:
						break
					next_data = data[counter]
				
				try:
					time_libthai, d_libthai, out_libthai = wordseg.libthai(origin_data, result)				
					time_swath, d_swath, out_swath = wordseg.swath(origin_data, result)
					time_wordcut, d_wordcut, out_wordcut = wordseg.wordcut(origin_data, result)
# 					time_tlex, d_tlex, out_tlex = wordseg.Tlex(origin_data.decode('utf-8'), result)	
# 					time_sem, d_sem, out_sem = wordseg.thaisematic(origin_data, result)
	
					try:
						time_tlex, d_tlex, out_tlex = wordseg.Tlex(origin_data.decode('utf-8'), result)
					except Exception, e:
						str_msg_tlex = str(self.line_id)+','+str(e)
						self.write_error_time_out('error_tlex.txt', str_msg_tlex)
					try:
						time_sem, d_sem, out_sem = wordseg.thaisematic(origin_data, result)
					except Exception, e:
						str_msg_sem = str(self.line_id)+','+str(e)
						self.write_error_time_out('error_thaisemantic.txt', str_msg_sem)
						
					self.write_output_time(time_libthai, time_swath, time_wordcut, time_sem, time_tlex)
					self.write_output_distance(d_libthai, d_swath, d_wordcut, d_sem, d_tlex)
				except Exception, e:
					self.write_erro(str(self.line_id)+','+str(e))
			if counter >= 431325:
				break
			counter = counter+1
	
	def validate_data(self, log_data):
		pass
# 		validate = ValidateData()
# 		validate.process_log(log_data)
	
	def read_resume(self):
		f = open('resume.txt','r')
		msg = f.read()
		f.close()
		return msg
	
	def resume_write(self, line):
		f = open('resume.txt','w')
		f.write(str(line))
		f.close()
			
	def write_erro(self, msg):
		self.write_file(msg, 'error.txt')
		
	def write_error_time_out(self, file_name, msg):
		self.write_file(msg, file_name)		
			
	def write_file(self, msg, file_name):
		print msg
		f = open(file_name,'a+b')
		f.write(msg+'\n')
		f.close()

	def write_output_time(self, time_libthai, time_swath, time_wordcut, time_sem, time_tlex):
		msg = ','.join([str(time_libthai), str(time_swath), str(time_wordcut), str(time_sem), str(time_tlex)])
		self.write_file(str(self.line_id)+','+msg, 'time.txt')
	
	def write_output_distance(self, d_libthai, d_swath, d_wordcut, d_sem, d_tlex):
		msg = ','.join([str(d_libthai), str(d_swath), str(d_wordcut), str(d_sem), str(d_tlex)])
		self.write_file(str(self.line_id)+','+msg, 'distance.txt')

try :
	arg = sys.argv[1]
except Exception, e:
	arg = ''
	print 'no arg'
	
print '************** Start *****************'
mainCmp = MainCompare()
start_time = time.time()
if arg == 'resume':
	print 'resume process...'
	resume_line = mainCmp.read_resume()
	print 'resume start with ',resume_line
	mainCmp.process_data(int(resume_line))
elif arg == 'clean':
	print 'clean log file'
	os.system('rm distance.txt time.txt error.txt error_tlex.txt error_thaisemantic.txt resume.txt')
else:
	print 'Start new process'
	mainCmp.process_data(0)
total_time = time.time() - start_time #return in seconds
print 'Execution time : ',total_time*0.000277778,' Hour'
print '**************** End *****************'
