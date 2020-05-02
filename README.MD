## REST API and GraphQL Kubernetes Demo

## Introduction
This is a kubernetes demo with flask and celery beat scheduling a task to populate a Postgres database periodically with mock contact data.
The data is then exposed through REST endpoint as well as through GraphQL.

All running inside a Kubernetes cluster. 

Core components:
- Flask - Web App
- Celery and Celery beat
- Redis - Task queue
- Postgres - Storing Data
- GraphQL
- REST - REST API

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

Query All
```
{
  contacts{
    id,
    username,
    firstName,
    lastName,
    emails{
      edges{
        node{
          email
        }
      }
    }
  }
}

```
Query by ID
```
{
  contact(id:"Q29udGFjdDoy"){
    id,
    username,
    emails{
      edges{
        node{
          email
        }
      }
    }
  }
}
```

![GraphQL](https://github.com/arisdavid/graphql-contacts/blob/master/src/static/img/graphql.PNG)

#### REST API
`http://minikube_ip:30008/contact`

![RESTAPI](https://github.com/arisdavid/graphql-contacts/blob/master/src/static/img/rest.PNG)


## Connect to PostgreSQL
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
