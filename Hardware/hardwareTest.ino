/*
    this code is for checking the hardware connection you have made

  open your serial monitor and type
  0: for stopping the motors
  1: moving both of them in forward direction
  2: moving both of them in forward direction but the right motor moves slowly
  3: moving both of them in forward direction but the left motor slower
*/



//renaming the pins for better identification
#define in1 D1 // --> in1 = D1
#define in2 D2
#define in3 D3
#define in4 D5
#define ena D6
#define enb D7

// some global variables
int pwmL = 255;
int pwmR = 255;
int i = 0;
int incomingByte = 0;


void setup()
{
  //nodemcu will start communicating with the laptop at 115200 baudrate
  Serial.begin(115200);

  //set corresponding pinModes
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(ena, OUTPUT);
  pinMode(enb, OUTPUT);

  //motors should be moving forward with this config
  digitalWrite(in1, 1);
  digitalWrite(in2, 0);
  digitalWrite(in3, 0);
  digitalWrite(in4, 1);


}

void loop()
{ if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
    incomingByte -= 48;

    // say what you got:
    Serial.print("I received: ");

  }
  Serial.println(incomingByte);
  switch (incomingByte) {
    case 0:
      analogWrite(ena, 0);
      analogWrite(enb, 0);
      break;

    case 1:
      analogWrite(ena, 255);
      analogWrite(enb, 255);
      break;

    case 2:
      analogWrite(ena, 255);
      analogWrite(enb, 100);
      break;

    case 3:
      analogWrite(ena, 100);
      analogWrite(enb, 255);

    default:
      analogWrite(ena, 0);
      analogWrite(enb, 0);
      break;
  }

}

