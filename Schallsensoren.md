# Soundsensor

## *Bosch Ultrasonic sensor type 3.1*

> <img src ="https://m.media-amazon.com/images/I/61ZFvIoZSLL._AC_SS450_.jpg">

>*Distance measurement up to 1.5m with pulse-echo operation*



Ultrasonic senso detection range:

* Horizontal aprox. 60
* Verical aprox.30°

Time-analog, digital bidirectional data transfer.


##  Design and function.
It operates  on the pulse-echo principle. The acoustic converter element transmits during excitation by a controlpulse (normally between 300ms max. 800ms) and can detect objects after decay time up to 900ms, during whichoecho signals canbe received.
The sensor has 3 connections: positive, ground and signal connection).
The signal connection is used bi-directionally and is designed as an open collector connection with high open-circuit potencial. The sensor has priority over the control unit and switches the signalconnection to Low (<0.5V) if an echo signal is detected. The send signal cannot be processed if there is an echo signalon the line. Ifa threshold value of 1.5V on the signal line is not reached by the control unit, the sensor is induced to send.

## 1. Basic Function.
Short ultrsonic pulses are emitted reflected by surrounding objects, and received by the sensor. The sensor transmits the information ofthe elapsed time $T_L$ between emission of the ultrasonic pulse and receiving the first incoming echo to the microcontrller which calculates the distance with the formula:

>$A=(c*T_L) / 2$
>
>>$A$ s the distance between the sensor and the reflecting object.
>>
>>$c$ is the velocity of sound in air.
>>
>>$T_L$ is the running time of the pulse.

The velocity of sound $c$ is temperature dependentaccording to:

>$c = (331.2 + 0.6*T/°C)(m/sec)$
>
>>$T$ is the temperature of the air in °C.

## 2. Design of the Sonic Transducer.
### 2.1 Resonator.



 