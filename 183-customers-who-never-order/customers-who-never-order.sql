# Write your MySQL query statement below
select Customers.name as 'Customers' from Customers
left join Orders o on Customers.id = o.customerId
where o.id is null;