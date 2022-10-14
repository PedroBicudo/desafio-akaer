create database akaer_resolucao_ex1;
use akaer_resolucao_ex1;

create table customers (
	id int primary key auto_increment,
	name varchar(255),
	street varchar(255),
	city varchar(255),
	state char(2),
	credit_limit int
);

create table orders (
	id int primary key auto_increment,
	orders_date date,
	id_customer int
);

alter table orders
add constraint fk_customers_orders
foreign key (id_customer) references customers(id);

insert into customers (name, street, city, state, credit_limit)
values 
	('Nicolas Diogo Cardoso', 'Acesso um', 'Porto Alegre', 'RS', 475),
	('Cecilia Olivia Rodrigues', 'Rua Sizuka Usuy', 'Cianorte', 'PR', 3170),
	('Augusto Fernando Carlos Eduardo Cardoso', 'Rua Baldomiro Koerich', 'Palhoça', 'SC', 1067),
	('Nicolas Diogo Cardoso', 'Acesso um', 'Porto Alegre', 'RS', 475),
	('Sabrina Heloisa Gabriela Barros', 'Rua Engenheiro Tito Marques Fernandes', 'Porto Alegre', 'RS', 4312),
	('Joaquim Diego Lorenzo Araújo', 'Rua Vitorino', 'Novo Haburgo', 'RS', 2314);

insert into orders(orders_date, id_customer)
values 
	('2016-05-13', 3),
	('2016-01-12', 2),
	('2016-04-18', 5),
	('2016-09-07', 4),
	('2016-02-13', 6),
	('2016-08-05', 3);


# Exercício 1
select
	c.name,
	o.id
from orders o
inner join customers c
	on o.id_customer = c.id
where 
	o.orders_date >= '2016-01-01' and
	o.orders_date <= '2016-06-30';
