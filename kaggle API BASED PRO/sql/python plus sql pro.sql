CREATE TABLE superstore_sales (
    row_id INT,
    order_id VARCHAR(50),
    order_date DATE,
    ship_date DATE,
    ship_mode VARCHAR(50),
    customer_id VARCHAR(50),
    customer_name VARCHAR(100),
    segment VARCHAR(50),
    country VARCHAR(50),
    city VARCHAR(50),
    state VARCHAR(50),
    postal_code INT,
    region VARCHAR(50),
    product_id VARCHAR(50),
    category VARCHAR(50),
    sub_category VARCHAR(50),
    product_name VARCHAR(200),
    sales FLOAT,
    quantity INT,
    discount FLOAT,
    profit FLOAT,
    order_year INT,
    order_month INT,
    profit_margin FLOAT
);

SELECT COUNT(*) FROM superstore_sales;
SELECT TOP 5 * FROM superstore_sales;

SELECT order_year, SUM(sales) total_sales, SUM(profit) total_profit
FROM superstore_sales
GROUP BY order_year
ORDER BY order_year;

SELECT TOP 5 product_name, SUM(profit) total_profit
FROM superstore_sales
GROUP BY product_name
ORDER BY total_profit DESC;

SELECT region, SUM(sales) total_sales
FROM superstore_sales
GROUP BY region
ORDER BY total_sales DESC;

SELECT discount, SUM(profit) total_profit
FROM superstore_sales
GROUP BY discount
ORDER BY discount;

SELECT segment, SUM(sales) total_sales, SUM(profit) total_profit
FROM superstore_sales
GROUP BY segment;


