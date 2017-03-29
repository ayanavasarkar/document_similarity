import algorithm
import operator

class Main:
	def __init__(self, sample_file):
		self.stop_word_removal()		
		self.sample_file=open(sample_file,'r')
		self.text = self.sample_file.read()
		
			
	def stop_word_removal(self):
		self.rake_object = algorithm.Algorithm("SmartStoplist.txt", 4, 3, 3)
	
	def ret_keywords(self):
		self.keywords = self.rake_object.run(self.text)
		return self.keywords

sample_file = "script.txt"#open("script.txt", 'r')

k=Main(sample_file)
keywords=k.ret_keywords()
n=10
print len(keywords)
print "Keywords:", keywords

