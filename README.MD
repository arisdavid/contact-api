## REST API and GraphQL Demo Kubernetes Demo

## Instructions

##### Start Minikube
```
minikube start
```

##### Config namespace context
````
kubectl config set-context $(kubectl config current-context) --namespace=<namespace>
````

#### Build the docker image

```
make build
```

##### Install 
```
make install
```

#### GraphQL Query

`http://minikube_ip:30008/graphql`

```
query {
      contacts {
        username,
        emails{
          email
        }
      }
    }
```

#### REST API
`http://minikube_ip:30008/contact`



##### Connect to postgreSQL
```
psql -h <minikube_ip> -p 30080 -U admin -d contact_db
```

##### List all tables
```
\dt
```

##### Select * from contact;
```
select * from contact;
```

```

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