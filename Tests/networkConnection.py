import network

ssid = "..."
password = "..."
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)