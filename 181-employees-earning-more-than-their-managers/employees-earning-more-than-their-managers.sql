# Write your MySQL query statement below
-- select a.Name as 'Employee'
-- from Employee as a, Employee as b
-- where a.ManagerId = b.id and a.salary > b.salary;

select a.Name as 'Employee'
from Employee as a join Employee as b
on a.ManagerId = b.id where a.salary > b.salary;