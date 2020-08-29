from flask import Flask, render_template
import logging
import dht11_test
import waterlevel

app = Flask(__name__)

@app.route("/")
def main():

    # calling temperature and humidity script.
    result = dht11_test.main()
    temperature = result.temperature
    humidity = result.humidity

    # calling water level.
    adc_value = waterlevel.main()

    return render_template('index.html', temperature=temperature , humidity=humidity , water_level=adc_value)




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)



