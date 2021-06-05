# Your Code

### Setting-up the project

  * Clone the repository to your local machine :
        `$ git clone https://github.com/jayasri2000/yourCode/tree/master`
  * Change directory to yourCode 
        `$ cd yourCode`
  * Install venv 
        `$ pip install pipenv`
  * Create a virtual environment and activate it
        `$ pipenv shell`  
  * Install the requirements: 
        `$ pipenv install`
  * Create a new file in the root directory of the repository (`yourCode`) with name `.env` (only `.env` and not `.env.txt`) and add the following content in it:
    ```
    DEBUG=True
    SECRET_KEY=django-insecure-gv6ebj%hw3xr+%q&o-k4oqfpi-gi(pr7gl^g73elo)tl6*!upb
    ``` 
    
    
    **Note** : You can find few Pipenv related commands [here](https://srty.me/pipenv).
    <br>

  * Make migrations 
        `$ python manage.py makemigrations`
  * Migrate the changes to the database 
        `$ python manage.py migrate`
  * Create admin 
        `$ python manage.py createsuperuser`
  * Run the server 
        `$ python manage.py runserver`
  
