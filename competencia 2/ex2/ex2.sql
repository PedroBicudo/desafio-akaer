create database akaer_resolucao_ex2;
use akaer_resolucao_ex2;

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

insert into categories(id, name)
values 
	(1, 'Superior'),
	(2, 'Super Luxury'),
	(3, 'Modern'),	
	(4, 'Nerd'),
	(5, 'Infantile'),	
	(6, 'Robust'),
	(9, 'Wood');	

insert into products (name, amount, price, id_categories)
values
	('Blue Chair', 30, 300.00, 9),
	('Red Chair', 200, 2150.00, 2),
	('Diney Wardrobe', 400, 829.50, 4),
	('Blue Toaster', 20, 9.90, 3),
	('Solar Panel', 30, 3000.25, 4);

# Exercicio 2
select
	p.name,
	c.name
from products p
inner join categories c
	on c.id = p.id_categories
where 
	p.amount > 100 and
	p.id_categories in (1, 2, 3, 6, 9)
order by c.id;
