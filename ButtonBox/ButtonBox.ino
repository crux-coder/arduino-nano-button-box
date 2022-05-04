/* @file HelloKeypad.pde
  || @version 1.0
  || @author Alexander Brevig
  || @contact alexanderbrevig@gmail.com
  ||
  || @description
  || | Demonstrates the simplest use of the matrix Keypad library.
  || #
*/
#include <Keypad.h>

const byte ROWS = 4; // four rows
const byte COLS = 4; // three columns
char keys[ROWS][COLS] = {
  {'A', 'B', 'C', 'D'},
  {'E', 'F', 'G', 'H'},
  {'I', 'J', 'K', 'L'},
  {'M', 'N', 'O', 'P'}
};
byte rowPins[ROWS] = {5, 4, 3, 2}; // connect to the row pinouts of the keypad
byte colPins[COLS] = {9, 8, 7, 6}; // connect to the column pinouts of the keypad

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);
char key = 'N';
char pressed_key = 'L';
void setup()
{
  Serial.begin(9600);
}

void loop()
{
  KeyState state = keypad.getState();
  key = keypad.getKey();
  if(key!= NO_KEY) {
    pressed_key = key;
  }
  if (state == PRESSED) {
    Serial.println(pressed_key);
  }
  if (state == HOLD) {
    Serial.println(pressed_key);
  }
  if (state == RELEASED) {
    pressed_key = NO_KEY;
    Serial.println(pressed_key);
  }
}
