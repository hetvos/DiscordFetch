import rpc
import distro
import time
import subprocess
import os

dobj = distro.linux_distribution(full_distribution_name=True)

def getLImage(id,dname):
	if id in ["archlinuxlogo","manjarolinuxlogo"]:
		return id
	else:
		print(f"Couldn't find a logo for {dname}, tell me what distro you are using and i will add it!")
		print("My Discord: Totally Discord#8671")
		print()
		return "questionmark"

dname = dobj[0]
dlogoid = ''.join(dname.split()).lower() + "logo"
uptime = float(os.popen("cat /proc/stat | grep btime | awk '{print $2}'").read())

limage = getLImage(dlogoid,dname)

client_id = '740300573303242813'
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)
print("RPC connection successful.")

while True:
	activity = {
		"details": f"Kernel: {os.popen('uname -r').read()}",
		"timestamps" : {
			"start": uptime
		},
		"assets": {
			"large_image": limage,
			"large_text": dname
		}
	}
	rpc_obj.set_activity(activity)
	time.sleep(30)