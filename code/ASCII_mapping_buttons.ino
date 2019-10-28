// Declare the pins for the Button and the LED<br>int buttonPin = 12;
#include <Keyboard.h>

int LED = 13;
int button1 = 12;
int button2 = 11;
int button3 = 10;
int button4 = 9;
int button5 = 8;

void setup() {
   // Define pin #12 as input and activate the internal pull-up resistor
   Serial.begin(9600);
   pinMode(button1, INPUT_PULLUP);
   pinMode(button2, INPUT_PULLUP);
   pinMode(button3, INPUT_PULLUP);
   pinMode(button4, INPUT_PULLUP);
   pinMode(button5, INPUT_PULLUP);
   
   Keyboard.begin();
   
   // Define pin #13 as output, for the LED
}

void loop(){
   // Read the value of the input. It can either be 1 or 0
   int buttonValue1 = digitalRead(button1);
   int buttonValue2 = digitalRead(button2);
   int buttonValue3 = digitalRead(button3);
   int buttonValue4 = digitalRead(button4);
   int buttonValue5 = digitalRead(button5);
   
   //For multiple key presses use Keyboard.press()
   
   if (buttonValue1 == LOW){
      // If button pushed, turn LED on
      //Serial.println("Button 1 is pressed");
      
      //M-g
      Keyboard.press(130);
      Keyboard.press(103);
      //delay(50);
      Keyboard.press(103);
      Keyboard.releaseAll();
       delay(50);
      
      //M-g
      Keyboard.press(130);
      Keyboard.press(103);
      //delay(50);
      Keyboard.press(103);
      Keyboard.releaseAll();
       delay(1000);
       
      //line number
      Keyboard.write(49);
      Keyboard.release(49);
      delay(200);
      
      //Return
      Keyboard.write(176);
      Keyboard.releaseAll();
      
      
   } 
   
   if (buttonValue2 == LOW){
      // If button pushed, turn LED on
      //Serial.println("Button 1 is pressed");
      
      //M-g
      Keyboard.press(130);
      Keyboard.press(103);
      //delay(50);
      Keyboard.press(103);
      Keyboard.releaseAll();
       delay(50);
      
      //M-g
      Keyboard.press(130);
      Keyboard.press(103);
      //delay(50);
      Keyboard.press(103);
      Keyboard.releaseAll();
       delay(1000);
       
      //line number
      Keyboard.write(50);
      Keyboard.release(50);
      delay(200);
      
      //Return
      Keyboard.write(176);
      Keyboard.releaseAll();
      
   } 

   else if (buttonValue3 == LOW){
 
      //M-g
      Keyboard.press(130);
      Keyboard.press(103);
      //delay(50);
      Keyboard.press(103);
      Keyboard.releaseAll();
       delay(50);
      
      //M-g
      Keyboard.press(130);
      Keyboard.press(103);
      //delay(50);
      Keyboard.press(103);
      Keyboard.releaseAll();
       delay(1000);
       
      //line number
      Keyboard.write(51);
      Keyboard.release(51);
      delay(200);
      
      //Return
      Keyboard.write(176);
      Keyboard.releaseAll();
      
   }
   
   else if (buttonValue4 == LOW){
      //Serial.println("Button 4 is pressed");
      
      //M-g
      Keyboard.press(130);
      Keyboard.press(103);
      //delay(50);
      Keyboard.press(103);
      Keyboard.releaseAll();
       delay(50);
      
      //M-g
      Keyboard.press(130);
      Keyboard.press(103);
      //delay(50);
      Keyboard.press(103);
      Keyboard.releaseAll();
       delay(1000);
       
      //line number
      Keyboard.write(52);
      Keyboard.release(52);
      delay(200);
      
      //Return
      Keyboard.write(176);
      Keyboard.releaseAll();
   }
   
   else if (buttonValue5 == LOW){
      //Serial.println("Button 5 is pressed");
      //Keyboard.write(69);
      
      
      //M-g
      Keyboard.press(130);
      Keyboard.press(103);
      //delay(50);
      Keyboard.press(103);
      Keyboard.releaseAll();
       delay(50);
      
      //M-g
      Keyboard.press(130);
      Keyboard.press(103);
      //delay(50);
      Keyboard.press(103);
      Keyboard.releaseAll();
       delay(1000);
       
      //line number
      Keyboard.write(53);
      Keyboard.release(53);
      delay(200);
      
      //Return
      Keyboard.write(176);
      Keyboard.releaseAll(); 
   }
 
}
