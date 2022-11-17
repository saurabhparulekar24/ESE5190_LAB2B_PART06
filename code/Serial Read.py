import matplotlib.pyplot as plt
import numpy as np
import math
import serial

ser = serial.Serial(
        # Serial Port to read the data from
        port='COM5',
 
        #Rate at which the information is shared to the communication channel
        baudrate = 115200,
   
        #Applying Parity Checking (none in this case)
        parity=serial.PARITY_NONE,
 
       # Pattern of Bits to be read
        stopbits=serial.STOPBITS_ONE,
     
        # Total number of bits to be read
        bytesize=serial.EIGHTBITS,
 
        # Number of serial commands to accept before timing out
        timeout=1
)
# Pause the program for 1 second to avoid overworking the serial port
Data = []
T = np.arange(0,1000/(100*10**3),1/(100*10**3))
print(T)
count = 0
while 1:
        x=ser.readline()
        for line in x:
            if line == 45:
                Data.append(1)
            elif line == 95:
                Data.append(0)
        print(Data,len(Data))
        if(Data):
            if count == 0:
                Y1 = np.array(Data)
                Data = []
            else:
                Y2 = np.array(Data)
                Data = []
            count+=1
            if count==2:
                count = 0
                print(Y1,Y2)
                fig, ax = plt.subplots(2, 1)
                ax[0].set_title("SDA")
                ax[1].set_title("SCL")
                ax[0].plot(T,Y1) #row=0, column=0
                ax[1].plot(T,Y2) #row=1, column=0
                fig.tight_layout()
                plt.show()
                #break

ser.close()
        
