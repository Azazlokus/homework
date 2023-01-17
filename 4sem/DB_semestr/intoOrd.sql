insert into ORD
values (ord_id_seq.nextval, &1, &2, &3, to_date('&4', 'DD/MM/YYYY'), to_date('&5', 'DD/MM/YYYY'), &6, &7)
/