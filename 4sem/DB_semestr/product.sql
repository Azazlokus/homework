create table PRODUCT(
    id NUMBER(3) CONSTRAINT prod_id_pk PRIMARY KEY,
    name VARCHAR2(20) CONSTRAINT prod_name_nn NOT NULL,
    measure_unit VARCHAR2(5)
)
/