## Learning Objectives

- The students should be able to apply advanced querying techniques using SQLAlchemy, such as filtering data and performing joins with custom query builders.
- The students should be able to demonstrate an understanding of ORM optimization techniques like pagination for large data sets.
- The students should be able to explain the concepts of lazy loading and eager loading in ORM and demonstrate their application in SQLAlchemy.




#### ORM Advanced Querying with SQLAlchemy

We can take alot of these querying principles and further enhance the API we have been working on.

- Filtering products using .where(Object assertion), filter(Object assertion), filter_by(kwargs) and a query parameter search term
- Linking orders to products using our products attribute and Nested Schemas .join()
- Searching for order by order_id
- Searching for orders by customer_id
- Searching for orders by customer_name
- Searching for products whose names are like "a search term"


#### Pagination:
Pagination allows for optimization when dealing with large datasets. With pagination we are able to carve our data into condensed packages determined by the end user.

