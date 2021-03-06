﻿# DOCUMENT SIMILARITY

STEPS FOR INSTALLATION

Open the terminal and run the following commands:

--> sudo apt-get upgrade

--> sudo apt-get update

--> python3 -v (to check if python version 3 is already installed or not)

--> sudo apt-get install -y python3-pip

--> sudo apt-get install build-essential libssl-dev libffi-dev python-dev
(for setting up the Python programming environment)

--> Open up a terminal and type .bashrc

--> In the file that now opens, set the pythonpath using the following command-

export pythonpath=$pythonpath /usr/local/lib/python3.x/site-packages

3.x denotes the version of Python installed. Now save and close it.

--> In the terminal type the following
sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose

--> Next type the following command--
pip install -U scikit-learn

--> Now on the terminal git this package using the following command:
git clone https://github.com/ayanavasarkar/document_similarity.git

--> cd document_similarity (in the Terminal).

--> python main.py

The file algorithm.py contains the implementation of keyphrase extraction after stopword removal. Now in order to add more files or to remove files from which comparison with keywords is to be done, simply go to the file main.py and in line number 93, make the required path additions.



What this package does?


A set of keywords is extracted from the file script.txt.
Based on those keywords and their respective scores in the script.txt file, the best 'n' keywords are taken in descending order of the scores.
Now, the best 'n' keywords are matched with words of the three transcript.txt files and a similarity score is calculated between each 'n' best keyword and words present in the transcript files.

Note – An important factor that must be noted is that based upon user need, the similarity comparison can be done between:
each keyword of the script.txt file and every word from each of the transcript files.
					OR
each keyword of the script.txt file and the best 'n' keywords extracted from each of the transcript files.
The latter is far more efficient than the former.

Output displayed is each keyword extracted from the script.txt file and their corresponding scores.





What are Keywords?

Keywords, defined as a sequence of one or more words, provide a compact representation of a document’s content. Ideally, keywords represent in condensed form the essential content of a document.





Extraction of Keywords

The stop words are first removed from the extracted text. 
Then separate each sentence using delimiters like full stop, question mark etc.
Then use the defined word delimiters to get an array of words.
Finally obtain a sequence of continuous words using the array delimited by the phrase delimiters. Phrase delimiters are the previous stop words.
The keywords have been extracted.

self.stop_word_t = algorithm.Algorithm("SmartStoplist.txt", 4, 1, 3)

This line in the file main.py is an important line due to the numbers 4,1,3.

It indicates that for the extracted keywords, each word must consist of minimum of 4 letters, each phrase can have a maximum of 3 words and has appeared at least 3 times in the document. Now these 3 values can be altered accordingly.






Score of the Keywords

After the keywords have been extracted, we calculate the degree and the frequency of each word.

Degree = number of words in the keyword phrase -1

Frequency = number of times the keyword appeared in the document

Final Score = (degree/frequency)

Thus, Total score of a keyword phrase = sum of each of its keyword scores


Similarity Calculation with Transcript file

After the Kywords have been extracted from the script.py file, next we need to measure the similarity between the keywords and words of the Transcript files. Now, as earlier mentioned, only the keywords from the transcript files can be extracted or all the words excluding the stop words can be extracted from the transcript files. 
A similarity calculation using Cosine similarity is measured between the keywords from the script.py and the words from each of the transcript files. The Similarities for each of the keywords of the script.py file with each of the words from transcript files are added up and thus we end up with a list having each keyword and its corresponding cumulated similarity value. this has been explained with an example:

If keywords extracted from script.py are [bird, wonderwall of dreams]
Let the words extracted from the first transcript file be [ball, bird in wonderland]

Then we compare similarity between the following pairs:
(bird, ball)
(bird, bird in wonderland)
(wonderwall of dreams, ball)
(wonderwall of dreams, bird in wonderland)

In the end, we end up with a list of [(bird:sim_score),(wonderwall of dreams:score)]
Now we sort the list in descending order of the scores of each keyword and we obtain the final result.


