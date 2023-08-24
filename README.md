# FWScience Code Challenge

In order to run the project, you first need to create a virtual environment and install the requirements. You can do it with the following commands:

```bash
python -m venv challenge_env
source challenge_env/bin/activate
pip install -r requirements.txt or requirements-dev.txt (in case you want to have the black and/or pre-commit package in your environment)
```

### Challenge Steps
#### 1-2. Read the data from this endpoint (`swapi-graphql.netlify.app/.netlify/functions/index?query=query Query {allPlanets{planets{name population terrains climates}}}`) and store the data from the endpoint into the database with the appropriate models.

For the challenge purposes I'm using a `sqlite3` database.

First, you need to run the migrations, so in the root of the project run the following command.

```bash
python fwscience_code_challenge/manage.py migrate
```

Next step is to get the data from the given endpoint and store it into the database. For doing that run the following command:

```bash
python fwscience_code_challenge/manage.py get_planets_data
```
After running the command above, you can go to the database and check the data.


#### 3. Write RESTful Create, Read, Update, and Delete endpoints to interact with the database.

To run the app, execute the following command:

```bash
python fwscience_code_challenge/manage.py runserver <port_number>
```

The api allows the following operations:

#### List
- Method : GET
- Endpoint Example: http://127.0.0.1:8000/api/planets/
- Response Example:
```javascript
[
    {
        "id": 1,
        "name": "Tatooine",
        "population": 200000,
        "terrains": [
            "desert"
        ],
        "climates": [
            "arid"
        ]
    },
    {
        "id": 2,
        "name": "Alderaan",
        "population": 2000000000,
        "terrains": [
            "grasslands",
            "mountains"
        ],
        "climates": [
            "temperate"
        ]
    }
]
```

#### Create
- Method : POST
- Endpoint Example: http://127.0.0.1:8000/api/planets/
- Request Body Example:
```javascript
{
    "name": "RobertoPlante",
    "population": 1,
    "terrains": [
        "grasslands"
    ],
    "climates": [
        "awesome"
    ]
}
```
- Response Example:
```javascript
{
    "id": 61,
    "name": "RobertoPlante",
    "population": 1,
    "terrains": [
        "grasslands"
    ],
    "climates": [
        "awesome"
    ]
}
```

#### Update
- Method : PUT
- Endpoint Example: http://127.0.0.1:8000/api/planets/<planet_id>/ -> http://127.0.0.1:8000/api/planets/61/
- Request Body Example:
```javascript
{
    "name": "RobertoPlanet",
    "population": 10,
    "terrains": [],
    "climates": [
        "awesome"
    ]
}
```
- Response Example:
```javascript
{
    "id": 61,
    "name": "RobertoPlanet",
    "population": 10,
    "terrains": null,
    "climates": [
        "awesome"
    ]
}
```

#### Retrieve
- Method : GET
- Endpoint Example: http://127.0.0.1:8000/api/planets/<planet_id>/ -> http://127.0.0.1:8000/api/planets/61/
- Response Example:
```javascript
{
    "id": 61,
    "name": "RobertoPlanet",
    "population": 10,
    "terrains": null,
    "climates": [
        "awesome"
    ]
}
```

#### Delete
- Method : DELETE
- Endpoint Example: http://127.0.0.1:8000/api/planets/<planet_id>/ -> http://127.0.0.1:8000/api/planets/61/
- Response Example:
```javascript
No content
```
