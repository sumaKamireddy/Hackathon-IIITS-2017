import processing.serial.*;
Serial myPort;  // Create object from Serial class
String val;
Table dataTable; //table where we will read in and store values. You can name it something more creative!
int numReadings = 1; //keeps track of how many readings you'd like to take before writing the file. 
int readingCounter = 0; 
String fileName;
float k[];
void setup()
{
  // I know that the first port in the serial list on my mac
  // is Serial.list()[0].
  // On Windows machines, this generally opens COM1.
  // Open whatever port is the one you're using.
  String portName = "/dev/ttyACM0"; //change the 0 to a 1 or 2 etc. to match your port
dataTable = new Table();  
dataTable.addColumn("moisture");
dataTable.addColumn("value");
dataTable.addColumn("waterflow");
  myPort = new Serial(this, portName, 9600);
}

void serialEvent(Serial myPort){

  val = myPort.readStringUntil('\n'); 
 if (val!= null) { //We have a reading! Record it.
    val = trim(val); //gets rid of any whitespace or Unicode nonbreakable space
    
   float k[]=float(split(val,','));
//float  val=val;
println(k);

 

 //float val=parseFloat(2);
 dataTable.clearRows();
  TableRow newRow = dataTable.addRow();

  newRow.setFloat("moisture", k[0]);
  newRow.setFloat("value", k[1]);
  newRow.setFloat("waterflow", k[2]);
  readingCounter++; //optional, use if you'd like to write your file every numReadings reading cycles
 }   
    //saves the table as a csv in the same folder as the sketch every numReadings. 
    if (readingCounter % numReadings ==0)//The % is a modulus, a math operator that signifies remainder after division. The if statement checks if readingCounter is a multiple of numReadings (the remainder of readingCounter/numReadings is 0)
    {
     saveTable(dataTable, "data/new.csv");
    }

}
void draw()
{
  //String portName = "COM3";
  //myPort = new Serial(this, portName, 9600);
 if(myPort.available()>0)
 {
 serialEvent(myPort); 
}
}