## Learning Objectives

- The students should be able to understand the importance of keeping API documentation up to date and demonstrate this understanding by regularly updating their own API documentation.
- The students should be able to comprehend the significance of documenting authentication and authorization requirements for API security and apply this knowledge to their own API projects.

- The students should be able to understand and implement the use of swagger as the main documentation tool for the correct interaction with API services.\

#### API Documentation
This is essentially a user manual to our API, and tells developers how they can interact with all of the API's resources.

## **Best Practices for Effective API Documentation**

Creating effective API documentation is an art and a science. Here are some best practices to follow:

1. **Be Clear and Concise**: API documentation should be easy to read and understand. Use simple language, avoid jargon, and include plenty of examples.
2. **Provide Detailed Examples**: Showcase what the API can do and how to use it. Include examples for every endpoint and data format.
3. **Keep It Up to Date**: API documentation should always be accurate and up to date. When you make changes to the API, adjust the documentation accordingly
4. **Organize It Well**:  API documentation should have a clear structure with logical sections and a table of contents.
5. **Offer Support and Feedback**: API documentation should provide ways for developers to ask questions and give feedback.

## **Using Swagger for Creating and Maintaining API Documentation**

Swagger is like an inventory management system for your API. It helps you create, maintain, and organize your API documentation in a structured and user-friendly way. With Swagger, you can define your API's endpoints, request and response formats, authentication methods, and more using a simple YAML or JSON format.

```bash
pip install flask-swagger flask_swagger_ui
```

Create a `static` folder and a `swagger.yaml` file which we will use to configure our documentation with the following boiler plate.

```yaml
swagger: '2.0'
info:
  title: "API name"
  description: "Brief description"
  version: "1.0.0"
host: "127.0.0.1:5000" #working on local host
schemes:
  - "http"
consumes:
  - "application/json"
produces:
  - "application/json"
paths: {}
definitions: {}
```

##### Now we can set up Swagger in our app.py

we'll do this by creating a swagger_blueprint (similar to a flask blueprint), and register it to our app.

YOU WILL NEED TO CONFIGURE A RATE LIMIT FOR THE SWAGGER_BLUEPRINT!
- When you access the swagger docs, it will immediatly fire ~6 requests, which will exceed the default limit we set of 3 per second. So add a customer limit for the swagger_blueprint of 10 per second

##### Now it's time to build out the documentation in `swagger.yaml`.

A genral rule of thumb for creating the documentation for each route:

- In definitions, create a schema for the route payload, outlining what the route is expecting (A necessary step for all POST requests)
- Then in definitions, create a schem for the route response, outling the what will be sent back to the view.
- In paths, create a path for the url endpoint, using the payload, and response schemas to add detail to the path UI.
-Add an example response

##### Adding Security Definitions
Allow you to create authentication schemes to be used on secure routes, outline what kind of authorization is required to access the route.

Add the following to your `swagger.yaml`:

```yaml
securityDefinitions:
  bearerAuth:
    type: apiKey
    name: Authorization
    in: header
```

With this in place we can add bearerAuth as a security parameter to any one of our paths we need to protect.