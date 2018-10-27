from appium import webdriver as WD
from time import sleep
from multiprocessing import Process
from subprocess import call
from subprocess import check_output as co
import sys

reload(sys)
sys.setdefaultencoding('utf8')

desired_caps = {
    "platformName": "android",
    "appPackage": "com.ghostery.android.ghostery",
    "appActivity": "org.mozilla.gecko.LauncherActivity",
    "deviceName": "Nexus 5",
    "automationName": "UiAutomator2",
    "app": "http://repository.cliqz.com.s3.amazonaws.com/dist/android/nightly/ghostery/latest_x86.apk",
    "noReset" : True
}

def checkDeviceBootStatus():
	try:
		return co(["adb", "shell", "getprop", "sys.boot_completed"]).strip()
	except:
		return 0

if __name__ == "__main__":
	try:
		emulator = Process(target=call, args=(["/Users/vsts/Library/Android/sdk/emulator/emulator", "-avd", "Nexus5Emu"],))
		emulator.start()
		count = 1
		while count < 600:
			if checkDeviceBootStatus() == "1":
				break
			count += 1
			sleep(1)
		appium = Process(target=call, args=(["appium"],))
		appium.start()
		sleep(20)
		driver = WD.Remote("http://localhost:4723/wd/hub", desired_caps)
		sleep(15)
		print((driver.page_source).replace(">", ">\n"))
	except Exception as e:
		print(e)
	finally:
		driver.quit()
		co(["adb", "-e", "emu", "kill"])
		sys.exit()
