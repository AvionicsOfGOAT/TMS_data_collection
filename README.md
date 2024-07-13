# TMS_data_collection

## Wiring
![Group 293](https://github.com/user-attachments/assets/2ab59834-6283-45e4-94cc-d4be2ce716ba)

## Preparation for collection
1. Install the Arduino program.
2. Copy and paste the code from code.txt into Arduino and compile it (if you 3. encounter an HX711 error, install and include the necessary library).
4. Upload the code to the Arduino.
5. Open the Serial Monitor to test the program.

## Collection process
1. Run the Serial Monitor with the load cell untouched.
2. Verify that each sensor value is being read correctly.
3. After TMS is complete, disconnect the USB cable connected to the Arduino (to 4. preserve data and stop the program).
4. Copy all sensor values recorded in the Serial Monitor and save them to a text file.

## Notes
1. Do not close the Serial Monitor after TMS (closing it will result in loss of output data).
2. To rerun the program, simply reopen the Serial Monitor.
3. Occasionally, gently press the load cell to check if it's working correctly.
