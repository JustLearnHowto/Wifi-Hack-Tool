import pywifi
from pywifi import const
import time



class WiFi:

	def __init__(self):
		super().__init__()

		self.wifi = pywifi.PyWiFi()

		self.iface = self.wifi.interfaces()[0]

		self.tmp_profile = None


	def disconnect(self):
		self.iface.disconnect()
		assert self.iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

	def update_profiles(self, profile):
		self.iface.remove_all_network_profiles()
		self.tmp_profile = self.iface.add_network_profile(profile)

		self.iface.connect(self.tmp_profile)

	def check_connection(self):
		assert self.iface.status() == const.IFACE_CONNECTED

	def get_adapter_name(self):
		return self.iface.name()

	def scan(self, delay=1):
		self.iface.scan()

		time.sleep(delay)

		return self.iface.scan_results()


	class Profile(pywifi.Profile):
		def __init__(self, ssid, key = '12345678'):
			self.ssid = ssid
			self.auth = const.AUTH_ALG_OPEN
			self.akm = [const.AKM_TYPE_WPA2PSK]
			self.cipher = const.CIPHER_TYPE_CCMP
			self.key = key
