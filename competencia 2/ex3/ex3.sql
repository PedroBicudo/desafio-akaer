create database akaer_resolucao_ex3;
use akaer_resolucao_ex3;

create table categories (
	id int primary key auto_increment,
	name varchar(255)
);

create table products (
	id int primary key auto_increment,
	name varchar(255),
	amount int,
	price float(10, 2),
	id_categories int
);

alter table products
add constraint fk_categories_products
foreign key (id_categories) references categories(id);

insert into categories (name)
values 
	('wood'),
	('luxury'),
	('vintage'),
	('modern'),
	('super luxury');

insert into products (name, amount, price, id_categories)
values
	('Two-doors wardrobe', 100, 800.00, 1),
	('Dining Table', 1000, 560.00, 3),
	('Towel holder', 10000, 25.50, 4),
	('Computer desk', 350, 320.50, 2),
	('Chair', 3000, 210.64, 4),
	('Single bed', 750, 460.00, 1);


# Exercicio 3
select
	c.name,
	sum(p.amount) as sum
from products p
inner join categories c
	on c.id = p.id_categories
group by p.id_categories;