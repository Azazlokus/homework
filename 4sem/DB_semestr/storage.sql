create table STORAGE(
    id_product NUMBER(3),
    id_point_of_sale NUMBER(3),
    quantity NUMBER(5),
    price NUMBER(5),
    manufacturer VARCHAR2(20),
    CONSTRAINT stor_id_pk PRIMARY KEY(id_product, id_point_of_sale),
    CONSTRAINT stor_id_prod_fk FOREIGN KEY(id_product) references PRODUCT(id),
    CONSTRAINT stor_id_pos_fk FOREIGN KEY(id_point_of_sale) references POINT_OF_SALE(id)
)
/