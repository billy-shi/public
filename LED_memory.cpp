""" This program is the main source code for LED memory task, which
performs the following tasks on the NUCELO-F746ZG MCU:
- cycling LEDs green-blue-red repeatedly
- color is selected by pressing button
- once 5 LEDs have been selected, cycle the 5 selected colors in order
"""

// to successfully compile, run this program on the MBed platform
//#include "mbed.h"


DigitalOut led1(LED1);
DigitalOut led2(LED2);
DigitalOut led3(LED3);


InterruptIn button(USER_BUTTON);

Timeout button_debounce_timeout;
float debounce_time_interval = 0.3;

// Choose LEDs with one parameter l
int current_on;
void select_led(int l)
{
        if (l==1) {
                led1 = true;
                led2 = false;
                led3 = false;
        }
        else if (l==2) {
                led1 = false;
                led2 = true;
                led3 = false;
        }
        else if (l==3) {
                led1 = false;
                led2 = false;
                led3 = true;
        }
}

void cycle_led(void){
         int t=1;
         while(t<4) {
                select_led(t);
                current_on = t;
                wait(1);
                t=t+1;
        }
}


// Button Response
void onButtonStopDebouncing(void);
int num_press = 1;
int selected_led[5]; // array to store chosen leds
void onButtonPress(void)
{
        num_press += 1;  // records how many times button is pressed
        selected_led[num_press] = current_on;
        button.rise(NULL);
        button_debounce_timeout.attach(onButtonStopDebouncing, debounce_time_interval);
		
}
void onButtonStopDebouncing(void)
{
        button.rise(onButtonPress);
}

// cycle chosen leds
void cycle_chosen(void){
         int t=0;
         while(true) {
                select_led(selected_led[t]);
                wait(0.1);
                t=(t+1)%5;
        }
}

int main()
{
        while(num_press <= 5)
        {
                button.rise(onButtonPress);
                cycle_led();
                wait(0.1);
        }
        if (num_press >= 5)
        {
        		led1 = led2 = led3 = true;
        		wait(0.1);
        		cycle_chosen();
        		// all lights turn on
        		// signal start of replaying selected sequence
        }
}