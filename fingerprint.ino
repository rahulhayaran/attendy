/*************************************************** 
  This is an example sketch for our optical Fingerprint sensor

  Designed specifically to work with the Adafruit BMP085 Breakout 
  ----> http://www.adafruit.com/products/751

  These displays use TTL Serial to communicate, 2 pins are required to 
  interface
  Adafruit invests time and resources providing this open source code, 
  please support Adafruit and open-source hardware by purchasing 
  products from Adafruit!

  Written by Limor Fried/Ladyada for Adafruit Industries.  
  BSD license, all text above must be included in any redistribution
 ****************************************************/
//#include <Fingerprint_Database.h>

#include <Adafruit_Fingerprint.h>

// On Leonardo/Micro or others with hardware serial, use those! #0 is green wire, #1 is white
// uncomment this line:
// #define mySerial Serial1

// For UNO and others without hardware serial, we must use software serial...
// pin #2 is IN from sensor (GREEN wire)
// pin #3 is OUT from arduino  (WHITE wire)
// comment these two lines if using hardware serial
#include <SoftwareSerial.h>
SoftwareSerial mySerial(2, 3);
int id_found = -1;

String names[] = {"", "Rimika Banerjee","Sravya Basvapatri","Ryan Chen","Luofei Chen","Kai Chorazewicz","Ashvin Dhawan","Quin Etnyre","Jahnvi Doshi","Charlie Faramarzi","Diego Gonzalez","Chai Goyal","Alara Guler","Amy Guo","Shiyuan Guo","Matt Hallac","Kelly Han","Rahul Hayaran","Neha Hudait","Francis Indaheng","Ayush Jain","Daniel Jing","Nishi Kaza","Andrew Kirillov","Elliot Larson","Aadhrik Kuila","Sean Lin","Chelsea Lo","Richard Liu","Nikhil Mandava","Alexander Manes","Michael McNabb","Ethan Mehta","Erel Saul","Rishma Murugan","Neha Nagabothu","Deven Navani","Dev Ojha","Harish Palani","Anika Ramachandran","Manav Rathod","Alfonso Sanchez","Birkaran Sachdev","David Shau","Vikram Shirsat","Jaiveer Singh","Austin Sun","Prangan Tooteja","Michael Trehan","Julius Vering","Hannah Vinh","Vincent Wang","Isabelle Zhou"};

int present[] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};

Adafruit_Fingerprint finger = Adafruit_Fingerprint(&mySerial);
//Fingerprint_Database fpdb = Fingerprint_Database();



/*
  String *names[53];
  names[1] = & "Rimika Banerjee";
names[2] = & "Sravya Basvapatri";
names[3] = & "Ryan Chen";
names[4] = & "Luofei Chen";
names[5] = & "Kai Chorazewicz";
names[6] = & "Ashvin Dhawan";
names[7] = & "Quin Etnyre";
names[8] = & "Jahnvi Doshi";
names[9] = & "Charlie Faramarzi";
names[10] = & "Diego Gonzalez";
names[11] = & "Chai Goyal";
names[12] = & "Alara Guler";
names[13] = & "Amy Guo";
names[14] = & "Shiyuan Guo";
names[15] = & "Matt Hallac";
names[16] = & "Kelly Han";
names[17] = & "Rahul Hayaran";
names[18] = & "Neha Hudait";
names[19] = & "Francis Indaheng";
names[20] = & "Ayush Jain";
names[21] = & "Daniel Jing";
names[22] = & "Nishi Kaza";
names[23] = & "Andrew Kirillov";
names[24] = & "Elliot Larson";
names[25] = & "Aadhrik Kuila";
names[26] = & "Sean Lin";
names[27] = & "Chelsea Lo";
names[28] = & "Richard Liu";
names[29] = & "Nikhil Mandava";
names[30] = & "Alexander Manes";
names[31] = & "Michael McNabb";
names[32] = & "Ethan Mehta";
names[33] = & "Erel Saul";
names[34] = & "Rishma Murugan";
names[35] = & "Neha Nagabothu";
names[36] = & "Deven Navani";
names[37] = & "Dev Ojha";
names[38] = & "Harish Palani";
names[39] = & "Anika Ramachandran";
names[40] = & "Manav Rathod";
names[41] = & "Alfonso Sanchez";
names[42] = & "Birkaran Sachdev";
names[43] = & "David Shau";
names[44] = & "Vikram Shirsat";
names[45] = & "Jaiveer Singh";
names[46] = & "Austin Sun";
names[47] = & "Prangan Tooteja";
names[48] = & "Michael Trehan";
names[49] = & "Julius Vering";
names[50] = & "Hannah Vinh";
names[51] = & "Vincent Wang";
names[52] = & "Isabelle Zhou";
*/
void setup()  
{
 
  Serial.begin(9600);
  while (!Serial);  // For Yun/Leo/Micro/Zero/...
  delay(100);
  Serial.println("\n\nAttendy finger detect test");

  // set the data rate for the sensor serial port
  finger.begin(57600);
  
  if (finger.verifyPassword()) {
    Serial.println("Found fingerprint sensor!");
  } else {
    Serial.println("Did not find fingerprint sensor :(");
    while (1) { delay(1); }
  }

  finger.getTemplateCount();
  Serial.print("Sensor contains "); Serial.print(finger.templateCount); Serial.println(" templates");
  Serial.println("Waiting for valid finger...");
}

