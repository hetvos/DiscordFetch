import rpc
import distro
from time import sleep
import requests
import json
import os

## Application ID to use ##
application_id = '1006437180383690813'

## dumb way to make logo change if added while DiscordFetch is running without spamming terminal ##
no_logo_warning = False

## FUNCTION: Gets a logo ID to use ##
def getLogoID():
	global no_logo_warning
	logos = json.loads(requests.get(f"https://discord.com/api/v9/oauth2/applications/{application_id}/assets").content)
	logo_id = next((item["name"] for item in logos if item["name"] == distro.id()), "tux")
	if logo_id == "tux" and not no_logo_warning:
		print(f"oops! we don't have a logo for id `{distro.id()}`")
		print("create an issue on github and give us that id so we can add it!")
		no_logo_warning = True
	return logo_id

## Get the uptime ##
uptime = float(os.popen("cat /proc/stat | grep btime | awk '{print $2}'").read())

## Get RPC object ##
rpc_obj = rpc.DiscordIpcClient.for_platform(application_id)

## MAIN LOOP: Sets the RPC activity every 30 seconds. ##
while True:
	activity = {
		"details": f"Kernel: {os.popen('uname -r').read()}",
		"timestamps" : {
			"start": uptime
		},
		"assets": {
			"large_image": getLogoID(),
			"large_text": distro.name()
		}
	}
	rpc_obj.set_activity(activity)
	sleep(30)
