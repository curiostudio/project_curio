#include <Stepper.h>
//#include <Keyboard.h>

// steps value is 360 / degree angle of motor
#define STEPS 200

// create a stepper object on pins 4, 5, 6 and 7
Stepper stepper1(STEPS, 17, 15, 16, 14);
Stepper stepper2(STEPS, 18, 20, 19, 21);
Stepper stepper3(STEPS, 7, 5, 6, 4);
Stepper stepper4(STEPS, 11, 9, 10, 8);
Stepper stepper5(STEPS, 0, 2, 1, 3);

//initialise button - pins configuration
int button1 = 11;
int button2 = 12;
int button3 = 13;
int button4 = 14;
int button5 = 15;

int VRx = A1;
int VRy = A2;

int xPosition = 0;
int yPosition = 0;
int mapX = 0;
int mapY = 0;

//variables to denote live page number tracking 
int pg = 1;


void  StepperReset()
{
  int i;
  int reset=0;
  
   Serial.println("Resetting to 0");
   stepper1.setSpeed(120);
   stepper1.step(-1200);
    
   stepper2.setSpeed(120);
   stepper2.step(-1200);
    
   stepper3.setSpeed(120);
   stepper3.step(-1200);
    
   stepper4.setSpeed(120);
   stepper4.step(-1200);
    
   stepper5.setSpeed(120);
   stepper5.step(-1200);
   delay (1000);
   }
    
int StepperPg1()
{
   Serial.println("Page 1");
   stepper1.setSpeed(120);
   stepper1.step(-240);
    
   stepper2.setSpeed(120);
   stepper2.step(640);
    
   stepper3.setSpeed(120);
   stepper3.step(600);
    
   stepper4.setSpeed(120);
   stepper4.step(640);
    
   stepper5.setSpeed(120);
   stepper5.step(420);

   return 1;
   delay (1000);
 }

  
 int StepperPg2()
 {
   Serial.println("Page 2");
   stepper1.setSpeed(120);
   stepper1.step(640);
    
   stepper2.setSpeed(120);
   stepper2.step(800);
    
   stepper3.setSpeed(120);
   stepper3.step(640);
    
   stepper4.setSpeed(120);
   stepper4.step(-400);
    
   stepper5.setSpeed(120);
   stepper5.step(640);
   return 2;
   delay (1000);
  }

void setup()
{
  Serial.begin(9600); 
  //Keyboard.begin();
  pinMode(VRx, INPUT);
  pinMode(VRy, INPUT);
  StepperReset();
}

void loop()

{

  xPosition = analogRead(VRx);
  yPosition = analogRead(VRy);
  mapX = map(xPosition, 0, 1023, -512, 512);
  mapY = map(yPosition, 0, 1023, -512, 512);
  
 
  
  if (mapY < -200) 
  {
  //Call for StepperPg1 function
  StepperReset();
  pg = StepperPg1();
  }
  else if (mapY > 200)
  {
  //Call for StepperPg2 function
  StepperReset();
  pg = StepperPg2();
  }
    
  //Send ASCII code to RPi to read words along X axis
  //else if (mapX > 200)
  {
    //Keyboard.write(215);
    //delay(100);
  }
  
  //Send ASCII code to RPi to read words along -X axis
  //else if (mapX > -200)
  {
    //Keyboard.write(216);
    //delay(100);
  }


   

//Send ascii code to Rpi to select particular line number
  //if (button1 == HIGH) 
  {
    //if(pg==1)
    {
      //Keyboard.write(1);
    }
    //else if (pg==2)
    {
      //Keyboard.write(6);
    } 
  }
   //if (button2 == HIGH) 
  {
    //if(pg==1)
    {
      //Keyboard.write(2);
    }
    //else if (pg==2)
    {
      //Keyboard.write(7);
    } 
  }
   //if (button3 == HIGH) 
  {
    //if(pg==1)
    {
      //Keyboard.write(3);
    }
    //else if (pg==2)
    {
      //Keyboard.write(8);
    } 
  }
   //if (button4 == HIGH) 
  {
    //if(pg==1)
    {
      //Keyboard.write(4);
    }
    //else if (pg==2)
    {
      //Keyboard.write(9);
    } 
  }
   //if (button5 == HIGH) 
  {
    //if(pg==1)
    {
      //Keyboard.write(5);
    }
    //else if (pg==2)
    {
      //Keyboard.write(10);
    } 
  }
  //Keyboard.releaseAll();
  delay(1000);
}
  
