create table SELLER(
    id NUMBER(3) CONSTRAINT sel_id_pk PRIMARY KEY,
    id_point_of_sale NUMBER(3),
    first_name VARCHAR2(25),
    last_name VARCHAR2(25) CONSTRAINT sel_last_name_nn NOT NULL,
    phone VARCHAR2(11),
    foreign key(id_point_of_sale) references POINT_OF_SALE(id)
)
/