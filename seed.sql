TRUNCATE TABLE fruit;

ALTER SEQUENCE fruit_id_seq RESTART WITH 1;

INSERT INTO fruit(genus, name, family, order_name, carbohydrate, protein, fat, calories, sugar) VALUES ('Malus', 'Apple', 'Rosaceae', 'Rosales', 11.4, 0.3, 0.4, 52, 10.3);
INSERT INTO fruit(genus, name, family, order_name, carbohydrate, protein, fat, calories, sugar) VALUES ('Prunus', 'Apricot', 'Rosaceae', 'Rosales', 3.9, 0.5, 0.1, 15, 3.2);
INSERT INTO fruit(genus, name, family, order_name, carbohydrate, protein, fat, calories, sugar) VALUES ('Musa', 'Banana', 'Musaceae', 'Zingiberales', 22, 1, 0.2, 96, 17.2);
INSERT INTO fruit(genus, name, family, order_name, carbohydrate, protein, fat, calories, sugar) VALUES ('Rubus', 'Blackberry','Rosaceae', 'Rosales', 9, 1.3, 0.4, 40, 4.5);
INSERT INTO fruit(genus, name, family, order_name, carbohydrate, protein, fat, calories, sugar) VALUES ('Fragaria', 'Blueberry','Rosaceae', 'Rosales', 5.5, 0, 0.4, 29, 5.4);
INSERT INTO fruit(genus, name, family, order_name, carbohydrate, protein, fat, calories, sugar) VALUES ('Prunus', 'Cherry','Rosaceae', 'None', 12, 1, 0.3, 50, 8);
INSERT INTO fruit(genus, name, family, order_name, carbohydrate, protein, fat, calories, sugar) VALUES ('Ficus', 'Fig','Moraceae', 'Rosales', 19, 0.8, 0.3, 74, 16);
INSERT INTO fruit(genus, name, family, order_name, carbohydrate, protein, fat, calories, sugar) VALUES ('Ribes', 'Gooseberry','Grossulariaceae', 'Saxifragales', 10, 0.9, 0.6, 44, 0);
INSERT INTO fruit(genus, name, family, order_name, carbohydrate, protein, fat, calories, sugar) VALUES ('Vitis', 'Grapes','Vitaceae', 'Vitales', 18.1, 0.72, 0.16, 69, 15.48);
INSERT INTO fruit(genus, name, family, order_name, carbohydrate, protein, fat, calories, sugar) VALUES ('Psidium', 'Guava','Myrtaceae', 'Myrtales', 14, 2.6, 1, 68, 9);