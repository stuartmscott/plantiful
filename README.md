# Plantiful

## Species, Plants, Produce, Harvest

## Containers, Locations, Soils, Observations

## Watering, Fertilizing, Mulching, Pruning

## Color Scheme
```
#1E2019 (Eerie Black)
#F1F2EB (Alabastor White)
#255921 (Hunter Green)
#62A87C (Mint Green)
#7E583A (Coyote Brown)
```

## Install

```sh
python3 -m pip install django
python3 manage.py createsuperuser
```

## Run

```sh
python3 manage.py shell
python3 manage.py runserver
sqlite3 db.sqlite3
```

## Migrate

```sh
python3 manage.py makemigrations plantiful
python3 manage.py check
python3 manage.py migrate
```
