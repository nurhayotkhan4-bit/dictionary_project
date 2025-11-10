login = {
	"jeymsBond" : "agent007",
	"tony_stark": "ironman101",
 	"piterParker": "spider.12.12",
	"sherlok": "sher.l04"
	}


username = input("Usernamingizni kiriting: ")
parol = input("Parolingizni kiriting: ")

if username in login:
    if login[username] == parol:
        print("Hisobga kirdingiz!")
    else:
        print("Parol noto'g'ri")
else:
    print("Bunday foydalanuvchi mavjud emas")