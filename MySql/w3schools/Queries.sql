use w3schools;
show tables;
--- selects the "CustomerName", "City", and "Country" columns from the "Customers" table
SELECT CustomerName, City, Country FROM Customers;

--- selects ALL the columns from the "Customers" table
SELECT * FROM Customers;

--- selects only the DISTINCT values from the "Country" column in the "Customers" table
SELECT DISTINCT Country FROM Customers;

--- counts and returns the number of different (distinct) countries in the "Customers" table
SELECT COUNT(DISTINCT Country) FROM Customers;

---  selects all the customers from "Mexico"
SELECT * FROM Customers
WHERE country = 'Mexico';
SELECT * FROM Customers
WHERE CustomerID = 1;

--- selects all fields from "Customers" where country is "Germany" AND city is "Berlin"
SELECT * FROM Customers
WHERE Country = 'Germany' AND City = 'Berlin';
SELECT * FROM Customers
WHERE City = 'Berlin' OR City = 'Stuttgart';
SELECT * FROM Customers
WHERE NOT Country = 'Germany';
SELECT * FROM Customers
WHERE Country = 'Germany' AND (City = 'Berlin' OR City = 'Stuttgart');
SELECT * FROM Customers
WHERE NOT Country = 'Germany' AND NOT Country = 'USA';

--- selects all customers from the "Customers" table, sorted by the "Country" column
SELECT * FROM Customers
ORDER BY Country;
SELECT * FROM Customers
ORDER BY Country DESC;
SELECT * FROM Customers
ORDER BY Country, CustomerName;

---  lists all customers with a NULL value in the "Address" field
SELECT CustomerName, ContactName, Address
FROM Customers
WHERE Address IS NULL;

--- updates the first customer (CustomerID = 1) with a new contact person and a new city
UPDATE Customers
SET ContactName = 'Alfred Schmidt', City = 'Frankfurt'
WHERE CustomerID = 1;

---  deletes the customer "Alfreds Futterkiste" from the "Customers" table
DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';

--- selects the first three records from the "Customers" table
SELECT * FROM Customers
LIMIT 3;

--- finds the price of the cheapest and expensive product
SELECT MIN(Price) AS SmallestPrice
FROM Products;
SELECT MAX(Price) AS LargestPrice
FROM Products;

--- finds the count,sum,avg of products
SELECT COUNT(ProductID)
FROM Products;
SELECT AVG(Price)
FROM Products;
SELECT SUM(Quantity)
FROM Order_details;

--- selects all customers with a CustomerName starting/ending with "a"
SELECT * FROM Customers
WHERE CustomerName LIKE 'a%';
SELECT * FROM Customers
WHERE CustomerName LIKE '%a';

--- selects all customers that are located in "Germany", "France" or "UK"
SELECT * FROM Customers
WHERE Country IN ('Germany', 'France', 'UK');

--- selects all customers that are from the same countries as the suppliers
SELECT * FROM Customers
WHERE Country IN (SELECT Country FROM Suppliers);

--- selects all products with a price between 10 and 20
SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20;
SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20
AND CategoryID NOT IN (1,2,3);
SELECT * FROM Orders
WHERE OrderDate BETWEEN '1996-07-01' AND '1996-07-31';

--- Alias for Columns 
SELECT CustomerName AS Customer, ContactName AS "Contact Person"
FROM Customers;
SELECT CustomerName, CONCAT_WS(', ', Address, PostalCode, City, Country) AS Address
FROM Customers;

--- Joins
SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
ORDER BY Customers.CustomerName;
SELECT Orders.OrderID, Employees.LastName, Employees.FirstName
FROM Orders
RIGHT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
ORDER BY Orders.OrderID;

--- Union
SELECT City FROM Customers
UNION
SELECT City FROM Suppliers
ORDER BY City;

--- lists the number of customers in each country
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country;

SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) > 5;