# API Documentation
## Fishingapp  Note(s)
1. This documentation uses the [``httpie``](https://httpie.org/) application for making API calls.
2. Please note, we are using ``Djano REST Framework`` to power our API web-service.
## Register
* **URL**
  * ``/api/register``
* **Method**
  * ``POST``
* **Data Params**
  * username
  * email
  * password
* **URL Params**
  * None
* **Success Message**
  **Status: 200**
  ```json
  {
      "message": "You have been registered!",
  }
  ```
* **Error Message**
  **Status: 400**
  ```json
  {
      "error": "Email is not unique."
  }
  ```
  **Status: 400**
  ```json
  {
      "error": "The password is not secure."
  }
  ```
* **Sample Call**
  ```bash
  http --form http://127.0.0.1:8000/api/register \
  username="819270478" \
  email="819270478@qq.com" \
  password="Jimmyjtc0001"
  ```
* **Sample Javascript**
  ```javascript
  function onRegisterClick() {
      const firstNameObject = document.getElementById("first_name")
      const firstName = firstNameObject.value;
      const lastName = document.getElementById("last_name").value;
      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;
      const username = document.getElementById("username").value;
      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
          if (this.readyState == 4 && this.status == 400) {
              alert("Something bad happend when you tried registering");
          } else if (this.readyState == 4 && this.status == 201) { // Thisis the callback function
              window.location.href = "{% url 'register_success_page' %}";
          }
      }
      xhttp.open("POST", "{{ BACKEND_API_SERVER_ADDRESS }}/api/register", true);
      xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
      xhttp.send("first_name="+firstName+"&last_name="+lastName+"&email="+email+"&username="+username+"&password="+password);
  }
  ```
* **Sample Python**
  ```python
  """
  Install requests library by running the following:
  pip install requests
  """
  import requests
  url = 'https://127.0.0.1:8000/api/register'
  myobj = {
      'username': 'bmika',
      'email': 'b@b.com',
      'password': '123'
  }
  x = requests.post(url, data = myobj)
  print(x.text)
  ``` (
