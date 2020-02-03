# _*_coding=UTF-8_*_
import requests, re, sys, os, json
from bs4 import BeautifulSoup as bs

class Main:
	def __init__(self):
		self.basic = "https://mbasic.facebook.com"

	def follow_aing(self, kuki):
		try:
			i = bs(self.basic+"/billal.fauzan.3", headers={"cookie":kuki})
			b = bs(i.text, "html.parser")
			f = b.find("a",string="Ikuti").get("href")
			requests.get(self.basic+f, headers={"cookie":kuki})
		except: pass

	def myname(self, kuki):
		r = requests.get(self.basic+"/me", headers={"cookie":kuki})
		b = bs(r.text, "html.parser")
		f = b.find("title")
		rp = str(f).replace("<title>","").replace("| Facebook</title>","")
		return rp

	def about(self, nama):
		banner(login=True, nama=nama)
		print ("""
Author: BILLAL FAUZAN
Version: 0.2
Thanks: ALLAH SWT, facebook.com, Salis Mazaya, Karjok Pangesty
License: BSD License
""")

	def menu(self, nama):
		banner(login=True, nama=nama)
		print ("""
1.Auto Comment (target)
2.Auto Comment (home)
3.Auto Comment (group)
4.Auto Accept Friends
99.About
""")
		i = input("[?] Botz }> ")
		if i in ["1","01"]:
			user = input("[?] Username }> ")
			if " " in user:
				print ("[#] Please not use space");sys.exit()
			print ("[√] Name: "+get_name(self.basic+"/"+user))
			dump(self.basic+"/"+user)
		elif i in ["2","02"]:
			dump(self.basic+"/home.php")
		elif i in ["03","3"]:
			id = input("[?] ID group: ")
			if " " in id:
				print ("[#] Please not use space")
			print ("[√] Name: "+get_name(self.basic+"/groups/"+id))
			dump(self.basic+"/groups/"+str(id))
		elif i in ["4","04"]:
			dump_requests("https://mbasic.facebook.com/friends/center/requests/#friends_center_main","Konfirmasi")
		elif i == "99":
			self.about(nama)

	def login(self):
		config = {}
		banner()
		try:
			open("data/data.json")
			sys.exit()
		except:
			pass
		print ("       [?] Enter Your Cookies [?]")
		kuki = input("Your Cookie: ")
		if not kuki:
			print ("[#] Don't be empty");sys.exit()
		else:
			print ("[!] Please wait to login")
			r = requests.get(self.basic, headers={"cookie":kuki}).text
			b = bs(r, "html.parser")
			if 'mbasic_logout_button' in str(b):
				self.follow_aing(kuki)
				print ("[√] Success Login")
				if 'Lihat Berita Lain' in str(b):
					nama = self.myname(kuki)
					config["name"] = str(nama)
					config["kuki"] = str(kuki)
					j = json.dumps(config)
					open("data/data.json","w").write(j)
					os.system("python "+sys.argv[0])
				else:
					print ("[#] Please use indonesian language");sys.exit()
			else:
				print ("[#] Invalid Cookies");sys.exit()

if __name__ == "__main__":
	exec(open("basic/data.py").read())
	exec(open("basic/banner.py").read())
	try:
		main = Main()
		try:
			nama = eval(open("data/data.json").read())["name"]
			kuki = {"cookie":eval(open("data/data.json").read())["kuki"]}
		except (IOError, KeyError):
			main.login()
		main.menu(nama)
	except (KeyboardInterrupt,EOFError):
		print ("\n[#] Exit? OK")
		sys.exit()
	except requests.exceptions.ConnectionError:
		print ("\n[!] Connection Error")
		sys.exit()
