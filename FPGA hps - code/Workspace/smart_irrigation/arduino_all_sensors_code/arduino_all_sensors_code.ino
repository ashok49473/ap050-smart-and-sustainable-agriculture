//NPK SENSOR
#include <SoftwareSerial.h>
#include <Wire.h>
#define RE 8
#define DE 7
//const byte code[]= {0x01, 0x03, 0x00, 0x1e, 0x00, 0x03, 0x65, 0xCD};
const byte nitro[] = {0x01,0x03, 0x00, 0x1e, 0x00, 0x01, 0xe4, 0x0c};
const byte phos[] = {0x01,0x03, 0x00, 0x1f, 0x00, 0x01, 0xb5, 0xcc};
const byte pota[] = {0x01,0x03, 0x00, 0x20, 0x00, 0x01, 0x85, 0xc0};
byte values[11];
SoftwareSerial mod(2,3);
//-----------------------------------------------------------------------------------------------------------
//PH sensor
float calibration_value = 21.34-0.7;
int phval = 0; 
unsigned long int avgval; 
int buffer_arr[10],temp;
float ph_act;
//------------------------------------------------------------------------------------------------------------
// soil moisture sensor
const int AirValue = 608;   //fixed value when we place sensor in Air for a while in the position
const int WaterValue = 310;  //""           """                   water      ""          ""
int soilMoistureValue = 0;
int soilmoisturepercent=0;
// ------------------------------------------------------------------------------------------------------------
//water level sensor
int waterlevelvalue=0;
#define sensorPower 12 //        for  powering up when we needed     DIGITAL PIN 12
//-----------------------------------------------------------------------------------------------------
// EC SENSOR
#include <EEPROM.h>
#include "GravityTDS.h"
 
#define TdsSensorPin A2   //         Defining for TDS data pin----->  ANALOG pin A2
GravityTDS gravityTds;
//----------------------------------------------------------------------------
// SOIL temperature SENSOR

#include <OneWire.h>
#include <DallasTemperature.h>
#define ONE_WIRE_BUS 4   //  Soil Temperature sensor Data wire is plugged into digital pin 2 on the Arduino      DIGITAL PIN 4
OneWire oneWire(ONE_WIRE_BUS);    
                                  
DallasTemperature sensors(&oneWire);
//---------------------------------------------------------------------------------

//
float temperature = 0, tdsValue = 0, ec=0;

//==============================================================================================================
void setup()
{
  Serial.begin(9600); // open serial port, set the baud rate to 9600 bps
    //NPK
  mod.begin(9600);
  pinMode(RE, OUTPUT);
  pinMode(DE, OUTPUT);

  pinMode(sensorPower, OUTPUT);
  digitalWrite(sensorPower, LOW);

  gravityTds.setPin(TdsSensorPin);
  gravityTds.setAref(5.0);  //reference voltage on ADC, default 5.0V on Arduino UNO
  gravityTds.setAdcRange(1024);  //1024 for 10bit ADC
  gravityTds.begin();  
  sensors.begin();  
}

