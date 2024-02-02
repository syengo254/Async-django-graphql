## Async Django + Strawberry GraphQL + Daphne

### Description
With pagination.
This is to demonstrate a very fast Django 5.0  GraphQL API application that can query as databse with millions of rows.

### Instructions
1. Clone the repo
2. Navigate to project root and create virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual env using ```source ./venv/bin/activate```
4. Install requirements from the requirements.txt file using pip
   ```bash
   python -m pip install -r requirements.txt
   ```
5. Run migrations ```python manage.py migrate```
6. Seed database with data using: ```python manage.py seed_database```
7. Run dev server
   ```bash
   python manage.py runserver
   ```
8. browse graphQL endpoint at http://localhost:8000/graphql/

### Test Query
```gql
query allposts {
  allPosts(offset: 0, limit: 50) {
    items {
      id
      title
      author {
        id
      }
    }
    itemsCount
  }
```
<br />
```gql
query allposts {
  allPosts(offset: 0, limit: 50) {
    items {
      id
      title
      author {
        id
      }
    }
    itemsCount
  }
  allAuthors(offset: 0, limit: 20) {
    items {
      id
      name
    }
    itemsCount
  }
}
```


### License
Free

### Credits
- https://github.com/strawberry-graphql/strawberry
- https://strawberry-graphql.github.io/strawberry-graphql-django/
- https://www.djangoproject.com/
  
### Copyright
&copy; 2024-2042, David Syengo. All rights reserved.
