# Final Project
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
  * firstName
  * lastName
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
##Login
* **URL**
  * ``/api/Login``
* **Method**
  * ``POST``
* **Data Params**
  * username
  * password
* **URL Params**
  * None
  ```json
  {
      "message": "Congrualuation, You successfully logged in!",
  }
  ```
* **Error Message**
  **Status: 400**
  ```json
  {
      "error": "username or password are not unique."
  }
  ```
##Dashboard
* **URL**
  * ``/api/fishing-spots``
* **Method**
  * ``GET``
* **Goal**
  * ``Show good fishing spot locations and weather``
* **Data Params**
  * Name
  * Country
  * Province
  * City
  * Address
  * Type of Fish Found
  * Kind of fishing gear to bring
* **URL Params**
  * None
  ```json
  {
      "message": "The best place to fish we recommended is ",
  }
  ```
* **Error Message**
  **Status: 400**
  ```json
  {
      "error": "Sorry, there is something wrong, please try again"
  }
  ```
  * **URL**
    * ``/api/fishing-spots``
  * **Method**
    * ``GET``
  * **Goal**
    * ``To be a list of all the fishing spots``
  * **Data Params**
    * Name
    * Country
    * Province
    * City
    * Address
    * Type of Fish Found
    * Kind of fishing gear to bring
  * **URL Params**
    * None
    ```json
    {
        "message": "This is the list of fishing spots",
    }
    ```
  * **Error Message**
    **Status: 400**
    ```json
    {
        "error": "Sorry,we can not found what you are looking for, please try again."
    }
    ```
##Fisherman make comments on fishing spot
    * **URL**
    * ``/api/fishing-spot/<id>/comments``
    * **Method**
      * ``GET``
    * **Goal**
      * ``Returns all the comments for this fishing spot``
    * **Data Params**
      * Name
      * Location
      * Time

    * **URL Params**
      * None
      * **URL**
        * ``/api/fishing-spot/<id>/comments``
      * **Method**
        * ``POST``
      * **Goal**
        * ``Creates a new comment for this fishing spot``
      * **Data Params**
        * Name
        * Location
        * Time

      * **URL Params**
        * None
