# Pokemon

<div>
<details open>
<summary>Python</summary>
Python 3.12 is used in developing the project.<br>
Virtual environment recommended.
</div>


<div>
<details open>
<summary>Usage</summary>
Clone the repository and change directory in `Pokemon`.<br>
Activate virtual Environment if virtual environment. <br>

### Install dependencies from [requirements.txt](https://github.com/mausam1112/Pokemon/blob/master/requirements.txt)  file.
```bash
    pip install -r requirements.txt
```

### Create Postgres Database named `pokemon_info`<br>

### DB migrations
Edit the database information in [.env](https://github.com/mausam1112/Pokemon/blob/master/app/config/.env) file.<br>
```bash
    alembic upgrade head --sql
    alembic upgrade head
```

### Run FastAPI application
##### Windows
```bash
    python main.py
```

##### Linux and MacOS
```bash
    python3 main.py
```
</div>


<div>
<details open>
<summary>API testing</summary>
Postman and Swagger API can be used. To open swagger API, open browser and enter following address. <br>

http://localhost:8000/docs <br>
OR http://youripaddress:8000/docs

##### OR [Click here](http://localhost:8000/docs)
</div>

