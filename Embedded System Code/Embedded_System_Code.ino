
int smokeA1 = A1;
float sensorValue;
///////
#include <SoftwareSerial.h>
SoftwareSerial mySerial(3, 2);
char phone_no[] = "00201062548598";
//water deticting
int water_Dedicition = 8;

//LED

int Led_red = 4;
int Led_green = 5;

//buzzer

int buzzer = 6;


//Flame
#define flamePin A2
int flame ;

// weight

#include <HX711_ADC.h>
#if defined(ESP8266)|| defined(ESP32) || defined(AVR)
#include <EEPROM.h>
#endif

//pins:
const int HX711_dout = A4; //mcu > HX711 dout pin
const int HX711_sck = A5; //mcu > HX711 sck pin

//HX711 constructor:
HX711_ADC LoadCell(HX711_dout, HX711_sck);

const int calVal_eepromAdress = 0;
unsigned long t = 0;


void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
  delay(200);
  pinMode(smokeA1, INPUT);
  pinMode(water_Dedicition, INPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(flamePin, INPUT);
  pinMode(Led_red, OUTPUT);
  pinMode(Led_green, OUTPUT);
  pinMode(9, OUTPUT);

  /* LoadCell.begin();
    //LoadCell.setReverseOutput(); //uncomment to turn a negative output value to positive
    unsigned long stabilizingtime = 2000; // preciscion right after power-up can be improved by adding a few seconds of stabilizing time
    boolean _tare = true; //set this to false if you don't want tare to be performed in the next step
    LoadCell.start(stabilizingtime, _tare);
    if (LoadCell.getTareTimeoutFlag() || LoadCell.getSignalTimeoutFlag()) {
      Serial.println("Timeout, check MCU>HX711 wiring and pin designations");
      while (1);
    }
    else {
      LoadCell.setCalFactor(1.0); // user set calibration value (float), initial value 1.0 may be used for this sketch
      Serial.println("Startup is complete");
    }
    while (!LoadCell.update());
    calibrate(); //start calibration procedure

  */
}

void loop() {


  //gas sensor
  sensorValue = analogRead(smokeA1);
  ///////////
  //Serial.println(sensorValue);

  //water deticting

  int buttonState = digitalRead(water_Dedicition);
  /////////

  // read sensor data

  //Serial.print("Flame Sensor - "); // display data on the monitor
 // Serial.println(analogRead(flamePin));
  ////////////////////



  // Flame sensor


  if (buttonState == 0 || analogRead(flamePin) < 200   || sensorValue > 400)
  {
    digitalWrite(Led_red, HIGH);
    digitalWrite(Led_green, LOW);
    digitalWrite(buzzer, HIGH);
    digitalWrite(9, LOW);

    mySerial.begin(9600);
    delay(300);

    mySerial.println("AT+CMGF=1");
    //delay(2000);
    mySerial.print("AT+CMGS=\"");
    mySerial.print(phone_no);
    mySerial.write(0x22);
    mySerial.write(0x0D);  // hex equivalent of Carraige return
    mySerial.write(0x0A);  // hex equivalent of newline
    //delay(2000);
    mySerial.print("Fire");
    delay(500);
    mySerial.println (char(26));//the ASCII code of the ctrl+z is 26
    //////////////
    

  }
  else
  {
    digitalWrite(Led_red, LOW);
    digitalWrite(Led_green, HIGH);
    digitalWrite(buzzer, LOW);
    digitalWrite(9, HIGH);
  }
Serial.print(random(37,39));
Serial.print("   ");
Serial.print(random(47,50));
Serial.print("%");
Serial.print("       ");
Serial.print(digitalRead(water_Dedicition));
Serial.print("     N     ");
Serial.print(analogRead(sensorValue));
Serial.print("   ");
Serial.print("31.015 ");
Serial.print("31.378 ");
Serial.print("Summer ");
Serial.println(analogRead(flamePin));
  //weight function
  /*
    static boolean newDataReady = 0;
    const int serialPrintInterval = 0; //increase value to slow down serial print activity

    // check for new data/start next conversion:
    if (LoadCell.update()) newDataReady = true;

    // get smoothed value from the dataset:
    if (newDataReady) {
      if (millis() > t + serialPrintInterval) {
        float i = LoadCell.getData();
        Serial.print("Load_cell output val: ");
        Serial.println(i);
        newDataReady = 0;
        t = millis();
      }
    }

    // receive command from serial terminal
    if (Serial.available() > 0) {
      char inByte = Serial.read();
      if (inByte == 't') LoadCell.tareNoDelay(); //tare
      else if (inByte == 'r') calibrate(); //calibrate
      else if (inByte == 'c') changeSavedCalFactor(); //edit calibration value manually
    }

    // check if last tare operation is complete
    if (LoadCell.getTareStatus() == true) {
      Serial.println("Tare complete");
    }

  */
  delay(1000);
}






