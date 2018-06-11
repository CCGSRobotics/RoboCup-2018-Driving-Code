#include <SoftwareSerial.h>
SoftwareSerial co2Serial(10, 11); // RX, TX
unsigned char hexdata[9] = {0xFF,0x01,0x86,0x00,0x00,0x00,0x00,0x00,0x79};
char CO2 = true;
char temperature = true;

// This is the functions that reads the pin's values, 
// and outputs the pin number and analog value from the sensor.
void readPin(int pin){
  Serial.print(pin); 
  Serial.println(analogRead(pin));
}

void readCO2() {
    co2Serial.write(hexdata,9);
    for(int i=0;i<9;i++)  {
      if (co2Serial.available()>0) {
        long hi,lo,CO2;
        int ch=co2Serial.read();
    
        if(i==2){
          hi=ch; //High concentration
        }   
        if(i==3){
          lo=ch;   
        }   //Low concentration
        if(i==8) {
          CO2=hi*256+lo;  //CO2 concentration
          Serial.print("0");
          Serial.println(CO2);
        }
      }
    } 
  }
// The setup of the Serial communication, on channel 9600.
void setup(){
  Serial.begin(9600);
  co2Serial.begin(9600);
}
// This is the code that repeats every 0.5 seconds.
void loop(){
  // They will output this signal to the serial communication with the "readPin(x)" function.
  if(temperature == true) {readPin(1);}
  if(CO2 == true) {readCO2();}

  // A delay of 500 milliseconds (0.5 seconds) is used to stop python from reading the values too quickly. 
  // Change to 250 milliseconds if absolutely neccessary.
  delay(500);
}
