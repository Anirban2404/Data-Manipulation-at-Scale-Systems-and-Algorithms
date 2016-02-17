Problem 2: Matrix Multiplication in SQL

Recall from lecture that a sparse matrix has many positions with a value of zero.

Systems designed to efficiently support sparse matrices look a lot like databases: They represent each cell as a record (i,j,value).
select mul_val from (
SELECT A.row_num, B.col_num, SUM(A.value * B.value) as mul_val
  FROM A, B
 WHERE A.col_num = B.row_num
 GROUP BY A.row_num, B.col_num
)
where row_num = 2 and col_num = 3
;

