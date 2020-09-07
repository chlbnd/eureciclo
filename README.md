# Gallon manager – eureciclo

This project means to calculate how to fill a gallon with bottles in a optimal way.

## Running the application

It is a single endpoint API made in Python using Flask framework.
You must clone this repository in your machine and run `api.py` file by entering the directory by your terminal and typing `python api.py`.
It will be available at your local network by the address `localhost:5000`.

## Filling gallons

This feature is available through the POST endpoint `gallons/fill`.

### Requests and responses

Numbers in arrays represents the volume of your containers in liters.

#### Request 1
```json
{
    "gallons": [7],
    "bottles": [1, 3, 4.5, 1.5, 3.5]
}
```
#### Response 1
`Um galão com a capacidade de 7 L foi preenchido pelas garrafas de [1, 1.5, 4.5] L.`

---

#### Request 2
```json
{
    "gallons": [5],
    "bottles": [1, 3, 4.5, 1.5]
}
```
#### Response 2
`Um galão com a capacidade de 5 L foi preenchido pelas garrafas de (1, 4.5) L com uma sobra de 0.5 L.`

---

#### Request 3
```json
{
    "gallons": [4.9],
    "bottles": [2, 4.5, 0.4]
}
```
#### Response 3
`Um galão com a capacidade de 4.9 L foi preenchido pelas garrafas de [0.4, 4.5] L.`

---

#### Request 4
```json
{
    "gallons": [5, 6.5],
    "bottles": [2, 4.5, 0.4, 5.5]
}
```
#### Response 4
`Galões com a capacidade de [5, 6.5] L foram preenchidos pelas garrafas de (2, 4.5, 5.5) L com uma sobra de 0.5 L.`