//================================================================================================================
void loop() {

    //*Serial.println("---------------------------------------------------------");
     // soil temperature
    sensors.requestTemperatures(); //requests temperature
    //Serial.print("Temperature (in Centigrade): ");
    temperature = sensors.getTempCByIndex(0);
    //////Serial.print("Temperature_(*C)");
    //////Serial.println(temperature);
    //---------------------------------------------------------
    // EC sensor
    gravityTds.setTemperature(temp);  // set the temperature and execute temperature compensation
    gravityTds.update();  //sample and calculate
    tdsValue = gravityTds.getTdsValue();  // then get the value
    ec=tdsValue*2/1000;
    //Serial.print("EC_(milliSiemens/cm) ");
    //Serial.println(ec);
  //PH SENSOR
    for(int i=0;i<10;i++) 
 { 
 buffer_arr[i]=analogRead(A0);           // ph  sensor data to  ANALOG PIN A0
 //delay(30);
 }
  for(int i=0;i<9;i++)
 {
 for(int j=i+1;j<10;j++)
 {
 if(buffer_arr[i]>buffer_arr[j])
 {
 temp=buffer_arr[i];
 buffer_arr[i]=buffer_arr[j];
 buffer_arr[j]=temp;
 }
 }
 }
 avgval=0;
 for(int i=2;i<8;i++)
 avgval+=buffer_arr[i];
 float volt=(float)avgval*5.0/1024/6; 
 ph_act = -5.70 * volt + calibration_value;
 
 //Serial.print("pH_Val ");
 //Serial.println(ph_act);

  //NPK SENSOR
  
  byte val1,val2,val3;
  val1 = nitrogen();
  delay(50);
  val2 = phosphorous();
  delay(50);
  val3 = potassium();
  delay(50);
   
  //Serial.print("Nitrogen_(mg/kg) ");
  //Serial.println(val1);
  //Serial.println(" mg/kg");
  //Serial.print("Phosphorous_(mg/kg) ");
  //Serial.println(val2);
  //Serial.println(" mg/kg");
  //Serial.print("Potassium_(mg/kg) ");
  //Serial.println(val3);
  //Serial.println(" mg/kg");
  //delay(2000);
  //-----------------------------------------------------------
  // water level sensor

  int level = readSensor();
  //Serial.print("Water_level_value ");
  //Serial.println(level);
  // soil moisture sensor
  
  soilMoistureValue = analogRead(A1);  //           Soil MOisture sensor data pin to ANAOG A3
  //Serial.print("Soil_Moisture_value ");
  //Serial.println(soilMoistureValue);
  soilmoisturepercent = map(soilMoistureValue, AirValue, WaterValue, 0, 100);
  if(soilmoisturepercent >= 100)
  {
    //Serial.println("soil moisture percent: 100 %");
  }
  else if(soilmoisturepercent <=0)
  {
    //Serial.println("soil moisture percent: 0 %");
  }
  else if(soilmoisturepercent >0 && soilmoisturepercent < 100)
  {
    //Serial.print("soil moisture percent: ");
    //Serial.print(soilmoisturepercent);
    //Serial.println("%");
  
  }
  //------------------------------------------------------------------------

   Serial.print("Temp:");
   Serial.print(temperature);
   Serial.print("::EC:");
   Serial.print(ec);
   Serial.print("::pH:");
   Serial.print(ph_act);
   Serial.print("::Nitro:");
   Serial.print(val1);
   Serial.print("::Potas:");
   Serial.print(val2);
   Serial.print("::Phosp:");
   Serial.print(val3);
   Serial.print("::level:");
   Serial.print(level);
   Serial.print("::Moist:");
   Serial.println(soilMoistureValue);
   delay(3000);
    //exit(0);
  }
// NPK SENSOR each chemical functions

byte nitrogen(){
  digitalWrite(DE,HIGH);
  digitalWrite(RE,HIGH);
  //delay(10);
  if(mod.write(nitro,sizeof(nitro))==8){
    digitalWrite(DE,LOW);
    digitalWrite(RE,LOW);
    for(byte i=0;i<7;i++){
    values[i] = mod.read();
    }
  }
  return values[4];
}
 
byte phosphorous(){
  digitalWrite(DE,HIGH);
  digitalWrite(RE,HIGH);
  //delay(10);
  if(mod.write(phos,sizeof(phos))==8){
    digitalWrite(DE,LOW);
    digitalWrite(RE,LOW);
    for(byte i=0;i<7;i++){
    values[i] = mod.read();
    }
  }
  return values[4];
}
 
byte potassium(){
  digitalWrite(DE,HIGH);
  digitalWrite(RE,HIGH);
  //delay(10);
  if(mod.write(pota,sizeof(pota))==8){
    digitalWrite(DE,LOW);
    digitalWrite(RE,LOW);
    for(byte i=0;i<7;i++){
    values[i] = mod.read();
    }
  }
  return values[4]; 
}


// WATER LEVEL SENSOR FUNCTION
  
int readSensor()
{
  digitalWrite(sensorPower, HIGH);
  //delay(10);
  waterlevelvalue=analogRead(A1);  // Water Level Sensor data pin to ANALOG A1
  digitalWrite(sensorPower, LOW);
  return waterlevelvalue;
}
