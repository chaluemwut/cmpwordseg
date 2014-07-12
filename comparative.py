from wordsegmentation import WordSegmentation

class MainCompare:
	
	def process_data(self):
		data = []
		for line in open('orchid97.crp.utf').readlines():
			data.append(line)

		counter = 0
		wordseg = WordSegmentation()
		for orchid_data in data:
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
				while next_data != '//\n':
					result.append(next_data[:next_data.index("/")])
					counter+=1
					next_data = data[counter]
# 				time_swath, correct_swath, wrong_swath = wordseg.swath(origin_data, result)
# 				print time_swath, correct_swath, wrong_swath
# 				time_wordcut, correct_wordcut, wrong_wordcut = wordseg.wordcut(origin_data, result)
# 				print time_wordcut, correct_wordcut, wrong_wordcut
				wordseg.thaisematic(origin_data, result)
				break
			counter = counter+1

	def write_output(self, program_id, data_msg, exe_time, num_correct):
		pass

mainCmp = MainCompare()
mainCmp.process_data()
