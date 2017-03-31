import algorithm
import operator
from sklearn.feature_extraction.text import TfidfVectorizer


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

	def script_keys_to_list(self,keywords,n):
		script_list=[]
		for i in range(n):
			script_list.append(keywords[i][0])
		return script_list


	def transcript_preprocess(self,transcript):
		self.stop_word_t = algorithm.Algorithm("SmartStoplist.txt", 4, 1, 3)
		self.transcript=open(transcript,'r')
		self.t_text=self.transcript.read()

		self.t_keywords = self.stop_word_t.run(self.t_text)				#first find the keywords
		self.t_keywords= sorted(self.t_keywords,key=lambda l:l[1], reverse=True)
		return self.t_keywords
      
      	def similarity(self,text1,text2):
          	tfidf = vectorizer.fit_transform([text1, text2])
          	x=((tfidf * tfidf.T).A)[0,1]
		self.test(x)
		return x
	def test(self,x):
		print x


sample_file = "script.txt"

k=Main(sample_file)
keywords=k.ret_keywords()
n=10											#n= number of keywords to be taken into account
keywords=k.truncated_keyword(n)
#print keywords
script_list=k.script_keys_to_list(keywords,n)
print script_list


files=['transcript_1.txt','transcript_2.txt','transcript_3.txt']

transcript1="transcript_1.txt"

t1_keywords=k.transcript_preprocess(transcript1)
trans1_list=k.script_keys_to_list(t1_keywords,len(t1_keywords))
#print trans1_list

vectorizer = TfidfVectorizer( stop_words='english')
key_score=[]
for i in range(n):
    tmp=0
    #key_score[i][0].append(script_list[i])
    for j in range(len(trans1_list)):
        tmp=tmp+k.similarity(script_list[i],trans1_list[j])
    key_score.append(tmp)

print key_score
