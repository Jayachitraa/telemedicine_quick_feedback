# Webhookify

## Summary

Webhookify is an app that consists of an admin site where you can create an account and register multiple destinations for the accounts. Every edit of the account will get notified to the destination URL.

## Setup

To run this project on your local machine, follow these steps:

1. Clone the project repository:
    ```
    git clone https://github.com/MadheshKumarVJ/webhookify.git
    ```

2. Move to the project directory:
    ```
    cd webhookify/webby/
    ```

3. Install the requirements:
    ```
    pip install -r requirements.txt
    ```

4. Create a superuser:
    ```
    ./manage.py createsuperuser
    ```
   Provide the required details.

5. Run migrations:
    ```
    ./manage.py migrate
    ```

6. Run the server:
    ```
    ./manage.py runserver 8000
    ```
   If you wish to run the server on a different port, please change the `SITE_URL` in `settings.py` before running the server.

7. Navigate to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and login with superuser credentials.

8. Click on "Account" and then click on "Add account" or use this URL: [http://127.0.0.1:8000/admin/webhookify/account/add/](http://127.0.0.1:8000/admin/webhookify/account/add/) to add account details.

9. Click on "Destination" and then click on "Add destination" or use this URL: [http://127.0.0.1:8000/admin/webhookify/destination/add/](http://127.0.0.1:8000/admin/webhookify/destination/add/) to add destination details. 

   I recommend you to add this URL in destination URL: `https://webhook.site/fa67b624-a277-4077-887c-eba6e1a99c16`.

10. Now, try to edit your account details. You will receive a webhook JSON data to this URL: `https://webhook.site/fa67b624-a277-4077-887c-eba6e1a99c16`.
