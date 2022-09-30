## Clone the repository
https://github.com/castilloxavie/CRUD

## Create virtual env and activate

create:
  virtualenv name_env 
  
activate:
  On Unix or MacOS, using the bash shell: source venv/bin/activate
  
  On Windows using the Command Prompt: path\venv\Scripts\activate.bat
  
  ## install libraries
  
  pip install -r requirements.txt
  
  ## create migrations
  
  - python manage.py makemigration
- python manage.py migrate

## NOTE 

-the database used in this project is sqlite3

-Ports to use that should not be busy or with local services turned off:

  -Djang:8000
