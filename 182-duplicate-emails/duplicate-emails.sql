# Write your MySQL query statement below
select distinct a.email as 'Email' from Person a, Person b
where a.email = b.email and a.id != b.id;