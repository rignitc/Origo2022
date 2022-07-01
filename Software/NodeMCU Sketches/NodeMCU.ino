#include <stdio.h>
#include <ESP8266WiFi.h>
#include <WiFiUdp.h>


#define UDP_PORT 4210

#define in1 D1
#define in2 D2
#define in3 D3
#define in4 D5
#define ena D6
#define enb D7

const char *ssid = "<Enter SSID>"; // The SSID (name) of the Wi-Fi network you want to connect to
const char *password = "<Enter Password>";

int left_pwm = 0;
int right_pwm = 0;
int i = 0;

// UDP
WiFiUDP UDP;
char packet[255];
char reply[] = "Packet received!";

void setup()
{
    Serial.begin(115200);

    pinMode(in1, OUTPUT);
    pinMode(in2, OUTPUT);
    pinMode(in3, OUTPUT);
    pinMode(in4, OUTPUT);
    pinMode(ena, OUTPUT);
    pinMode(enb, OUTPUT);

    digitalWrite(in1, 1);
    digitalWrite(in2, 0);
    digitalWrite(in3, 0);
    digitalWrite(in4, 1);

    Serial.println('\n');
    WiFi.begin(ssid, password); // Connect to the network
    Serial.print("Connecting to ");
    Serial.print(ssid);
    Serial.println(" ...");

    int i = 0;
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(++i);
        Serial.print(' ');
    }
    WiFi.setSleepMode(WIFI_NONE_SLEEP);
    
    Serial.println('\n');
    Serial.println("Connection established!");
    Serial.print("IP address:\t");
    Serial.println(WiFi.localIP()); // Send the IP address of the ESP8266 to the computer

    // Begin listening to UDP port
    UDP.begin(UDP_PORT);
    Serial.print("Listening on UDP port ");
    Serial.println(UDP_PORT);
}

void loop()
{
    int packetSize = UDP.parsePacket();
    if (packetSize)
    {
        Serial.print("Received packet! Size: ");
        Serial.println(packetSize);
        int len = UDP.read(packet, 255);
        if (len > 0)
        {
            packet[len] = '\0';
        }
        Serial.print("Packet received: ");
        Serial.println(packet);

        int pwmL = 0;
        int pwmR = 0;

        for (i = 0; i < 3; i++)
        {
            pwmL = pwmL * 10 + (packet[i] - 48);
        }
        
        for (i = 4; i < 7; i++)
        {
            pwmR = pwmR * 10 + (packet[i] - 48);
        }

        Serial.print(pwmL);
        Serial.print(",");
        Serial.println(pwmR);

        analogWrite(ena, pwmL);
        analogWrite(enb, pwmR);
    }
    
}