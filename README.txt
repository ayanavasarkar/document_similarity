# DOCUMENT SIMILARITY

What this package does?


A set of keywords is extracted from the file script.txt.
Based on those keywords and their respective scores in the script.txt file, the best 'n' keywords are taken in descending order of the scores.
Now, the best 'n' keywords are matched with words of the three transcript.txt files and a similarity score is calculated between each 'n' best keyword and words present in the transcript files.

Note – An imprtant factor that must be noted is that based upon user need, the similarity comparison can be done between:
each keyword of the script.txt file and every word from each of the transcript files.
					OR
each keyword of the script.txt file and the best 'n' keywords extracted from each of the transcript files.
The latter is far more efficient than the former.

Output displayed is each keyword extracted from the script.txt file and their corresponding scores.


What are Keywords?


Keywords, defined as a sequence of one or more words, provide a
compact representation of a document’s content. Ideally, keywords represent in
condensed form the essential content of a document.



