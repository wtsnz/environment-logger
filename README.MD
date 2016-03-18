# environment-logger

This is a script to be run on a RaspberryPi that reads the temperature, pressure
and humidity from a BME280 and sends the result to a statsd server.

It is based on https://github.com/adafruit/Adafruit_Python_BME280 and uses the
`Adafruit_BME280.py` lib to read the sensors data. (Make sure you install that
projects dependencies!)

This project requires python 2.7.

## Installation

Clone the repository and run the main.py

    git clone https://github.com/wtsnz/environment-logger.git
    cd environment-logger
    chmod +x main.py

## Usage

    $ ./main.py --statsd-server server.com --statsd-port 1234
    Timestamp = 119445.000
    Temp      = 23.329 deg C
    Pressure  = 1023.85 hPa
    Humidity  = 59.49 %
    done
    $

Now I collect the stats every 10 seconds by running the command above in a simple while loop. I can't think of a better way to do this as crontab only goes down to a minute. (If you have a better idea please open an issue!)

    while true ; do ./main.py --statsd-server server.com --statsd-port 1234; sleep 10; done
