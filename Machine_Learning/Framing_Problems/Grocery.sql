CREATE TABLE Products(
	product_id INT PRIMARY KEY,
	pro_name VARCHAR(20),
	uom_id INT,
	price_per_unit INT,
	FOREIGN KEY (uom_id) REFERENCES Uom(uom_id)
);

CREATE TABLE Uom (
	uom_id INT PRIMARY KEY,
	uom_name VARCHAR(20)
);



CREATE TABLE Orders(
	order_id INT PRIMARY KEY NOT NULL,
	customer_name VARCHAR(20),
	total DOUBLE PRECISION,
	datetime DATE
);

CREATE TABLE Order_details(
	order_id INT PRIMARY KEY NOT NULL,
	product_id INT NOT NULL,
	quantity DOUBLE PRECISION,
	total_price DOUBLE PRECISION,
	FOREIGN KEY(order_id) REFERENCES Orders(order_id),
	FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

SELECT*FROM Products;
SELECT*FROM Orders;
SELECT*FROM Order_details;
SELECT*FROM Uom;






