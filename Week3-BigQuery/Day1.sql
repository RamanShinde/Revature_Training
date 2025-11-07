create table
-- customers
CREATE TABLE sales_data.customers AS
SELECT 'C001' AS customer_id, 'Arun Kumar' AS name, 'Chennai' AS city, DATE('2022-03-15') AS join_date UNION ALL
SELECT 'C002', 'Priya Sharma', 'Bangalore', DATE('2023-01-20') UNION ALL
SELECT 'C003', 'Rahul Mehta', 'Hyderabad', DATE('2022-07-10') UNION ALL
SELECT 'C004', 'Sneha Reddy', 'Pune', DATE('2023-06-25') UNION ALL
SELECT 'C005', 'Vikram Das', 'Mumbai', DATE('2024-02-12');
-- products
CREATE OR REPLACE TABLE sales_data.products AS
SELECT 'P101' AS product_id, 'Laptop' AS name, 'Electronics' AS category, 65000.0 AS price UNION ALL
SELECT 'P102', 'Smartphone', 'Electronics', 35000.0 UNION ALL
SELECT 'P103', 'Office Chair', 'Furniture', 9000.0 UNION ALL
SELECT 'P104', 'Bookshelf', 'Furniture', 7500.0 UNION ALL
SELECT 'P105', 'Wireless Mouse', 'Accessories', 1200.0;

--Orders
CREATE OR REPLACE TABLE sales_data.orders AS
SELECT 'O001' AS order_id, 'C001' AS customer_id, 'P101' AS product_id, DATE('2024-05-12') AS order_date, 1 AS quantity, 65000.0 AS total_amount UNION ALL
SELECT 'O002', 'C002', 'P102', DATE('2024-05-18'), 2, 70000.0 UNION ALL
SELECT 'O003', 'C003', 'P103', DATE('2024-06-01'), 1, 9000.0 UNION ALL
SELECT 'O004', 'C001', 'P105', DATE('2024-06-10'), 3, 3600.0 UNION ALL
SELECT 'O005', 'C004', 'P104', DATE('2024-06-15'), 2, 15000.0 UNION ALL
SELECT 'O006', 'C005', 'P102', DATE('2024-07-02'), 1, 35000.0;


select * from `Sales_Data.customers`;
select * from `Sales_Data.orders`;
select * from `Sales_Data.products`;

-- It fetch the cid,name,join date
select customer_id as `cid`,name as `customer name`,join_date as `joining date`
from `Sales_Data.customers`;  -- when we right that time we use backtick for name

select customer_id as `cid`,name as `cutomer name`,join_date as `join date`
from `Sales_Data.customers`  where join_date >'2022-03-15'; -- when wwe deal with column that time use '' or ""


-- fetch the a letterin between name
select customer_id as `cid`,name as `customer name`,join_date as `joining date`
from `Sales_Data.customers` where name like "%a%";


select customer_id as `cid`,name as `customer name`,join_date as `joining date`
from `Sales_Data.customers` 
where customer_id in ('c001','c002');

select customer_id as `cid`,name as `customer name`,join_date as `joining date`
from `Sales_Data.customers` 
where join_date between '2022-01-01' and '2025-01-01';

select customer_id as `cid`,name as `customer name`,join_date as `joining date`
from `Sales_Data.customers` 
where join_date > '2022-03-15'
order by name;


-- products
-- It will return the product name with price and discounted price 
select product_id as `pid`,name as `product name`,price,price*0.9 as `Discounted_price`
from `Sales_Data.products`;

-- Orders
-- First top 3 purchesed products
select * from `Sales_Data.orders` order by
order_date desc limit 3;

--Remove duplicate by using Distinct 

select distinct city from `Sales_Data.customers`;

-- Extract year and month

select order_id, EXTRACT(YEAR from order_date) as `Order Year`
from `Sales_Data.orders`;
-- When we want to Extract from anythin then use Extrxt method (Extract from column_name)

-- Aggregation function 
select count(*) as total_orders,
       sum(total_amount) as total_sales,
       avg(total_amount) as avg_order_value
from `Sales_Data.orders`     


-- Group by
select 
