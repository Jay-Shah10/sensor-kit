from flask import Flask
import logging
import dht11_test
import waterlevel

app = Flask(__name__)

@app.route("/")
def main():

    # calling temperature and humidity script.
    dht11_test.main()

    # calling water level.
    adc_value = waterlevel.main()




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)



