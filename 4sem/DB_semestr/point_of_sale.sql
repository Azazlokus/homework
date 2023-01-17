create table POINT_OF_SALE(
    id NUMBER(3) CONSTRAINT pos_id_pk PRIMARY KEY,
    type VARCHAR2(25) CONSTRAINT pos_type_nn NOT NULL,
    address VARCHAR2(25),
    name VARCHAR2(20) CONSTRAINT pos_name_nn NOT NULL
)
/