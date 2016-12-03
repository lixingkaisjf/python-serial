import time
import serial

# 设置串口
# 在linux下串口是字符串 /dev/ttyACM0
# ser = serial.Serial('/dev/ttyACM0', 9600)  # 没有timeout, 一直保持连接
# ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # timeout扫描串口间隔时间，超过时间没有返回数据，自动断开

port = '/dev/ttyUSB0'
ser = serial.Serial(port, 9600, timeout=0.1)  # timeout扫描串口间隔时间，
print(ser)
print(ser.portstr)	# 串口名称

# 打开串口
ser.isOpen()
if ser.isOpen() == False:
	ser.open()

# # 关闭串口
# ser.close()
# ser.isOpen()


print('---------------------------------------------------------')


# # 发送 数据
# str1 = 'send data\n'
# byte1 = str1.encode(encoding="utf-8")	# 把字符串转为 bytes
# ser.write(byte1)

# # 读取 数据
# byte1 = ser.readline()	# 接收到的数据是bytes类型
# print(byte1)



while 1:
	# 输入数据 (不能为空)
	input_str = input('enter some words:')
	if input_str == "":
		while 1:
			input_str = input('enter some words:')
			if input_str != "":
				break
	# 发送 数据
	byte1 = input_str.encode(encoding="utf-8")	# 把字符串转为 bytes
	ser.write(byte1)

	# 读取 数据
	# n=ser.inWaiting()	# 返回接收字符串的长度值，然后把这个值赋给read做参数
	# print("buffer:",n)
	# #print(ser.read(n))
	
	count=0
	while 1:
		print("--------------------------------------")
		time.sleep(0.02)
		byte1 = ser.readline()	# 读取的数据是bytes类型
		# byte1 = ser.read(4) # 读取4个字节
		print(byte1)
		str1 = str(byte1, encoding = "utf-8")	# 把 bytes 转换成 str
		print(str1)
		
		
		# 读取任意数据
		print("buffer:",ser.inWaiting())  # 缓冲区字节数
		n = ser.inWaiting()
		if(n==0):
			break
		
		# 读取固定 行数
		# count+=1	# 读取总行数
		# print("count:",count)
		# if(count==4):
			# break

		




	
# Methods of Serial instances
# open()                  # （打开串口）open port
# close()                 # （关闭串口）close port immediately 
# setBaudrate(baudrate)   # change baud rate on an open port
# inWaiting()             # （返回 buffer缓冲器 字节数）return the number of chars in the receive buffer
# read(size=1)            # （读取数据）read "size" characters
# write(s)                # （写入数据）write the string s to the port
# flushInput()            # flush input buffer, discarding all it's contents
# flushOutput()           # flush output buffer, abort output
# sendBreak()             # send break condition
# setRTS(level=1)         # set RTS line to specified logic level
# setDTR(level=1)         # set DTR line to specified logic level
# getCTS()                # return the state of the CTS line
# getDSR()                # return the state of the DSR line
# getRI()                 # return the state of the RI line
# getCD()                 # return the state of the CD line


# Attributes of Serial instances
# portstr                 # device name
# BAUDRATES               # list of valid baudrates
# BYTESIZES               # list of valid byte sizes
# PARITIES                # list of valid parities
# STOPBITS                # list of valid stop bit widths


# New values can be assigned to the following attributes, the port will be reconfigured, even if it's opened at that time:
# port                    # port name/number as set by the user
# baudrate                # current baud rate setting
# bytesize                # byte size in bits
# parity                  # parity setting
# stopbits                # stop bit with (1,2)
# timeout                 # timeout setting
# xonxoff                 # if Xon/Xoff flow control is enabled
# rtscts                  # if hardware flow control is enabled
