# What is an API? A Beginner's Guide with Python

Hello, I know, I promised to share with some of the things I learnt about Python FastAPI. But before doing that, I thought I should introduce what and API is and how does that work, because there could be friends who are completely new to the subject of API. So I prepared this quick and small module to cover my intentions! This module will introduce you to the concept of an API. By the end, you'll understand what an API is, what its key components are, and how to interact with one using a simple Python script.

## Part 1: What is an API? The Restaurant Analogy

First let's starts with what does the acronym API means. API stands for **Application Programming Interface**. That might sound complex, so let's use a simple analogy: a restaurant.

*   **You (the Customer)** are an application that needs something (in this case, data).
*   **The Kitchen** is another application or a server that has the data you want.
*   You can't just walk into the kitchen and get the food yourself. It's complex, you don't know the rules, and it's not allowed.

This is where the **Waiter (the API)** comes in. The waiter is the intermediary who knows how to talk to the kitchen.

1.  You look at the **Menu** (the API documentation) to see what you can order.
2.  You give your order (a **Request**) to the waiter in a specific format.
3.  The waiter takes your request to the kitchen.
4.  The kitchen prepares your order and gives it back to the waiter.
5.  The waiter brings the food (the **Response**) back to you.

In technology, an **API** is a set of rules and definitions that allows different software applications to communicate with each other. One application (the "client") sends a request for data, and another application (the "server") sends back a response.

## Part 2: Key API Concepts

Now, having a small idea about what and API is, let's quickly look at the different types of words we encounter when talking or learning about APIs. When working with web APIs, you'll encounter these terms frequently:

*   **API Endpoint**: This is the specific URL you send your request to. It's like a specific item on the menu. For example, an API might have a `/users` endpoint to get user data or a `/products` endpoint to get product data.

*   **HTTP Methods**: These are the actions you want to perform. They are the verbs of your request. The most common one is:
    *   `GET`: Used to retrieve or "get" data from the server. (This is what we'll be using today).
    *   Other common methods include `POST` (to create new data), `PUT` (to update data), and `DELETE` (to remove data).

*   **Request**: The message your application sends to the server's API endpoint. It includes the method (`GET`), the endpoint URL, and sometimes other information.

*   **Response**: The server's answer to your request. It contains a **status code** (like `200 OK` for success or `404 Not Found` for an error) and the data you asked for.

*   **JSON (JavaScript Object Notation)**: The most common data format for API responses. It's lightweight and easy for both humans and machines to read. It looks very similar to a Python dictionary.

    ```json
    {
      "userId": 1,
      "id": 1,
      "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
      "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    }
    ```

## Part 3: Let's Call Some APIs with Python!

Now for the fun part. What I wanted to learn was not to call the APIs manually to get data. Instead I wanted to learn how to invoke an API programmatically so I can automate workflow, build applications by integrating data from external provider etc. I found a pythong library called `requests`, which allows us to do all of this. Therefore, we will use the `requests` library in Python to make our API calls. It simplifies the process of sending HTTP requests.

### Setup

First, you need to install the `requests` library. Open your terminal or command prompt and run:

```bash
pip install requests
```

Just for fun, I am going to show how to invoke web apis with python using this `requests` library. Now, me walk you through the `api_examples.py` file and run it to see live API calls in action!

```bash
python 00_what_is_an_api/api_examples.py
```

### Our Example APIs

In the Python script, we will call three different free, public APIs:

1.  **JSONPlaceholder**: A fantastic service that provides fake API data for testing. We'll use it to fetch a sample blog post.
    *   **Endpoint**: `https://jsonplaceholder.typicode.com/posts/1`

2.  **Public APIs Project**: A fun, meta-API that lists other public APIs. We'll use it to find APIs related to animals.
    *   **Endpoint**: `https://api.publicapis.org/entries`

3.  **Dog CEO API**: A simple API that provides weather data like temperature and windspeed.
    *   **Endpoint**: `https://api.open-meteo.com/v1/forecast`

## Conclusion

Congratulations! You now know:
*   An API acts as a messenger between applications.
*   We use `GET` requests to ask for data from a specific URL called an **endpoint**.
*   The data is usually returned in **JSON** format.
*   The Python `requests` library makes it easy to work with APIs.

This is the fundamental building block for countless applications, from mobile apps fetching weather data to complex web platforms integrating third-party services.