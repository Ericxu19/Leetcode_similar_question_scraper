# Leetcode_similar_question_scraper
Builds a database of pairs of questions from LeetCode with a similarity score.

The output will be a csv fo form "question 1", "question 2", score, dev (if it is part of the dev set)
The questions will be striped of the included examples and notes.

20% of the total pairs will be in the dev set. There is currently no test set. 

the score is out of 5 and is determined by the "similar question" category and "Related Topics" tags on the question on leetcode. 

Questions taged in similar question will recieve a score of 5. Score of other pairs of questions are determined by the amount of Related Topics tags they share.

process.py also produces Qcollection.csv which is simply a collection of all the problems with the examples and notes striped.