OpenGrowBox for anyone !!!

- Base / Heart / Call it how you like 
    - Home Assistant Supervised
        - Installation Link
            - https://github.com/home-assistant/supervised-installer
        - Setup For HA:
            - Install MQTT on it and Start the Server
            - Install the File editor 
            - Install HACS
    - NodeRed
        - SetupLink:
            - https://pimylifeup.com/install-node-red-home-assistant/
    - Grafana
        - Add if you need it 


- Sensors: 
    - OS:
        - Tasmota
    - Types:
        - Temperatur
        - Humidity
        - CO2
        - AirPressure
        - VPD
        


- EC FAN Setup 
https://github.com/0xW3bJun6l3/Ruck_EC_API


- Ventilation Setup With PC Fans: 
- Devices Needed:
    - NodeMCUv3 (ESP 8266)
        - Flash it with the latest Tasmota Version
        - Set the Module Type to Generic 18

    - Base Board for NodeMCU V3
    - Power Based on the NodeMCU BaseBOARD
- Artic P12/P14 PWM FAN
    - PINOUT: 
        - 1: Ground
        - 2: VCC (5- 12V)
        - 3: Signal
        - 4: PWM
    - Connection on ESP:
        - FAN PIN 1 TO Ground PIN ESP
        - FAN PIN 2 TO 5-12v input PIN
        - FAN PIN 3 you can ignore it/or read data from it 
        - FAN PIN 4 set it to some D3/D0/D2 Pin on you ESP
- you can also add some Sensors like: SHT31/DHT11/etc. 
