void setup() {
  // put your setup code here, to run once:
pinMode(10 ,OUTPUT);
pinMode(9 ,OUTPUT);
pinMode(8 ,OUTPUT);
pinMode(7,OUTPUT);
Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
if(Serial.available()>0)
{
  int value=Serial.read();
  if(value==3){
    //forward
    digitalWrite(10,HIGH);
    digitalWrite(9,LOW);
    digitalWrite(8,HIGH);
    digitalWrite(7,LOW);
  }
  else if (value==2){
    //left
     digitalWrite(10,HIGH);
    digitalWrite(9,LOW);
    digitalWrite(8,LOW);
    digitalWrite(7,HIGH);
  }
  else if(value==1){
    //right
     digitalWrite(10,LOW);
    digitalWrite(9,HIGH);
    digitalWrite(8,HIGH);
    digitalWrite(7,LOW);
  }
  else {
    //do nothing
    digitalWrite(10,LOW);
    digitalWrite(9,LOW);
    digitalWrite(8,LOW);
    digitalWrite(7,LOW)
  }
  
}
