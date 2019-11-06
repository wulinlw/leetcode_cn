#!/usr/bin/python
#coding:utf-8

# 第二高的薪水
# 编写一个 SQL 查询，获取 Employee 表中第二高的薪水（Salary） 。

# +----+--------+
# | Id | Salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+
# 例如上述 Employee 表，SQL查询应该返回 200 作为第二高的薪水。如果不存在第二高的薪水，那么查询应返回 null。

# +---------------------+
# | SecondHighestSalary |
# +---------------------+
# | 200                 |
# +---------------------+

# Write your MySQL query statement below

#使用offset
SELECT Salary FROM Employee GROUP BY Salary
UNION ALL (SELECT NULL AS Salary)
ORDER BY Salary DESC LIMIT 1 OFFSET 1;

select (select distinct Salary from Employee
order by Salary DESC 
limit 1 offset 1) as SecondHighestSalary

SELECT MAX(Salary) FROM Employee 
WHERE Salary NOT IN
(SELECT MAX(Salary) FROM Employee);


SELECT MAX(Salary) FROM Employee
Where Salary <
(SELECT MAX(Salary) FROM Employee);

SELECT MAX(Salary) FROM Employee E1
WHERE 1 =
(SELECT COUNT(DISTINCT(E2.Salary)) FROM Employee E2
WHERE E2.Salary > E1.Salary);


