import speedtest

#setup for the speedtest

obj = speedtest.Speedtest()

print("obtaining Server list ...")

obj.get_servers() #provides a list of servers

print("getting the best server ... ")

optimalServer = obj.get_best_server() #choose optimal server

print(optimalServer)


print(f"Found: {optimalServer['host'] } Located in {optimalServer['country']}")

#the speedtest code starts from here

print("processing download speed ...")

download_result = obj.download()

print("processing upload speed ... ")

upload_result = obj.upload()

ping_result = obj.results.ping

print(f"Download Speed : {download_result / 1024 / 1024:.2f} Mbit/s")

print(f"upload Speed : {upload_result / 1024 / 1024:.2f} Mbit/s")

print(f"ping : {ping_result } ms ")



