#include <Servo.h>

#define LEDpin LED_BUILTIN
#define ESCpin_1 3 //PWM

Servo ESC_1;

int v = 0; 
int vr = 0;

void armESC(){
  ESC_1.writeMicroseconds(2000);
  delay(1000);
  ESC_1.writeMicroseconds(1000);
  delay(2000);
}

void setup() {
  Serial.begin(9600);
  Serial.println("Connected Arduino");
  ESC_1.attach(ESCpin_1, 1000, 2000);
  armESC();
  pinMode(LEDpin,OUTPUT);
  digitalWrite(LEDpin,1);
  delay(500);
  digitalWrite(LEDpin,0);
  Serial.println("Ready.");
}

void loop() {
   int data = -1;
   if (Serial.available()){
     data = Serial.read() - '0'; 
   }  
   switch (data){
   case 1:
    if(v < 100){
        v = v + 10;
        delay(10);
        Serial.print(v);
        Serial.println(" %"); 
      }else Serial.println("100 %");
      break;
    case 0://problem
      if(v != 0){
        v = v - 10;
        Serial.print(v);
        Serial.println(" %");
      }else Serial.println("0 %");
      break;
    //default:
    //  Serial.println("Err");
    vr = map(v, 0, 100, 1000, 2000);
    ESC_1.writeMicroseconds(vr);
  }
}
