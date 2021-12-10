DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    is_active BOOLEAN
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    item VARCHAR(255),
    description VARCHAR(255),
    category VARCHAR(255),
    stock_quantity INT,
    buying_cost INT,
    selling_price INT,
    manufacturer_id INT REFERENCES manufacturers(id) ON DELETE CASCADE
);