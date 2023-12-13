import serial, time
import serial.tools.list_ports

ser = serial.Serial("COM4", 115200) #chnnge to your COM port
#ser.port = "COM4" #COM port of ESP32
#ser.baudrate = 115200 
ser.bytesize = serial.EIGHTBITS #one byte is eight bits(Japanese equipment usually seen  7 bits?)
ser.parity = serial.PARITY_NONE #no parity check
ser.stopbits = serial.STOPBITS_ONE #modern equipment usually 1 bit
ser.xonxoff = False #disavle xon and xoff, which are flow control regarding the capacity of buffer
ser.rtscts = False #disable 'request to send' and 'clear to send' packet exchange
ser.dsrdtr = False

if ser.isOpen():
	f = open("Voltage.txt" ,'a')
	count = 0
	while True:
		t = time.localtime()
		current_time = time.strftime("%H:%M:%S", t)
		v = ser.read(6).decode("utf-8")

		f.write(current_time + ' ' + v)

		v = v.split('\r')[0]
		print(v)
		count+=1

		if float(v) <= 3.00:
			print(current_time)
			break
		if count >= 3:
			f.close()
			f = open("Voltage.txt", 'a')

	f.close()
else:
	print("Get serial " + ser.port + " fail.\n")
	print(list(serial.tools.list_ports.comports()))