create table SUPPLIER(
    id NUMBER(3) CONSTRAINT sup_id_pk PRIMARY KEY,
    address VARCHAR2(25),
    name VARCHAR2(20) CONSTRAINT sup_name_nn NOT NULL,
    phone VARCHAR2(11)
)
/