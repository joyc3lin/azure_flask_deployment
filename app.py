from flask import Flask, render_template
import pandas as pd
import random
from faker import Faker

faker = Faker()

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('base.html')

@app.route('/about')
def aboutpage():
        return render_template('about.html')

@app.route('/random')
def randomstuff():
    number_var = random.randint(1,10000)
    fake_address = faker.address()
    return render_template('random.html', single_number = number_var, single_address = fake_address)
        
if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )