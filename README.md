## Installation and usage
- Use your preferred way to create python 3.7.2 environment
- For example: `mkvirtualenv opening_hours -p python3.7.2`
- Activate the created virtualenv if it is not yet e.g. `workon opening_hours`
- Install requirements `pip install -r requirements.txt`
- Run flask server `flask run`
- Use your preferred way to post opening hours to `localhost:5000`
- For example with curl: `curl -vX POST http://localhost:5000 -d @test_data.json \
--header "Content-Type: application/json"`


## Thoughts

Made the API using flask for the first time. Was first thinking of creating some input validation, but then decided against it as it felt that it is not within the scope of this task. I must admit that getting flask project up and running was really quickly and there is not any overhead when starting the project.

The data format really depends on what the data is used for.
If the data is only to be presented for the human customers then maybe it should be stored as that human readable string.

But lets say that it is required to programmatically tell at any given time that is one single restaurant open or how many restaurants are open. The format could have information for each hour that the restaurant is open. Although this format then bloats the data structure somewhat.

```json
{
    "monday": {
        "08-09": "open",
        "09-10": "open",
        ...
    },
    "tuesday": {
        ...
    }
}
```

Also using proper timestamps instead of name of the day + UNIX time would make the data more flexible for other usage than just presenting the opening hours.

```json
{
    "2019-01-01T10:00:00.000Z": "open",
    "2019-01-01T14:00:00.000Z": "close",
    "2019-01-01T16:00:00.000Z": "open",
    "2019-01-02T02:00:00.000Z": "close",
    ...
}
```
