create table SALE(
    id NUMBER(3) CONSTRAINT sale_id_pk PRIMARY KEY,
    id_product NUMBER(3),
    id_point_of_sale NUMBER(3),
    quantity NUMBER(5) CONSTRAINT sale_quant_nn NOT NULL,
    id_customer NUMBER(3),
    id_seller NUMBER(3),
    FOREIGN KEY(id_product) references PRODUCT(id),
    FOREIGN KEY(id_point_of_sale) references POINT_OF_SALE(id),
    FOREIGN KEY(id_customer) references CUSTOMER(id),
    FOREIGN KEY(id_seller) references SELLER(id)
)
/