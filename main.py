import algorithm
import operator

class Main:
	def __init__(self, sample_file):
		self.stop_word_removal()		
		self.sample_file=open(sample_file,'r')
		self.text = self.sample_file.read()
		
			
	def stop_word_removal(self):
		self.rake_object = algorithm.Algorithm("SmartStoplist.txt", 4, 3, 3)	#stop word removal using the smart stopword list
	
	def ret_keywords(self):
		self.keywords = self.rake_object.run(self.text)				#first find the keywords
		self.keywords= sorted(self.keywords,key=lambda l:l[1], reverse=True)	#sort the keywords in descending order of score
		return self.keywords

	def truncated_keyword(self,n):
		self.n=n
		self.keywords=self.keywords[0:self.n]
		return self.keywords
		
sample_file = "script.txt"

k=Main(sample_file)
keywords=k.ret_keywords()
#print keywords
n=10											#n= number of keywords to be taken into account
keywords=k.truncated_keyword(n)
#print len(keywords)
#print "Keywords:", keywords


print keywords

