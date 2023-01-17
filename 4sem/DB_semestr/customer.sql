create table CUSTOMER(
    id NUMBER(3) CONSTRAINT cust_id_pk PRIMARY KEY,
    first_name VARCHAR2(25),
    last_name VARCHAR2(25) CONSTRAINT cust_last_name_nn NOT NULL
)
/