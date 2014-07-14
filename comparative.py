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
		for orchid_data in data:
			print orchid_data
			first_char, sec_char, line_data = orchid_data[:1], orchid_data[:2], orchid_data[1:2]
			if '%' == first_char:
				counter = counter+1
				continue

			if first_char == '#' and line_data.isdigit() :
				counter+=1
				origin_data = data[counter]
				counter+=1
				next_data = data[counter]
				result = []
				print origin_data
				while next_data != '//\n':
					result_data = self.convert_result(next_data)
					result.append(result_data)
					counter+=1
					next_data = data[counter]
				time_swath, d_swath = wordseg.swath(origin_data, result)
				time_wordcut, d_wordcut = wordseg.wordcut(origin_data, result)
				time_sem, d_sem = wordseg.thaisematic(origin_data, result)
				time_tlex, d_tlex = wordseg.Tlex(origin_data.decode('utf-8'), result)
				time_libthai, d_libthai = wordseg.libthai(origin_data, result)
				self.write_output_time(time_swath, time_wordcut, time_sem, time_tlex, time_libthai)
				self.write_output_distance(d_swath, d_wordcut, d_sem, d_tlex, d_libthai)
			counter = counter+1

	def write_output_time(self, time_swath, time_wordcut, time_sem, time_tlex, time_libthai):
		print time_swath, time_wordcut, time_sem, time_tlex, time_libthai
	
	def write_output_distance(self, d_swath, d_wordcut, d_sem, d_tlex, d_libthai):
		print d_swath, d_wordcut, d_sem, d_tlex, d_libthai

mainCmp = MainCompare()
mainCmp.process_data()
