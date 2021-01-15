# 쇼핑몰 데이터베이스


CREATE TABLE users(
	id NVARCHAR(10) PRIMARY KEY, 
	pwd NVARCHAR(10) NOT NULL,
	name NVARCHAR(20) NOT NULL,
	age INT(10) NULL CHECK (age >= 1 AND age <= 999) DEFAULT -1,
	addr NVARCHAR(20) NOT NULL DEFAULT '서울'
);

INSERT INTO users VALUES('id01', 'pw01', 'name1', 20, default);
INSERT INTO users VALUES('id02', 'pw02', 'name2', 25, '인천');
INSERT INTO users VALUES('id03', 'pw03', 'name3', 45, '경기');
INSERT INTO users VALUES('id04', 'pw04', 'name4', 54, '대전');
INSERT INTO users VALUES('id05', 'pw05', 'name5', 14, '제주');
SELECT * FROM users;




CREATE TABLE items(
	id INT(10) AUTO_INCREMENT PRIMARY KEY, 
	name NVARCHAR(10) NOT NULL,
	price INT(10) NOT NULL,
	regdate DATE NOT NULL
);

INSERT INTO items VALUES(id, 'name1', 1000, CURRENT_DATE);
INSERT INTO items VALUES(id, 'name2', 25000, CURRENT_DATE);
INSERT INTO items VALUES(id, 'name3', 4000, CURRENT_DATE);
INSERT INTO items VALUES(id, 'name4', 9900, CURRENT_DATE);
INSERT INTO items VALUES(id, 'name5', 500, CURRENT_DATE);
SELECT * FROM items;



CREATE TABLE cart(
	id INT(10) AUTO_INCREMENT PRIMARY KEY, 
	userid NVARCHAR(10),
	itemid INT(10)
);
ALTER TABLE cart
	ADD CONSTRAINT FK_users_cart
	FOREIGN KEY (userid)
	REFERENCES users(id);
ALTER TABLE cart
	ADD CONSTRAINT FK_items_cart
	FOREIGN KEY (itemid)
	REFERENCES items(id);
INSERT INTO cart VALUES(id, 'id01', 2);
INSERT INTO cart VALUES(id, 'id01', 1);
INSERT INTO cart VALUES(id, 'id02', 3);
INSERT INTO cart VALUES(id, 'id04', 4);
INSERT INTO cart VALUES(id, 'id05', 3);
SELECT * FROM cart;
	
	
	
	
CREATE TABLE orders(
	id INT(10) AUTO_INCREMENT PRIMARY KEY, 
	userid NVARCHAR(10),
	itemid INT(10),
	regdate DATE NOT NULL,
	qt INT(10) NULL DEFAULT 1
);
ALTER TABLE orders
	ADD CONSTRAINT FK_users_orders
	FOREIGN KEY (userid)
	REFERENCES users(id);
ALTER TABLE orders
	ADD CONSTRAINT FK_items_orders
	FOREIGN KEY (itemid)
	REFERENCES items(id);
INSERT INTO orders VALUES(id, 'id01', 1, CURRENT_DATE, default);
INSERT INTO orders VALUES(id, 'id01', 1, CURRENT_DATE, 3);
INSERT INTO orders VALUES(id, 'id02', 3, CURRENT_DATE, default);
INSERT INTO orders VALUES(id, 'id04', 4, CURRENT_DATE, 10);
INSERT INTO orders VALUES(id, 'id05', 3, CURRENT_DATE, 5);
SELECT * FROM orders;
	
	
	
CREATE TABLE favorite(
	userid NVARCHAR(10),
	itemid INT(10),
	CONSTRAINT PK_favorite_userid_itemid
		PRIMARY KEY (userid, itemid)
);
ALTER TABLE favorite
	ADD CONSTRAINT FK_users_favorite
	FOREIGN KEY (userid)
	REFERENCES users(id);
ALTER TABLE favorite
	ADD CONSTRAINT FK_items_favorite
	FOREIGN KEY (itemid)
	REFERENCES items(id);
INSERT INTO favorite VALUES('id01', 1);
INSERT INTO favorite VALUES('id01', 3);
INSERT INTO favorite VALUES('id02', 3);
INSERT INTO favorite VALUES('id04', 4);
INSERT INTO favorite VALUES('id05', 3);
SELECT * FROM favorite;
	

	
CREATE TABLE rate(
	userid NVARCHAR(10),
	itemid INT(10),
	ratenum INT(10) NOT NULL,
	CONSTRAINT PK_rate_userid_itemid
		PRIMARY KEY (userid, itemid)
);
ALTER TABLE rate
	ADD CONSTRAINT FK_users_rate
	FOREIGN KEY (userid)
	REFERENCES users(id);
ALTER TABLE rate
	ADD CONSTRAINT FK_items_rate
	FOREIGN KEY (itemid)
	REFERENCES items(id);
INSERT INTO rate VALUES('id01', 1, 10);
INSERT INTO rate VALUES('id01', 3, 6);
INSERT INTO rate VALUES('id02', 3, 10);
INSERT INTO rate VALUES('id04', 4, 2);
INSERT INTO rate VALUES('id05', 3, 8);
SELECT * FROM rate;


# 장바구니 리스트
# 주문자 아이디,주문자 이름, 제품이름, 제품가격
SELECT userid, users.name as username, items.name as itemname, items.price
FROM cart 
	INNER JOIN users 
		ON cart.userid = users.id
	INNER JOIN items 
		ON cart.itemid = items.id;

# id01의 주문  리스트 
# 주문번호, 주문자 아이디,주문자 이름, 주문자 주소, 제품이름, 제품가격, 주문날짜, 수량
SELECT orders.id as orderid, userid, users.name as username, users.addr, items.name as itemname, items.price, qt
FROM orders 
	INNER JOIN users 
		ON orders.userid = users.id
	INNER JOIN items 
		ON orders.itemid = items.id;

# id01의 좋아요 리스트
# 사용자 아이디, 제품 이름
SELECT userid, items.name as itemname
FROM favorite 
	INNER JOIN items 
		ON favorite.itemid = items.id
WHERE userid = 'id01';

# 상품 3의 별점 리스트
# 사용자 아이디, 제품 이름, 별점
SELECT userid, rateNum
FROM rate 
	INNER JOIN items 
		ON rate.itemid = items.id
WHERE itemid = 3;

