char c;
#include <Servo.h>
int pwm=50;
int brakepin = 10;
int pwmpin = 11;
int dirpin = 9;
Servo myservo;


void setup() {
  // put your setup code here, to run once:
pinMode(brakepin,OUTPUT);
pinMode(pwmpin ,OUTPUT);
pinMode(dirpin,OUTPUT);
digitalWrite(brakepin,HIGH);
analogWrite(pwmpin,255);
myservo.attach(6);
Serial.begin(9600);
myservo.write(70);
}

void loop() {
  // put your main code here, to run repeatedly:
if(Serial.available()>0)
{
   c=Serial.read();
  if ((char)c=='a'){
    //forward
    myservo.write(70);
    analogWrite(pwmpin,pwm);
  digitalWrite(brakepin,LOW);
  digitalWrite(dirpin,HIGH);
    
  }
  else if ((char)c=='c'){
    //left
   
    myservo.write(73.5);
   analogWrite(pwmpin,pwm);
  digitalWrite(brakepin,LOW);
  digitalWrite(dirpin,HIGH);

  }
  else if((char)c=='b'){
    //right
myservo.write(66.5);
  
   analogWrite(pwmpin,pwm);
  digitalWrite(brakepin,LOW);
  digitalWrite(dirpin,HIGH);
 
  }
}
}
