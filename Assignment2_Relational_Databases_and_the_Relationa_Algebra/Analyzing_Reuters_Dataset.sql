/* Problem 1: Inspecting the Reuters Dataset and Basic Relational Algebra 

/* 
(a) select: Write a query that is equivalent to the following relational algebra expression. 
   σdocid=10398_txt_earn(frequency) 
*/ 
SELECT Count(*) 
FROM   frequency 
WHERE  docid = '10398_txt_earn'; 

/* 
(b) select project: Write a SQL statement that is equivalent to the following relational algebra expression.
πterm(σdocid=10398_txt_earn and count=1(frequency)) 
*/ 
SELECT Count(*) 
FROM   frequency 
WHERE  docid = '10398_txt_earn' 
       AND count = 1; 

/* 
(c) union: Write a SQL statement that is equivalent to the following relational algebra expression. (Hint: you can use the UNION keyword in SQL)
πterm(σdocid=10398_txt_earn and count=1(frequency)) U πterm(σdocid=925_txt_trade and count=1(frequency))
*/ 
SELECT Count(term) 
FROM   (SELECT term 
        FROM   frequency 
        WHERE  docid = '10398_txt_earn' 
               AND count = 1 
        UNION 
        SELECT term 
        FROM   frequency 
        WHERE  docid = '925_txt_trade' 
               AND count = 1); 

/* 
(d) count: Write a SQL statement to count the number of unique documents containing the word "law"
 or containing the word "legal" (If a document contains both law and legal, it should only be counted once)
 */ 
SELECT Count(DISTINCT( docid )) 
FROM   frequency 
WHERE  term IN ( 'law', 'legal' ); 

/* 
(e) big documents Write a SQL statement to find all documents that have more than  
300 total terms, including duplicate terms. (Hint: You can use the HAVING clause,  
or you can use a nested query. Another hint: Remember that the count column contains  
the term frequencies, and you want to consider duplicates.) (docid, term_count) 
*/ 
SELECT Count(docid) 
FROM   (SELECT docid, 
               SUM(count) AS SUM 
        FROM   frequency 
        GROUP  BY docid 
        HAVING SUM > 300); 

/* 
(f) two words: Write a SQL statement to count the number of unique documents that  
contain both the word 'transactions' and the word 'world'. (Hint: Find the docs that  
contain one word and the docs that contain the other word separately, then find the intersection.)
*/ 
SELECT Count(DISTINCT( docid )) 
FROM   (SELECT DISTINCT( docid ) 
        FROM   frequency 
        WHERE  term = 'transaction' 
        INTERSECT 
        SELECT DISTINCT( docid ) 
        FROM   frequency 
        WHERE  term = 'world'); 