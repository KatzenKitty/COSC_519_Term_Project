## Harry Potter Interactive Photo Frame
This project uses a raspberry pi to simulate a "magic" photograph similar to those described in the Harry Potter literary universe. In Harry Potter, the photographs and portaits of people act essentially as mini instances of that person, able to interact with the outside world and even talk. For example, Harry looks at a photo of his parents when he is upset and they look sympathetic, wave, and blow him kisses to try and comfort him. We wanted to simulate this using the Raspberry Pi Zero, an HDMI display, gesture-sensing technology, and a normal photo frame. This readme describes our process and solutions to challenges we faced.

## Motivation
This is our Term Project for COSC 519: Operating Systems at Towson University. The goal of this assignment was to create something that would demonstrate the knowledge we have gained this semester about operating systems. An example of the topics we used in creating this project are as follows:
1. Process/Thread synchronization
2. Linux terminal
3. Shell scripting
4. Compiling from source
5. I/O devices
6. Buses

## Challenges we faced:
We soldered the header into the pi and the mini-header into the skywriter. As you can see, we soldered the mini-header into the skywriter upsidedown. This could have been avoided if there had been more documentation available about the skywriter or if we had known more about electronics engineering to realize that it would still work no matter which way it was soldered.

![In Progress 1](https://github.com/KatzenKitty/COSC_519_Term_Project/blob/master/InProgress.jpg)
![In Progress 2](https://github.com/KatzenKitty/COSC_519_Term_Project/blob/master/InProgress2.jpg)

Our skywriter stopped working at one point, only recognizing touches. The pimoroni team was very helpful!
https://forums.pimoroni.com/t/skywriter-xl-only-recognizes-touch-gestures/7724/2

Sierra, our wonderful doggie model! She was not always able to perform the tricks we needed:

![Our Model](https://github.com/KatzenKitty/COSC_519_Term_Project/blob/master/Gifs/8bad_fetch.gif)

One of the biggest challenges was getting the PyQt make file to compile. In total, it took about 10 hours due to the limited processing power of the Raspberry Pi zero.

## Completed project
Our complete setup, prior to attaching the header and skywriter:

![CompleteSetup](https://github.com/KatzenKitty/COSC_519_Term_Project/blob/master/CompleteSetup.jpg)

## Things we used
- [Raspberry Pi Zero W Starter Kit](http://www.microcenter.com/product/488620/Pi_Zero_W_Starter_Kit) $39.99
  - RP0W
  - Pibow case
  - Micro SD card (preloaded with Raspbian OS)
  - Blinkt! LED strip (we did not end up using this)
  - Male 2x20 pin header
  - USB A to micro-B cable
  - USB adaptor
  - HDMI adaptor
  - Kit Box
  - Product Manual
  - Stickers
- [Skywriter XL Gesture-Sensing Breakout Board](https://shop.pimoroni.com/products/skywriter) $22.50
- [HDMI Display](https://shop.pimoroni.com/products/hdmi-8-inch-lcd-screen-kit-800-600) $50.63
- [HDMI 1 ft cable](https://www.amazon.com/gp/product/B00474YRE0/ref=oh_aui_detailpage_o01_s00?ie=UTF8&psc=1) $6.49
- [Powerbank](https://www.bestbuy.com/site/tzumi-pocketjuice-endurance-12000-mah-portable-charger-black/5182800.p?skuId=5182800&cmp=RMX&extStoreId=149&ref=212&loc=1&gclid=EAIaIQobChMIo9_NqJKS2wIVywOGCh2EVgIMEAQYASABEgImm_D_BwE&gclsrc=aw.ds) $39.99
- Android phone charger (already owned) $0.00
- Wooden Photo Frame (we had this already) $0.00
- Packing styrofoam (also had this already) $0.00

## Installation
First things first, we updated and upgraded via the terminal to ensure we had the most up-to-date software loaded onto our pi:

```sudo apt-get update && sudo apt-get upgrade```

Next, we cloned the skywriter github repository:

```git clone https://github.com/pimoroni/skywriter-hat
cd skywriter-hat
sudo python setup.py install
```
    
Then, we installed the python module for the skywriter:

```pip3 install skywriter```
    
The skywriter uses the I2C bus - transactions are performed by passing one or more I2C I/O messages to the transaction method of
the I2CMaster. I2C I/O messages are created with reading, reading_into, writing, and writing_bytes functions defined in the
quick2wire.i2c module. An I2CMaster acts as a context manager, allowing it to be used in a with statement. The I2CMaster's file
descriptor is closed at the end of the with statement and the instance cannot be used for I/O further.

```curl -sSl get.pimoroni.com/i2c | bash```
    
The skywriter also requires smbus:

```sudo apt-get install python-smbus```
    
and required dev libraries:

```sudo apt-get install libx11-dev libxtst-dev```

In order to install autopy, which was required for some of the skywriter test scripts, we needed to install the Rust programming
language:

```
curl https://sh.rustup.rs -sSf | sh -s -- --default.toolchain nightly
source $HOME/.cargo/env #this sets the PATH variable so we can run rust from any directory
```
    
We were unable to install autopy via the pip3 command, so we cloned the github repository and compiled from source:

```get clone https://github.com/autopilot-rs/autopy.git
cd autopy
python3 setup.py build
python3 setup.py install
```
    
We needed to disable the screensaver and autotimeout in the system settings:

```sudo nano /etc/xdg/lxsession/LXDE/autostart
# @xscreensaver -no-splash #commented out the screensaver to disable it, then added these three lines to the end of the file
@xset s off
@xset -dpms
@xset s noblank
```
    
After trying a few different python libraries such as Pyglet and tKinter, we found PyQt would work perfectly for supporting the
gif animations. It is a C/C++ Python cross-platform application development framework. We needed to install SIP before installing
PyQt
⚠️ Important! The installation of PyQt takes a very long time (as in hours) especially if you compile from source.

```wget "https://sourceforge.net/projects/pyqt/files/sip/sip-4-19.8/sip-4.19.8.tar.gz"
tar -xzf sip-4.19.8.tar.gz
cd sip-4.19.8
python3 configure.py
make
sudo make install
wget "https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.10.1/PyQt5_gpl-5.10.1.tar.gz"
tar -xzf PyQt5_gpl-5.10.1.tar.gz
cd PyQt5_gpl-5.10.1
python3 configure.py
make
sudo make install
```

In order to easily transfer the gif animations we would be using to the pi, we shared the dropbox links and used wget to retrieve them:

```cd Project
wget "https://www.dropbox.com/s/[the specific URL tail for the gif].gif"
```

## References
- [https://howtomechatronics.com/tutorials/arduino/how-i2c-communication-works-and-how-to-use-it-with-arduino/]
Dachis, A., n.d. A Beginner’s Guide to DIYing with the Raspberry Pi [WWW Document]. 

- Lifehacker. URL [https://lifehacker.com/5976912/a-beginners-guide-to-diying-with-the-raspberry-pi] (accessed 3.5.18).

- Magic Presentations with Skywriter [WWW Document], 2015. . The MagPi Magazine. URL [https://www.raspberrypi.org/magpi/skywriter/] (accessed 3.5.18).

- [https://www.google.com/url?q=http://pyqt.sourceforge.net/Docs/PyQt4/new_style_signals_slots.html&sa=D&source=hangouts&ust=1526831120266000&usg=AFQjCNHFOnfeON5MYShTeRC3yjTUGBxxKw]

- [https://gist.github.com/altendky] This individual assisted with python syntax and utilizing the PyQt library via the python IRC

- [https://github.com/pimoroni/skywriter-hat/blob/master/datasheets/Datasheet.pdf]

- [https://pinout.xyz/pinout/skywriter_hat#]

- [https://hackernoon.com/compiling-rust-for-the-raspberry-pi-49fdcd7df658]

- [https://doc.rust-lang.org/book/second-edition/ch00-00-introduction.html]
