CREATE TABLE brands (
    brand_id INTEGER NOT NULL,
    brand_name VARCHAR(50) NOT NULL
);

CREATE TABLE laptops (
    brand_id INTEGER NOT NULL,
    laptop_id INTEGER NOT NULL,
    laptop_name VARCHAR(50) NOT NULL
);

CREATE TABLE prices(
	laptop_id INTEGER NOT NULL,
	prices_id INTEGER NOT NULL,
	discount_price FLOAT NOT NULL,
	d_change_dis DATE NOT NULL, 
	old_price FLOAT NOT NULL,
	d_change_old DATE NOT NULL
); 

CREATE TABLE ratings(
	laptop_id INTEGER NOT NULL,
	ratings_id INTEGER NOT NULL,
	ratings_5max FLOAT NOT NULL,
	d_change_rgs DATE NOT NULL 
);

CREATE TABLE details (
    laptop_id INTEGER NOT NULL,
	details_id INTEGER NOT NULL,
    display_size FLOAT NOT NULL,
    processor_type VARCHAR(50) NOT NULL,
    graphics_card VARCHAR(50) NOT NULL,
    disk_space VARCHAR(50) NOT NULL
);

ALTER TABLE brands ADD CONSTRAINT PK_brand_id
PRIMARY KEY(brand_id);

ALTER TABLE laptops ADD CONSTRAINT PK_laptop_id
PRIMARY KEY(laptop_id);

ALTER TABLE laptops ADD CONSTRAINT FK_laptop_brand
FOREIGN KEY(brand_id) REFERENCES brands(brand_id);

ALTER TABLE details ADD CONSTRAINT PK_details_id
PRIMARY KEY(details_id);

ALTER TABLE details ADD CONSTRAINT FK_details_laptop
FOREIGN KEY(laptop_id) REFERENCES laptops(laptop_id);

ALTER TABLE prices ADD CONSTRAINT PK_prices_id
PRIMARY KEY(prices_id);

ALTER TABLE prices ADD CONSTRAINT FK_prices_laptop
FOREIGN KEY(laptop_id) REFERENCES laptops(laptop_id);

ALTER TABLE ratings ADD CONSTRAINT PK_ratings_id
PRIMARY KEY(ratings_id);

ALTER TABLE ratings ADD CONSTRAINT FK_ratings_laptop
FOREIGN KEY(laptop_id) REFERENCES laptops(laptop_id);