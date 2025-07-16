-- Last updated: 7/16/2025, 7:23:50 PM
# Write your MySQL query statement below
SELECT firstName, lastName, city, state
FROM Person LEFT OUTER JOIN Address
ON Person.personId = Address.personId