-- Table: bootcampdb.user_purchase

DROP TABLE IF EXISTS bootcampdb.user_purchase;

CREATE TABLE IF NOT EXISTS bootcampdb.user_purchase
(
    invoice_number VARCHAR(10),
    stock_code VARCHAR(20),
    detail VARCHAR(1000),
    quantity int,
    invoice_date timestamp,
    unit_price numeric(8,3),
    customer_id int,
    country VARCHAR(20)    
);
