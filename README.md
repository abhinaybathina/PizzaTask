# PizzaTask

## Cloning the project  
* Run command `git clone https://github.com/abhinaybathina/PizzaTask.git` and change into the project folder
* Create a virtual environment `venv` in the repository (use virtualenv, etc)
* Install the requirements
* Activate virtual environment

To create virtual environment and install requirements run following commands
```shell script
virtualenv venv
pip install -r requirements.txt
```

To activate the environment use following commands:
Window: 
```shell script
.\venv\Scripts\activate
```
Ubuntu/Linux
```shell script
source venv/bin/activate
```

To run server use following command:
```shell script
python manage.py runserver
```

## REST API DOCUMENTATION

Documentation of our API endpoints starts here

## Get the list of Pizzas

### Request

`GET /api/list-pizza HTTP/1.1
Host: 127.0.0.1`

### Response

`[{
    "id": 1,
    "pizza_type": "Regular",
    "pizza_size": "Small",
    "toppings": "Onions"
}, {
    "id": 2,
    "pizza_type": "Square",
    "pizza_size": "Medium",
    "toppings": "Cheese"
}]`

## Get the list of pizzas filtered based on size and type of pizza

### Request

`GET /api/list-pizza?type=Regular&size=Small HTTP/1.1
Host: 127.0.0.1`

### Response

`[{
    "id": 1,
    "pizza_type": "Regular",
    "pizza_size": "Small",
    "toppings": "Onions"
}]`

## Create a new pizza

### Request

`POST /api/create-pizza HTTP/1.1
Host: 127.0.0.1
Content-Type: application/json
Content-Length: 67

{"pizza_type":"Square","pizza_size":"Large", "toppings":"Capsicum"}`

### Response

`{
    "id": 6,
    "pizza_type": "Square",
    "pizza_size": "Large",
    "toppings": "Capsicum"
}`

## Edit a pizza

### Request

`PUT /api/edit-pizza/6 HTTP/1.1
Host: 127.0.0.1
Content-Type: application/json
Content-Length: 65

{"pizza_type":"Square","pizza_size":"Large", "toppings":"Cheese"}`

### Response

`{
    "id": 6,
    "pizza_type": "Square",
    "pizza_size": "Large",
    "toppings": "Cheese"
}`

## Delete a pizza

### Request

`DELETE /api/edit-pizza/6 HTTP/1.1
Host: 127.0.0.1`

### Response

`{
    "message": "Pizza deleted successfully"
}`
