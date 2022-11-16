# Trace of RP2040-ADPS9960 exchange
First we captured the RAW trace on a serial terminal(below)

![pioscope_zoom_capture](https://user-images.githubusercontent.com/57740824/202064834-c154c60f-2e57-40a3-8268-814069fdb3cf.png)

To get a better visual, we read the data using a python script and plotted the data

![cap2](https://user-images.githubusercontent.com/57740824/202294740-2d935884-f425-47e5-b089-f15db829bdea.png)

We can see that the above recorded trace is exactly similar with the one captured on the oscilloscope, In case of the above trace, the time scale shows time in seconds. The clock of I2C was 80kHz, Therefore we captured data at 630kHz(8 times) for easy reconstruction of the original data

![real_cap](https://user-images.githubusercontent.com/57740824/202295431-88538811-78e1-4d05-95bd-32fb0965a4a4.png)
