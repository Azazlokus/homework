/* УДАЛЕНИЕ ТАБЛИЦ */
@@drop customer
@@drop sale
@@drop point_of_sale
@@drop seller
@@drop ord
@@drop product
@@drop storage
@@drop supplier
/* УДАЛЕНИЕ ПОСЛЕДОВАТЕЛЬНОСТЕЙ */
drop sequence customer_id_seq;
drop sequence seller_id_seq;
drop sequence point_of_sale_id_seq;
drop sequence ord_id_seq;
drop sequence supplier_id_seq;
drop sequence product_id_seq;
drop sequence sale_id_seq;
/* СОЗДАНИЕ ПОСЛЕДОВАТЕЛЬНОСТЕЙ */
create sequence customer_id_seq;
create sequence seller_id_seq;
create sequence point_of_sale_id_seq;
create sequence ord_id_seq;
create sequence supplier_id_seq;
create sequence product_id_seq;
create sequence sale_id_seq;
/* СОЗДАНИЕ ТАБЛИЦ */
@@customer
@@supplier
@@point_of_sale
@@product
@@ord
@@storage
@@seller
@@sale
/* ВЫВОД СТРУКТУРЫ ТАБЛИЦ */
@@desc_table
/* ВЫВОД ОГРАНИЧЕНИЙ ТАБЛИЦ */
column column_name format a15;
@@cons customer
@@cons sale
@@cons point_of_sale
@@cons seller
@@cons ord
@@cons product
@@cons storage
@@cons supplier
/* ВСТАВКА ДАННЫХ В ТАБЛИЦЫ */
@@intoCustomer 'Magee' 'Vel'
@@intoCustomer 'Ngao' 'Mnic'
@@intoCustomer 'Paul' 'Brant'
@@intoSupplier NULL 'FruitWorld' '72813-15'
@@intoSupplier 'Tokyo, Japan' 'Mix' NULL
@@intoSupplier 'Moscow, Russia' 'Colld' '731-12-321'
@@intoProduct 'red apple' 1
@@intoProduct 'banana' 1
@@intoProduct 'pinapple' 1
@@intoProduct 'potato' 2
@@intoPoint_of_sale 'larek' 'Moscow, Russia' 'FruitsForYou'
@@intoPoint_of_sale 'supermarket' 'Novosibirsk, Russia' 'TheSweetestWorld'
@@intoPoint_of_sale 'larek' 'Tokyo, Japan' 'GoodDay'
@@intoSeller 1 'Max' 'Cool' NULL
@@intoSeller 2 'Paul' 'Beat' '871-321-33'
@@intoSeller 2 'Frank' 'Berd' '932-12-333'
@@intoSeller 3 'Marta' 'Stuart' '3321-3234-2'
@@intoSeller 1 'Candal' 'Hip' NULL
@@intoOrd 2 1 1 '19.01.2022' '20.01.2022' 1000 100
@@intoOrd 3 2 1 '27.03.2022' '01.04.2022' 1500 100
@@intoOrd 3 1 2 '19.05.2022' '22.05.2022' 1300 70
@@intoOrd 4 3 2 '07.03.2022' '01.04.2022' 1240 75
@@intoOrd 1 3 3 '03.07.2022' '07.07.2022' 1300 200
@@intoOrd 4 1 3 '10.12.2022' '11.12.2022' 1300 500
@@intoOrd 2 2 2 '03.09.2022' '20.09.2022' 1300 2000
@@intoStorage 1 1 0 15.1 NULL
@@intoStorage 2 1 10 10 NULL
@@intoStorage 3 1 32 8.7 NULL
@@intoStorage 4 1 4 2.1 NULL
@@intoStorage 1 2 2 7.1 NULL
@@intoStorage 2 2 7 3.2 NULL
@@intoStorage 3 2 14 9.9 NULL
@@intoStorage 4 2 7 7.1 NULL
@@intoStorage 1 3 8 12.99 NULL
@@intoStorage 2 3 43 7.99 NULL
@@intoStorage 3 3 11 6.7 NULL
@@intoStorage 4 3 25 1.99 NULL
@@intoSale 1 1 10 1 5
@@intoSale 1 2 5 2 4
@@intoSale 1 3 7 2 4
@@intoSale 2 1 50 1 4
@@intoSale 2 2 10 2 4
@@intoSale 2 3 5 2 4
@@intoSale 3 1 5 1 4
@@intoSale 3 2 2 2 5
@@intoSale 3 3 5 2 4
@@intoSale 4 1 2 1 5
@@intoSale 4 2 2 2 4
@@intoSale 4 3 1 2 4
/* ВЫВОД СОДЕРЖИМОГО ТАБЛИЦ */
@@select_all