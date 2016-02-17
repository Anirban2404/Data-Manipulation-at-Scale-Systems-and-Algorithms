/*
(i) keyword search: Find the best matching document to the keyword query "washington taxes treasury". 
You can add this set of keywords to the document corpus with a union of scalar queries:

SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count
Then, compute the similarity matrix again, but filter for only similarities involving the "query document": docid = 'q'. 
Consider creating a view of this new corpus to simplify things.
*/