void loop()                     // run over and over again
{
  getFingerprintIDez();

  delay(50);            //don't ned to run this at full speed.
  
}

uint8_t getFingerprintID() {
  uint8_t p = finger.getImage();
  switch (p) {
    case FINGERPRINT_OK:
      Serial.println("Image taken");
      break;
    case FINGERPRINT_NOFINGER:
      Serial.println("No finger detected");
      return p;
    case FINGERPRINT_PACKETRECEIVER:
      Serial.println("Communication error");
      return p;
    case FINGERPRINT_IMAGEFAIL:
      Serial.println("Imaging error");
      return p;
    default:
      Serial.println("Unknown error");
      return p;
  }

  // OK success!

  p = finger.image2Tz();
  switch (p) {
    case FINGERPRINT_OK:
      Serial.println("Image converted");
      break;
    case FINGERPRINT_IMAGEMESS:
      Serial.println("Image too messy");
      return p;
    case FINGERPRINT_PACKETRECEIVER:
      Serial.println("Communication error");
      return p;
    case FINGERPRINT_FEATUREFAIL:
      Serial.println("Could not find fingerprint features");
      return p;
    case FINGERPRINT_INVALIDIMAGE:
      Serial.println("Could not find fingerprint features");
      return p;
    default:
      Serial.println("Unknown error");
      return p;
  }
  
  // OK converted!
  p = finger.fingerFastSearch();
  if (p == FINGERPRINT_OK) {
    Serial.println("Found a print match!");
  } else if (p == FINGERPRINT_PACKETRECEIVER) {
    Serial.println("Communication error");
    return p;
  } else if (p == FINGERPRINT_NOTFOUND) {
    Serial.println("Did not find a match");
    return p;
  } else {
    Serial.println("Unknown error");
    return p;
  }   
  
  // found a match!
  Serial.print("Found ID #"); Serial.print(finger.fingerID); 
  Serial.print(" with confidence of "); Serial.println(finger.confidence); 

  return finger.fingerID;
}

// returns -1 if failed, otherwise returns ID #
int getFingerprintIDez() {
  uint8_t p = finger.getImage();
  if (p != FINGERPRINT_OK)  return -1;

  p = finger.image2Tz();
  if (p != FINGERPRINT_OK)  return -1;

  p = finger.fingerFastSearch();
  if (p != FINGERPRINT_OK)  return -1;
  
  // found a match!
  Serial.print("Found ID #"); Serial.print(finger.fingerID); 
  Serial.print(" with confidence of "); Serial.println(finger.confidence);
  Serial.println("TEST PRINT");
  Serial.println(names[finger.fingerID]);
  present[finger.fingerID] = 1;
  Serial.println();
  for(int j = 0; j < 53; j++){
    Serial.print(present[j]);
    Serial.print(" ");
  }
  
  return finger.fingerID; 
}
