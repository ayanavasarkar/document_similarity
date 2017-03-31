import algorithm
import operator

class Main:
	def __init__(self, sample_file):
		self.stop_word_removal()		
		self.sample_file=open(sample_file,'r')
		self.text = self.sample_file.read()
		
			
	def stop_word_removal(self):
		self.stop_word = algorithm.Algorithm("SmartStoplist.txt", 4, 3, 3)	#stop word removal using the smart stopword list
	
	def ret_keywords(self):
		self.keywords = self.stop_word.run(self.text)				#first find the keywords
		self.keywords= sorted(self.keywords,key=lambda l:l[1], reverse=True)	#sort the keywords in descending order of score
		return self.keywords

	def truncated_keyword(self,n):
		self.n=n
		self.keywords=self.keywords[0:self.n]
		return self.keywords

	def transcript_preprocess(self,transcript):
		self.stop_word_t = algorithm.Algorithm("SmartStoplist.txt", 4, 3, 3)
		self.transcript=open(transcript,'r')
		self.t_text=self.transcript.read()

		self.t_keywords = self.stop_word_t.run(self.t_text)				#first find the keywords
		self.t_keywords= sorted(self.t_keywords,key=lambda l:l[1], reverse=True)
		return self.t_keywords


sample_file = "script.txt"

k=Main(sample_file)
keywords=k.ret_keywords()
#print keywords
n=10											#n= number of keywords to be taken into account
keywords=k.truncated_keyword(n)
#print len(keywords)
#print "Keywords:", keywords


print keywords

transcript1="transcript_1.txt"

t1_keywords=k.transcript_preprocess(transcript1)

print t1_keywords
