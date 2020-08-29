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
    F = (temperature * 9/5) + 32
    humidity = result.humidity

    # calling water level.
    adc_value = waterlevel.main()
    water_level = adc_value/200.*100

    # if adc_value == 0:
    #     print("no water\n")
    # elif adc_value>0 and adc_value<30 :
    #     print("it is raindrop\n")
    # elif adc_value>=30 and adc_value<200 :
    #     print("it is water flow")
    #     print("water level:"+str("%.1f"%(adc_value/200.*100))+"%\n")

    return render_template('index.html', temperature=F , humidity=humidity , water_level=water_level)




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)



