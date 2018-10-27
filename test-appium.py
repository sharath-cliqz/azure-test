from appium import webdriver as wd
from time import sleep
from thread import start_new_thread
from subprocess import call
from subprocess import check_output as co
from datetime.datetime import now

desired_caps = {
    "platformName": "android",
    "appPackage": "com.ghostery.android.ghostery",
    "appActivity": "org.mozilla.gecko.LauncherActivity",
    "deviceName": "Nexus 5",
    "automationName": "UiAutomator2",
    "app": "http://repository.cliqz.com.s3.amazonaws.com/dist/android/nightly/ghostery/latest_x86.apk",
    "noReset" : True
}

def checkDevice():
	out = co(["adb", "devices"])
	if ("emulator" in out) or ("exus" in out):
		return True
	else:
		return False

if __name__ == "__main__":
	try:
		timeout = 2*60 #2 mins or 120 seconds
		start_time = now().replace(microsecond=0)
		while now().replace(microsecond=0) - start_timeme < timeout:
			if checkDevice:
				break
		appium = start_new_thread(call, (["appium"],))
		driver = WD.Remote("http://localhost:4723/wd/hub", desired_caps)
		sleep(15)
		print(driver.page_source)
	except Exception as e:
		print(e)
	finally:
		driver.quit()
		appium.conjugate()