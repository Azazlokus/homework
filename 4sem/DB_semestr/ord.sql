create table ORD(
    id NUMBER(3) CONSTRAINT ord_id_pk PRIMARY KEY,
    id_product NUMBER(3),
    id_supplier NUMBER(3),
    id_point_of_sale NUMBER(3),
    date_ordered DATE,
    date_shipped DATE,
    total_price NUMBER(10) CONSTRAINT ord_total_nn NOT NULL,
    quantity NUMBER(5),
    CONSTRAINT ord_id_prod_fk FOREIGN KEY(id_product) references PRODUCT(id),
    CONSTRAINT ord_id_sup_fk FOREIGN KEY(id_supplier) references SUPPLIER(id),
    CONSTRAINT ord_id_pos_fk FOREIGN KEY(id_point_of_sale) references POINT_OF_SALE(id)
)
/