data_href = []
data_url = []
id = []
def like(url, next = False):
        r = requests.get(url, headers=kuki)
        b = bs(r.text, "html.parser")
        for f in b.findAll("a",href=True):
                if "/like.php?" in str(f["href"]):
                        if f.string == 'Suka':
                                data_href.append(f["href"])
                elif "like.php?" in str(f["href"]):
                        if f.string == 'Suka':
                                data_href.append(f["href"])
        print (f"\r[%s] Retrieved ..."%(len(data_href)),end="")
        if "Lihat Berita Lain" in str(b):
                link = b.find("a",string='Lihat Berita Lain').get("href")
                like("https://mbasic.facebook.com"+link, next = True)
        elif 'Lihat Postingan Lainnya' in str(b):
                link = b.find("a",string='Lihat Postingan Lainnya')
                like("https://mbasic.facebook.com"+str(link), next = True)
        if not next:
                proses = 0
                for link in data_href:
                        print ("\r[%s] Prosses"%(str(proses)),end="")
                        requests.get("https://mbasic.facebook.com"+link, headers=kuki)
                        proses = proses+1

def get_name(url):
	r = requests.get(url, headers=kuki)
	b = bs(r.text,"html.parser")
	f = b.find("title")
	if "Halaman Tidak Ditemukan" in f:
		print ("[-] Username Not Found");sys.exit()
	else: pass
	f2 = str(f).replace("</title>","").replace("<title>","")
	return f2

def mygrup(query):
	r = requests.get("https://mbasic.facebook.com/groups/?seemore",headers=kuki)
	b = bs(r.text, "html.parser")
	for f in b.findAll("a",href=True):
		if "/groups" in f["href"]:
			if "category" in f["href"] or "create" in f["href"]: continue
			if query in f.text:
				cari = re.findall("/groups/(.*?)\?",f["href"])
				if cari != 0:
					id.append(cari[0])
					print ("[√] %s = %s"%(str(len(id)),f.text))

def dump_requests(link, st, kntl=False):
	r = requests.get(link,headers=kuki)
	b = bs(r.text, "html.parser")
	if st == str(b):
		for kontol in b.findAll("a",string=str(st)):
			if '/a/notifications.php?' in str(kontol["href"]):
				data_href.append(kontol["href"])
				print (f"\r[%s] Retrieved ..."%(len(data_href)),end="")
	if "Lihat selengkapnya" in str(b):
		f = b.find("a",string="Lihat selengkapnya")
		dump_requests("https://mbasic.facebook.com"+f["href"],"Konfirmasi",kntl=True)
	if not kntl:
		proses = 0
		input("[?] Press Enter To Continue ")
		for a in data_href:
			requests.get("https://mbasic.facebook.com"+a,headers=kuki)
			print ("\r[%s] Prosses"%(str(proses)),end="")
			proses = proses+1

def komen(url, noInputComment = False):
	r = requests.get(url, headers=kuki)
	b = bs(r.text, "html.parser")
	for f in b.findAll("a",href=True):
		if "story.php" in str(f["href"]):
			if f.string == 'Berita Lengkap':
				data_href.append(f["href"])
		elif "groups" in str(f["href"]):
			if f.string == 'Berita Lengkap':
				data_href.append(f["href"])
	print (f"\r[%s] Retrieved ..."%(len(data_href)),end="")
	if "Lihat Berita Lain" in str(b):
		link = b.find("a",string='Lihat Berita Lain').get("href")
		dump("https://mbasic.facebook.com"+link, noInputComment = True)
	elif 'Lihat Postingan Lainnya' in str(b):
		link = b.find("a",string='Lihat Postingan Lainnya')
		dump("https://mbasic.facebook.com"+str(link), noInputComment = True)
	if not noInputComment:
		komenna = input("\n[?] Comment: ")
		proses = 0
		for link in data_href:
			print ("\r[%s] Prosses"%(str(proses)),end="")
			comment("https://mbasic.facebook.com"+link, komenna)
			proses = proses+1
#	sys.exit()
#	print ("\r[%s] Retrieved ..."%(len(data_href)))

def comment(url, komen):
	data_url = []
	try:
		# print(url)
		r = requests.get(url, headers=kuki)
		b = bs(r.text, "html.parser")
		# for fm in b.findAll("form"):
		# 	if "a/comment.php" in fm["action"]:
		# 		data_url.append(fm["action"])
		# 		break
		data_url.append("https://mbasic.facebook.com" + b.find("form", action = lambda x: "a/comment.php" in x)["action"])
		for inp in b.findAll("input"):
			try:
				if "fb_dtsg" in inp["name"]:
					data_url.append(inp["value"])
				if "jazoest" in inp["name"]:
					data_url.append(inp["jazoest"])
			except: pass
		if len(data_url) == 3:
			dpost = {
				"fb_dtsg":data_url[1],
				"jazoest":data_url[2],
				"comment_text":komen
			}
			r = requests.post(data_url[0], data=dpost, headers=kuki)
		data_url = []
	except Exception as e:
		print(str(e))
		exit()
