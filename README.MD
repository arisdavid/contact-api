## DEMO CELERY BEAT

## Build and run docker containers

Ensure in the root directory. Run all services in the background


```
docker-compose up --build -d
```


## Connect to postgres
### Connect
```
docker exec -it postgres_svcs psql -U dev postgres
```

### Switch to contact_management_db
```
\c contact_management_db
```

### List all tables
```
\dt
```

### Select * from contact;
```
select * from contact;
```


### Terminal Sample Commands
```

docker exec -it postgres_svcs psql -U dev postgres
psql (11.6 (Debian 11.6-1.pgdg90+1))
Type "help" for help.

postgres=# \c contact_management_db
You are now connected to database "contact_management_db" as user "dev".
contact_management_db=# \dt
        List of relations
 Schema |  Name   | Type  | Owner
--------+---------+-------+-------
 public | contact | table | dev
 public | email   | table | dev
(2 rows)

contact_management_db=# select * from contact;
 id  |   username   | first_name | last_name |        date_created
-----+--------------+------------+-----------+----------------------------
 976 | ogriffin     | Daniel     | Walters   | 2020-02-07 09:00:10.389303
 977 | timothy85    | Steven     | Newman    | 2020-02-07 09:00:25.394798
 978 | cesar08      | Donna      | Mcdowell  | 2020-02-07 09:00:40.411293
 979 | kristie60    | Lauren     | Marshall  | 2020-02-07 09:00:55.409154
 980 | weaverdaniel | Lori       | Williams  | 2020-02-07 09:01:10.405783
 981 | jcharles     | Debra      | Hill      | 2020-02-07 09:01:25.410651
(6 rows)

contact_management_db=#
```