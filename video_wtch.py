import webbrowser, time

url = 'https://youtu.be/F-gRPC4XN10'
while True:
	try:
		dur = 30
		break
	except:
		print("Введите число!")
while True:
	try:
		wtc = 10
		break
	except:
		print("Введите число!")

for i in range(wtc):
	webbrowser.open_new(url)
	time.sleep(dur)
