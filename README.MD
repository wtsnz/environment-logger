# environment-logger

This is a script to be run on a RaspberryPi that reads the temperature, pressure
and humidity from a BME280 and sends the result to a statsd server.

It is based on https://github.com/adafruit/Adafruit_Python_BME280 and uses the
`Adafruit_BME280.py` lib to read the sensors data. (Make sure you install that
projects dependencies!)

This project requires python 2.7.

## Installation

This will clone the repository, install the init.d service script and register
to start the script on startup.

    cd ~
    git clone https://github.com/wtsnz/environment-logger.git
    cd environment-logger
    chmod +x main.py

Now to install the service modify the `environment-logger.sh` on lines 18 & 19
to ensure that they match your configuration and then run the following:

    sudo cp ./environment-logger.sh /etc/init.d/environment-logger
    sudo chmod +x /etc/init.d/environment-logger
    sudo update-rc.d environment-logger defaults

## Usage

If you'd like to manually run the script use the two arguments below to configure it.

    $ ./main.py --statsd-server server.com --statsd-port 1234

## Service

I've figured out how to get the script to run at startup as a daemon. You can
control the daemon like so

Start the service

    sudo service environment-logger start

Stop the service

    sudo service environment-logger stop

Restart the service

    sudo service environment-logger restart

Enable the script to start on system startup

    sudo update-rc.d environment-logger defaults

Disable the script to start on system startup

    sudo update-rc.d environment-logger remove


## Uninstall

    sudo update-rc.d environment-logger remove
    sudo rm /etc/init.d/environment-logger
    sudo rm -rf ~/environment-logger
