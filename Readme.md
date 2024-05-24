### Required Hardware
- **RUCK EC 125L 02** or any other volume type with PWM support
- **Raspberry Pi**

### Connection
1. Connect the cable from pin 1 of the fan to a ground pin (PIN 14) on your Raspberry Pi.
2. Connect the cable from pin 2 of the fan to the PWM GPIO pin 18 (PIN 12) on your Raspberry Pi.

### Setup
1. Clone this repository:
    ```bash
    git clone https://github.com/0xW3bJun6l3/OpenGrowBox.git
    ```
2. Test the setup with:
    ```bash
    python3 API.py
    ```
3. If everything works, modify the service file to your needs and enable it.
4. Add the sensor files to Home Assistant.
5. Enjoy your PWM fan for your grow!
