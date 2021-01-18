## Email Sender

Email scheduler app

### Getting started

1. Install Docker and docker-compose
    visit [here](https://docs.docker.com/) to read more about docker installation

    ```shell
    $ docker --version
    Docker version 19.03.3, build a872fc2f86

    $ docker-compose --version
    docker-compose version 1.24.1, build 4667896b
    ```

2. Run docker container

   ```shell
   $ docker-compose -f docker/docker-compose.yml -p up -d
   ```

3. Install dependencies

   ```shell
   pip install -r requirements.txt
   ```

4. Execute migration

   ```
   flask db upgrade head
   ```

5. Run celery worker

   ```
   celery -A app.controllers.emails.celery worker
   ```


### API

##### Send Email
----
  Send email for registered recipients.

* **URL**
  /save-emails
* **Method:**
  `POST`
* **Request:**
    {
        "event_id":6,
        "subject":"Lets see if its work",
        "content":"Hi there, Let's hope its just work as expected..",
        "timestamp":"2021-01-18 14:34:30"
    }

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{
    "id": 57,
    "subject": "Lets see if its work",
    "timestamp": "2021-01-18 14:34:30",
    "event_id": 6,
    "content": "Hi there, Let's hope its just work as expected.."
}`
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{
    "message": "{'timestamp': ['Missing data for required field.']}"
}`

##### Add Recipients
----
  Send email for registered recipients.

* **URL**
  /save-recipients
* **Method:**
  `POST`
* **Request:**
    {
    "name": "Pikachu",
    "email": "pikachu@gmail.com"
    }

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{
    "email": "pikachu@gmail.com",
    "name": "Pikachu",
    "id": 4
}`
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{
    "message": "{'name': ['Missing data for required field.']}"
}`
