import algorithm
import operator
from sklearn.feature_extraction.text import TfidfVectorizer


class Main:
	def __init__(self, sample_file):
		self.stop_word_removal()		
		self.sample_file=open(sample_file,'r')
		self.text = self.sample_file.read()
		
		
	'''
		algorithm.Algorithm("SmartStoplist.txt", 4, 3, 3) means that 

		Each word of the keyword phrase has at least 4 characters
		Each keyword phrase has at most 3 words
		Each keyword appears in the text at least 3 times

		This can be altered according to user's discretion
	
	'''
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
          	tfidf = vectorizer.fit_transform([text1, text2])				#tf-idf calculation
          	x=((tfidf * tfidf.T).A)[0,1]
		
		return x
	
	
sample_file = "script.txt"
vectorizer = TfidfVectorizer( stop_words='english')
k=Main(sample_file)
keywords=k.ret_keywords()								#find the keywords based on occurrence
n=10											#n= number of keywords to be taken into account
keywords=k.truncated_keyword(n)								#only take the best n keywords

script_list=k.script_keys_to_list(keywords,n)						#converting the keywords into a list
print "List of extracted top n keywords are---",script_list
key_score=[]
total_score=[]
files=['transcript_1.txt','transcript_2.txt','transcript_3.txt']

####This loop is for extracting the necessary words(either keywords or each and every word depending on the user) and calculating their similarity with the extracted keywords
for index in range(len(files)):

	t1_keywords=k.transcript_preprocess(files[index])
	trans1_list=k.script_keys_to_list(t1_keywords,len(t1_keywords))

	for i in range(n):
    		tmp=0
    
    		for j in range(len(trans1_list)):
        		tmp=tmp+k.similarity(script_list[i],trans1_list[j])		#calculating the similarity for the keywords and each word in the transcript files
    		key_score.append(tmp)

for i in range(n):
	total_score.append(key_score[i]+key_score[i+10]+key_score[i+20])		#calculating score for each of the keywords extracted from the script file
		

total_score= sorted(total_score, reverse=True)						#Sorting the score for each of the keywords accordingly in descending order

print "PRINTING THE SORTED SCORE FOR EACH OF THE KEYWORDS --------  "

for i in range(n):
	print script_list[i], "= \t", total_score[i]
