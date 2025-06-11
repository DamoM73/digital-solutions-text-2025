# Requests

The `requests` library allows Python programs to send HTTP/HTTPS requests easily. It's commonly used for:

- Accessing APIs
- Downloading web content
- Submitting forms programmatically

## GET Request

Use **GET** to **retrieve data** from a server.

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
print(response.json())
```

:::{important} Explanation of GET Code
:class: dropdown
- `requests.get(URL)`: Sends a GET request to the URL.
- `status_code`: Returns the HTTP status code (e.g., 200 means OK, 404 means Not Found).
- `json()`: Converts the response from JSON string to Python dictionary.
:::

:::{seealso} GET Requests Activities
:class: dropdown
**Activity 1: Retrieve User Information**

Write a Python script that:

* Sends a GET request to `https://jsonplaceholder.typicode.com/users`
* Prints the names and email addresses of all users

**Activity 2: Filter Posts by User**

Write a Python script that:

* Sends a GET request to `https://jsonplaceholder.typicode.com/posts` with the query parameter `userId=3`
* Prints the titles of all posts made by user ID 3
:::

---

## POST Request

You usually use **POST** to **send data** to a server (e.g., submit a form).

```python
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
print(response.status_code)
print(response.json())
```

:::{important} Explanation of POST Code
:class: dropdown
- `post()`: Sends a POST request to create a new resource.
- `json=data`: Converts the Python dictionary into a JSON payload.
:::

:::{seealso} POST Requests Activities
:class: dropdown
**Activity 1: Submit a New Post**
Write a Python script that:

* Sends a POST request to `https://jsonplaceholder.typicode.com/posts`
* Includes JSON data with a title, body, and userId
* Prints the response JSON to confirm creation

**Activity 2: Register a New Comment**

Write a script that:

* Sends a POST request to `https://jsonplaceholder.typicode.com/comments`
* Includes a name, email, postId, and body in the JSON payload
* Prints the new comment’s ID from the response
:::

---

## PUT and PATCH Requests

Use **PUT** to replace the **entire record**.

```python
put_data = {
    "id": 1,
    "title": "updated title",
    "body": "updated body",
    "userId": 1
}

response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=put_data)
print(response.json())
```

:::{important} Explanation of PUT Code
:class: dropdown
- `put_data`: This dictionary contains the **complete updated data** for the resource with `ID` `1`.
- `requests.put(...)`: This sends a PUT request to the server to **replace** the existing data at `/posts/1`.
- `json=put_data`: The data is sent in JSON format, which is what most APIs expect.
- `response.json()`: The server replies with the updated record, which we print.
:::

:::{seealso} PUT Requests Activities
:class: dropdown
**Activity 1: Replace a Post**

Write a script that:

* Sends a PUT request to `https://jsonplaceholder.typicode.com/posts/1`
* Replaces the entire post with new `title`, `body`, and `userId`
* Prints the full updated record from the response

**Activity 2: Reset a User Profile**

Write a script that:

* Sends a PUT request to `https://jsonplaceholder.typicode.com/users/5`
* Replaces all user fields (name, username, email, etc.) with new values
* Prints confirmation that the user was updated
:::

Use **PATCH** to update only **specific fields**.

```python
patch_data = {"title": "new title only"}

response = requests.patch("https://jsonplaceholder.typicode.com/posts/1", json=patch_data)
print(response.json())
```

:::{important} Explanation of PATCH Code
:class: dropdown
- `patch_data`: This only includes the field you want to update — in this case, just the `title`.
- `requests.patch(...)`: Sends a PATCH request to modify part of the resource.
- `json=patch_data`: Sends only the data you want to change.
- `response.json()`: The server responds with the updated record.
:::

:::{seealso} PATCH Requst Activities
:class: dropdown
**Activity 1: Update a Post Title**

Write a script that:

* Sends a PATCH request to `https://jsonplaceholder.typicode.com/posts/2`
* Changes only the `title` field
* Prints the updated post

**Activity 2: Update User Email Only**

Write a script that:

* Sends a PATCH request to `https://jsonplaceholder.typicode.com/users/3`
* Changes only the `email` field
* Prints the updated user data
:::

---

## DELETE Request

Sends a **DELETE** request to **remove** a resource. Often used in admin interfaces or APIs with write access.

```python
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
```

