# Leetcode_similar_question_scraper
Builds a database of similar questions from leetcode.

The output will be a csv fo form "question 1", "question 2", score, dev (if it is part of the dev set)

20% of the total pairs will be in the dev set. There is currently no test set. 

the score is out of 5 and is determined by the "similar question" category and "Related Topics" tags on the question on leetcode. 

Questions taged in similar question will recieve a score of 5. Score of other pairs of questions are determined by the amount of Related Topics tags they share.
