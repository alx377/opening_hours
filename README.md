## Installation and usage
- Use your preferred way to create python 3.7.2 environment
- For example: `mkvirtualenv opening_hours -p python3.7.2`
- Install requirements `pip install -r requirements.txt`
- Run flask server `flask run`
- Use your preferred way to post opening hours to `localhost:5000`
- For example with curl: `curl -vX POST http://localhost:5000 -d @test_data.json \
--header "Content-Type: application/json"`