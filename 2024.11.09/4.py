# Программа создает словарь, где ключами являются имена, а значениями - соответствующие им ключи, и позволяет искать ключ по имени.

err_book = {}

while True:
    line = input().strip()
    if not line: 
        break
        
    key, name = line.split()
    err_book[name] = key  

search_name = input().strip()

if search_name in err_book:
    print(err_book[search_name])  
else:
    print("! value error !")  

#1004 ER_CANT_ CREATE_ FILE
#1005 ER_CANT_CREATE_TABLE
#1006 ER_CANT_CREATE_DB
#1007 ER_DB_CREATE_EXISTS
#1008 ER_DB_DROP_EXISTS
#1010 ER_DB_DROP_RMDIR
#1016 ER_CANT_OPENFILE
#1022 ER_DUP_KEY

#ER_CANT_CREATE_DB
#1006

#4107 ER_SRS_UNUSED_PROJ_PARAMETER_PRESENT
#4108 ER_GIPK_COLUMN_EXISTS
#4111 ER_DROP_PK_COLUMN_TO_DROP_GIPK
#4113 ER DA_EXPIRE_LOGS_DAYS_IGNORED
#4114 ER_ CTE_RECURSIVE NOT UNION

#ER_CANT_OPEN_FILE
#! value error !
