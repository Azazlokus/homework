select ucc.table_name, ucc.column_name, ucc.constraint_name, uc.constraint_type from 
user_constraints uc join user_cons_columns ucc
on uc.constraint_name = ucc.constraint_name
where lower(ucc.table_name) = lower('&1')
/