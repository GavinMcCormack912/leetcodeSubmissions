-- Last updated: 7/21/2025, 8:35:29 PM
-- Write your PostgreSQL query statement below
SELECT employee.name AS Employee
FROM employee
JOIN employee manager ON employee.managerId = manager.id
WHERE employee.salary > manager.salary
