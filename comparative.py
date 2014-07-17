from wordsegmentation import WordSegmentation

# spacial char 
# <minus> -
# <space>
# <left_parenthesis> (
# <right_parenthesis> )
# <equal> =
# new line \\
# <quotation> "

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
		else :
			return next_data[:next_data.index("/")]
		
	
	def process_data(self):
		data = []
		for line in open('orchid97.crp.utf').readlines():
			data.append(line)

		counter = 0
		wordseg = WordSegmentation()
		for orchid_data in range(len(data)):
			orchid_data = data[counter]
			first_char, line_data = orchid_data[:1], orchid_data[1:2]
			if '%' == first_char:
				counter = counter+1
				continue
			
			if first_char == '#' and line_data.isdigit() and data[counter+1][:1] == '%':
				counter = counter+1
				continue

			if first_char == '#' and line_data.isdigit() :
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
					next_data = data[counter]
				
# 				time_swath, d_swath = wordseg.swath(origin_data, result)
# 				time_wordcut, d_wordcut = wordseg.wordcut(origin_data, result)
# 				time_sem, d_sem = wordseg.thaisematic(origin_data, result)
# 				time_tlex, d_tlex = wordseg.Tlex(origin_data.decode('utf-8'), result)
# 				time_libthai, d_libthai = wordseg.libthai(origin_data, result)
# 				self.write_output_time(time_libthai, time_swath, time_wordcut, time_sem, time_tlex)
# 				self.write_output_distance(d_swath, d_wordcut, d_sem, d_tlex, d_libthai)
									
				try:					
					time_swath, d_swath = wordseg.swath(origin_data, result)
					time_wordcut, d_wordcut = wordseg.wordcut(origin_data, result)
					time_sem, d_sem = wordseg.thaisematic(origin_data, result)
					time_tlex, d_tlex = wordseg.Tlex(origin_data.decode('utf-8'), result)
					time_libthai, d_libthai = wordseg.libthai(origin_data, result)
					self.write_output_time(time_libthai, time_swath, time_wordcut, time_sem, time_tlex)
					self.write_output_distance(d_swath, d_wordcut, d_sem, d_tlex, d_libthai)
				except Exception, e:
					self.write_erro(str(e))
				
			counter = counter+1
			
	def write_erro(self, msg):
		self.write_file(msg, 'error.txt')		
			
	def write_file(self, msg, file_name):
		print msg
		f = open(file_name,'a+b')
		f.write(msg+'\n')
		f.close()

	def write_output_time(self, time_libthai, time_swath, time_wordcut, time_sem, time_tlex):
		msg = ','.join([str(time_libthai), str(time_swath), str(time_wordcut), str(time_sem), str(time_tlex)])
		self.write_file(msg, 'time.txt')
	
	def write_output_distance(self, d_libthai, d_swath, d_wordcut, d_sem, d_tlex):
		msg = ','.join([str(d_libthai), str(d_swath), str(d_wordcut), str(d_sem), str(d_tlex)])
		self.write_file(msg, 'distance.txt')

mainCmp = MainCompare()
mainCmp.process_data()