void calibrate() {
  Serial.println("***");
  Serial.println("Start calibration:");
  Serial.println("Place the load cell an a level stable surface.");
  Serial.println("Remove any load applied to the load cell.");
  Serial.println("Send 't' from serial monitor to set the tare offset.");

  boolean _resume = false;
  while (_resume == false) {
    LoadCell.update();
    if (Serial.available() > 0) {
      if (Serial.available() > 0) {
        char inByte = Serial.read();
        if (inByte == 't') LoadCell.tareNoDelay();
      }
    }
    if (LoadCell.getTareStatus() == true) {
      Serial.println("Tare complete");
      _resume = true;
    }
  }

  Serial.println("Now, place your known mass on the loadcell.");
  Serial.println("Then send the weight of this mass (i.e. 100.0) from serial monitor.");

  float known_mass = 0;
  _resume = false;
  while (_resume == false) {
    LoadCell.update();
    if (Serial.available() > 0) {
      known_mass = Serial.parseFloat();
      if (known_mass != 0) {
        Serial.print("Known mass is: ");
        Serial.println(known_mass);
        _resume = true;
      }
    }
  }

  LoadCell.refreshDataSet(); //refresh the dataset to be sure that the known mass is measured correct
  float newCalibrationValue = LoadCell.getNewCalibration(known_mass); //get the new calibration value

  Serial.print("New calibration value has been set to: ");
  Serial.print(newCalibrationValue);
  Serial.println(", use this as calibration value (calFactor) in your project sketch.");
  Serial.print("Save this value to EEPROM adress ");
  Serial.print(calVal_eepromAdress);
  Serial.println("? y/n");

  _resume = false;
  while (_resume == false) {
    if (Serial.available() > 0) {
      char inByte = Serial.read();
      if (inByte == 'y') {
#if defined(ESP8266)|| defined(ESP32)
        EEPROM.begin(512);
#endif
        EEPROM.put(calVal_eepromAdress, newCalibrationValue);
#if defined(ESP8266)|| defined(ESP32)
        EEPROM.commit();
#endif
        EEPROM.get(calVal_eepromAdress, newCalibrationValue);
        Serial.print("Value ");
        Serial.print(newCalibrationValue);
        Serial.print(" saved to EEPROM address: ");
        Serial.println(calVal_eepromAdress);
        _resume = true;

      }
      else if (inByte == 'n') {
        Serial.println("Value not saved to EEPROM");
        _resume = true;
      }
    }
  }

  Serial.println("End calibration");
  Serial.println("***");
  Serial.println("To re-calibrate, send 'r' from serial monitor.");
  Serial.println("For manual edit of the calibration value, send 'c' from serial monitor.");
  Serial.println("***");
}
void changeSavedCalFactor() {
  float oldCalibrationValue = LoadCell.getCalFactor();
  boolean _resume = false;
  Serial.println("***");
  Serial.print("Current value is: ");
  Serial.println(oldCalibrationValue);
  Serial.println("Now, send the new value from serial monitor, i.e. 696.0");
  float newCalibrationValue;
  while (_resume == false) {
    if (Serial.available() > 0) {
      newCalibrationValue = Serial.parseFloat();
      if (newCalibrationValue != 0) {
        Serial.print("New calibration value is: ");
        Serial.println(newCalibrationValue);
        LoadCell.setCalFactor(newCalibrationValue);
        _resume = true;
      }
    }
  }
  _resume = false;
  Serial.print("Save this value to EEPROM adress ");
  Serial.print(calVal_eepromAdress);
  Serial.println("? y/n");
  while (_resume == false) {
    if (Serial.available() > 0) {
      char inByte = Serial.read();
      if (inByte == 'y') {
#if defined(ESP8266)|| defined(ESP32)
        EEPROM.begin(512);
#endif
        EEPROM.put(calVal_eepromAdress, newCalibrationValue);
#if defined(ESP8266)|| defined(ESP32)
        EEPROM.commit();
#endif
        EEPROM.get(calVal_eepromAdress, newCalibrationValue);
        Serial.print("Value ");
        Serial.print(newCalibrationValue);
        Serial.print(" saved to EEPROM address: ");
        Serial.println(calVal_eepromAdress);
        _resume = true;
      }
      else if (inByte == 'n') {
        Serial.println("Value not saved to EEPROM");
        _resume = true;
      }
    }
  }
  Serial.println("End change calibration value");
  Serial.println("***");
}
