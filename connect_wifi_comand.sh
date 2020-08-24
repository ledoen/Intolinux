ifconfig  #list in-use net interface

#if the wlan interface is not open, open it

ifconfig -a
ifconfig wlan1 up

#add config file

wpa_passphrase "wifi-name" "password" >/etc/wpa_supplicant/wifi-name.conf

#connect the wifi

wpa_supplicant -Dnl80211 -iwlan1 -c/etc/ASUS-joey.conf -B #-D:driver  -B:backend
#or
wpa_supplicant -Dwext -iwlan1 -c/etc/ASUS-joey.conf &
