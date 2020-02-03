def banner(login=False, nama=False):
	os.system("clear")
	print ("""
                              )  
            (           )  ( /(  
          ( )\       ( /(  )\()) 
          )((_)  (   )\())((_)\  
         ((_)_   )\ (_))/  _((_) 
          | _ ) ((_)| |_  |_  /  
          | _ \/ _ \|  _|  / /   
          |___/\___/ \__| /___|  """)
	if login == True:
		print ("        [+]   %s   [+]"%(nama))
	else: pass
