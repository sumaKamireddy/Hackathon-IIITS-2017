int sensor_pin0 = A0;
int sensor_pin1 = A1;
int sensor_pin2 = A2;
int sensor_pin3 = A3;

int output_value0 ;
int output_value1 ;
int output_value2 ;
int output_value3 ;


byte sensorInterrupt = 0;  // 0 = digital pin 2
byte sensorPin       = 2;

// The hall-effect flow sensor outputs approximately 4.5 pulses per second per
// litre/minute of flow.
float calibrationFactor = 4.5;

volatile byte pulseCount;  

float flowRate;
unsigned int flowMilliLitres;
unsigned long totalMilliLitres;

unsigned long oldTime;


void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);

  pinMode(sensorPin, INPUT);
  digitalWrite(sensorPin, HIGH);

  pulseCount        = 0;
  flowRate          = 0.0;
  flowMilliLitres   = 0;
  totalMilliLitres  = 0;
  oldTime           = 0;

  // The Hall-effect sensor is connected to pin 2 which uses interrupt 0.
  // Configured to trigger on a FALLING state change (transition from HIGH
  // state to LOW state)
  attachInterrupt(sensorInterrupt, pulseCounter, FALLING);
  
  delay(2000);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  

  output_value1= analogRead(sensor_pin1);
  output_value1 = map(output_value1,550,0,0,100);
 
  Serial.print(output_value1*(-1));
  
  Serial.print(',');
  
  delay(5);

  output_value2 = analogRead(sensor_pin2); //Read data from analog pin and store it to value variable
  Serial.print(output_value2);

  Serial.print(',');

  if((millis() - oldTime) > 1000)    // Only process counters once per second
  { 
    // Disable the interrupt while calculating flow rate and sending the value to
    // the host
    detachInterrupt(sensorInterrupt);
   
    flowRate = ((1000.0 / (millis() - oldTime)) * pulseCount) / calibrationFactor;
    
    oldTime = millis();
    
    flowMilliLitres = (flowRate / 60) * 1000;
  
    totalMilliLitres += flowMilliLitres;
      
    unsigned int frac;
    
    Serial.println((flowRate));  // Print the integer part of the variable
    //Serial.print(".");             // Print the decimal point
    // Determine the fractional part. The 10 multiplier gives us 1 decimal place.
    frac = (flowRate - int(flowRate)) * 10;
    //Serial.println(frac, DEC) ;      // Print the fractional part of the variable
    
    // Reset the pulse counter so we can start incrementing again
    pulseCount = 0;
    
    // Enable the interrupt again now that we've finished sending output
    attachInterrupt(sensorInterrupt, pulseCounter, FALLING);
  }
  delay(5000);

  
}

void pulseCounter()
{
  // Increment the pulse counter
  pulseCount++;
}

