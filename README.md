# flask-graphQL-example
graphQL example API in flask

## build and up

```
  docker-compose build
  docker-compose up
```

## database migrate

```
  docker-compose exec api flask db upgrade
```

## seed data

```
  docker-compose exec api flask seed sample
```

## try it

you can try it graphiql

```
{
  users {
    edges {
      node {
        id
        name
        githubId
        avatar
        photos {
          edges {
            node {
              id
              url
              category
            }
          }
        }
      }
    }
  }
}
```

## used packages

```
flask = "*"
flask-graphql = "*"
graphene = ">=2.0"
graphene-sqlalchemy = "*"
flask-sqlalchemy = "*"
pymysql = "*"
inflection = "*"
flask-migrate = "*"
```
