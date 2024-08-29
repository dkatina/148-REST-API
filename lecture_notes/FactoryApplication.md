## Learning Objectives

- Students should be able to design REST APIs using best practices for resource naming, endpoint structuring, and efficient patterns, ensuring scalability and maintainability.
- Students should be able to apply modularization in REST APIs and demonstrate how to apply it effectively to improve code maintainability, reusability, and scalability.
- Students should be able to understand the concept of caching and how to apply it in REST APIs to improve performance and efficiency.
- Students should be able to grasp the significance of setting rate limits in REST APIs and how to apply rate-limiting strategies to ensure fair and sustainable use of server resources.

#### Recap

##### Naming Convention:
- Use Plural Nouns for resource names
```python
/products
/customers
/orders
```
Use plural even when accessing single items of a collection
```python
/products/{id}
```
- Hyphens to separate words
```python
/product-categories
```
- Always lowercase
- Use Query parameters for filtering, sorting, and pagination (NEW)
`/products?category=electronics` (query params start after a question mark)
`/products?sort=price` (param=value)
`/products?limit=10&offset=20` (Multiple params separated by &)

### Advanced API Patterns

So far we've been able to create a full api all on a single document, while we can continue to do so this format lends itself to becoming cumbersome and difficult to maintain as the api gets more complex. This is why we turn to the `Factory Aplication Pattern`

##### Factory Aplication Pattern:
Allows for a more dynamic and scaleable API because it allows us to break our api into sub-units called blueprint, each responsible for a different capabilities, we then configure our API with these desired blueprints, allowing us to slot in and take off blueprints at will.

The overall file structer of an API broken into a Factory Application will look something like this.
```
Project folder
├── app.py
├── config.py
├── database.py
├── controllers
│   ├── __init__.py
├── models
│   ├── __init__.py
│   └── schemas
│       ├── __init__.py
├── requirements.txt
├── routes
│   ├── __init__.py
└── services
    ├── __init__.py
```

###### Today's Required packages
requirements.txt
```
Flask
Flask-SQLAlchemy
flask_marshmallow
marshmallow-sqlalchemy
mysql-connector-python
```
`pip install -r requirements.txt` To install these packages from the above page

#### General Flow
- **Create Config file (config.py)**: The config file is responsible for configuring the  the attributes of your flask API (database URI string: 'mysql+mysqlconnector://root:password@localhost/database')
- **Create Database file (database.py)**: This file is responsible for configuring and initializing our SQLAlchemy database.
- **Create our Application Factory (app.py)**: Here we create a function that will initialize our Flask App, configure the app using our config file, connect our app to our db, and also lay the ground work for our app schemas

#### Creating Blueprints

- **Initialize Blueprint** (routes folder)
- **Create Model**: database table (models folder)
- **Create Accompanying Schema(s)**: to aid in Validation of data (schemas folder)
- **Do the Following for Each Route**
    - **Create the Service** (services folder): Services serve data to and from the database
    - **Create the Controller** (controllers folder): Controllers validate, serialize, and deserialize, imported and exported data. Send validated data to service to store in database.
    - **Create Route Endpoint** (blueprint file): This route will trigger the controller
- **Register your blueprint** (app.py)

![blueprint](https://miro.medium.com/v2/resize:fit:720/format:webp/1*Vu2ThQPxr72UEOP0LMo4hA.jpeg)

### API Throttling and Rate Limiting:
This is the process of controlling the number of requests that can be made to an API within a certain period, to prevent abuse and ensure the API isn't overwhelmed
https://flask-limiter.readthedocs.io/en/stable/

```python
pip install flask-limiter
```

- **Initialize Limiter** (limiter.py)
- **Configure Limiter on App** (app.py): Set how many times a blueprint can be accessed

```
[count] [per|/] [n (optional)] [second|minute|hour|day|month|year][s]
```

### Caching:
https://flask-caching.readthedocs.io/en/latest/
Caching is the process of storing frequently access data in memory, to reduce the number of queries that need to be made. This not only reduce traffic to your database but also increases the speed of retrieval.

The downside to caching is that it is not updated as frequently, so while you get the info faster there is a chance it is incomplete.
```
pip install flask-caching
```
- **Instantiate Cache** (cache.py)
- **Add Cache Type to Config** (config.py)
- **Initialize Cache on App** (app.py)
- **Wrap the Controllers you wish to Cache** (controllers folder)