:::{important} Explanation of DELETE Code
:class: dropdown
- `requests.delete(...)`: This sends an HTTP DELETE request to the server at the URL `https://jsonplaceholder.typicode.com/posts/1`.
- The `/posts/1` endpoint refers to a **specific resource**, in this case, the post with ID 1.
- `response.status_code`: This prints the HTTP response code returned by the server.
- `200` or `204` usually means the delete operation was successful:
  - `200 OK`: The server deleted the resource and may have returned a message.
  - `204 No Content`: The resource was deleted, and there's no content in the response.
:::

### When to Use DELETE

You use a `DELETE` request when:

- You want to remove a record from a server or database via an API.
- You're building an admin panel or content management system where users can remove items like posts, users, or files.

### Caution

- `DELETE` is **destructive**: once something is deleted, it usually can't be recovered.
- Some APIs require **authentication** (e.g., an API key or token) to allow delete requests.
- Many servers will respond with a **403 Forbidden** or **401 Unauthorized** error if proper permissions aren't provided.

**Example with Authentication (optional)**

This shows how to send a `DELETE` request with an API token.

```python
headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}
response = requests.delete("https://api.example.com/posts/42", headers=headers)
print(response.status_code)
```

:::{seealso} DELETE Requests Activities
:class: dropdown
**Activity 1: Delete a Post**

Write a script that:

* Sends a DELETE request to `https://jsonplaceholder.typicode.com/posts/10`
* Prints the status code to confirm deletion

**Activity 2: Remove a Comment**

Write a script that:

* Sends a DELETE request to `https://jsonplaceholder.typicode.com/comments/7`
* Checks the status code to ensure the request was successful
:::

---

## Headers and Query Parameters

**Headers** are used for things like tokens, content-type, etc. **Params** are sent as a query string like `?userId=1`

```python
headers = {
    "Authorization": "Bearer abc123"
}
params = {
    "userId": 1
}

response = requests.get("https://jsonplaceholder.typicode.com/posts", headers=headers, params=params)
print(response.url)
print(response.json())
```

:::{seealso} Header and Parameters Activities
:class: dropdown
**Use a Fake Authorization Header**

Write a Python script that:
* Sends a GET request to `https://httpbin.org/headers`
* Adds a custom `Authorization` header:

  ```python
  headers = {"Authorization": "Bearer abc123"}
  ```
* Prints the response JSON to confirm the header was received by the server

**Activity: Filter Posts by User ID**

Write a Python script that:

* Sends a GET request to `https://jsonplaceholder.typicode.com/posts`
* Adds a query parameter:

  ```python
  params = {"userId": 5}
  ```
* Prints the titles of all posts made by user ID 5
:::

---

## Error Handling

```python
try:
    response = requests.get("https://httpbin.org/status/404")
    response.raise_for_status()  # Raises HTTPError if status is 4xx or 5xx
except requests.exceptions.HTTPError as err:
    print("HTTP Error:", err)
except requests.exceptions.RequestException as err:
    print("Request Error:", err)
```

:::{important} Explanation of Error Handling Code
:class: dropdown
- `raise_for_status()` helps catch failed requests.
- `RequestException` catches all other connection issues, like timeouts.
:::

:::{seealso} Error Handling Activity
:class: dropdown
**Handle a 404 Error Gracefully**

Write a Python script that:

* Sends a GET request to `https://jsonplaceholder.typicode.com/posts/9999` (a post that doesn’t exist)
* Uses `try`/`except` with `response.raise_for_status()` to detect and print a user-friendly message like:

  > "Error: The requested post was not found (404)."
:::

---

## Timeouts

```python
try:
    response = requests.get("https://httpbin.org/delay/3", timeout=2)
except requests.exceptions.Timeout:
    print("Request timed out.")
```

:::{important} Explanation of Timeouts Code
:class: dropdown
- `timeout=2`: Waits 2 seconds before giving up.
- Helps avoid hanging programs if a server is slow or down.
:::

:::{seealso} Timeouts Activity
:class: dropdown
**Simulate and Handle a Timeout**

Write a Python script that:

* Sends a GET request to `https://httpbin.org/delay/5`
* Sets a timeout of `2` seconds using the `timeout` argument
* Catches the timeout exception and prints:

  > "Request timed out. Please try again later."
:::

Here are two targeted activities—one for **headers** and one for **query parameters**—to help students learn how to use them effectively in API requests.

---

## 🧾 Header Activity



🔍 **Learning Goal:** Learn how query parameters change the request URL and filter data server-side.

---

Would you like these activities formatted as classroom worksheets or exported into Markdown for a student learning site?
