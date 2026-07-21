# Write your MySQL query statement below
select EmployeeUNI.unique_id , e.name from Employees e left join EmployeeUNI on e.id=EmployeeUNI.id;