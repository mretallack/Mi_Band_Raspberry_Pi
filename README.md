# MiBand Raspberry Pi Unofficial SDK

Library to work with Xiaomi MiBand (Tested on MiBand3, Might work on 2) [Read the Article here](https://medium.com/@a.nikishaev/how-i-hacked-xiaomi-miband-2-to-control-it-from-linux-a5bd2f36d3ad)

# Contributors & Info Sources

1) Base lib provided by [Leo Soares](https://github.com/leojrfs/miband2)
2) Additional debug & fixes was made by [Volodymyr Shymanskyy](https://github.com/vshymanskyy/miband2-python-test)
3) Some info that really helped, found at [Freeyourgadget team](https://github.com/Freeyourgadget/Gadgetbridge/tree/master/app/src/main/java/nodomain/freeyourgadget/gadgetbridge/service/devices/miband2)
4) I forked the repository from [yogeshojha](https://github.com/yogeshojha) not sure if he edited the original code or it works for MiBand3 out of the box. the original code belongs to [Andrey Nikishaev](https://github.com/creotiv)
5) Tested on Raspberry Pi 3B+ and Raspberry Pi Zero W with official Raspbian image.

### System requirements

Install the following python and bluetooth related libs

    $ sudo apt-get install python-pip python3-pip libglib2.0-dev python-dev python3-dev

### Install dependencies

`pip install -r requirements.txt` from within the folder.

Make sure to Unpair you MiBand from current mobile apps and accounts you have.

Find out your MiBand MAC address using the following command

`sudo hcitool lescan`

set the MAC Address that you've found inside the `main.py` script.

If it's your first time running the code, set the `INIT` flag inside `main.py` as `True`, later change it to `False`
Execute the script:

`python main.py`

If you having problems (BLE can glitch sometimes)
`sudo hciconfig hci0 reset`

# Donate
This library and code wouldn't be possible without [Andrey Nikishaev](https://github.com/creotiv)
If you like it and you find it useful, you can consider donating him pepsi-money by paypal: https://www.paypal.me/creotiv
