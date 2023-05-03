#include <Arduino.h>
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 2, 16); 

void setup()
{
  lcd.init();                     
  lcd.backlight();
  Serial.begin(9600);
  lcd.print("ready");
}


void loop() {
  if (Serial.available())
  {
    String input = Serial.readStringUntil('\n');
    int inputLength = input.length();
    lcd.clear();
    if (inputLength > 16) 
    {
      lcd.setCursor(0, 0);
      lcd.print(input.substring(0, 16));
      lcd.setCursor(0, 1);
      lcd.print(input.substring(16));
    } 
    else 
    {
      lcd.print(input);
    }
  }
}