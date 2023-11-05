
import datetime
import pickle

#クラス定義
class Person:
	#国籍
	NATIONALITY= None
	#コンストラクタ
	def __init__(self, firstname, lastname, age, gender):
		self.firstname = firstname
		self.lastname = lastname
		self.age = age
		self.gender = gender
	#変数name操作
	def setName(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname
	def getName(self):
		fullname = "{0} {1}".format(self.firstname, self.lastname)
		return fullname
	#変数age操作
	def setAge(self, age):
		self.age=age
	def getAge(self):
		return self.age
	def addAge(self):
		self.age += 1
	#変数gender操作
	def setGender(self, gender):
		self.gender=gender
	def getGender(self):
		return self.gender

#
class American(Person):
	NATIONALITY="American"
	STATE="General"
	def __init__(self, firstname, middlename, lastname, age, gender):
		super().__init__(firstname, lastname, age, gender)
		#middlename
		self.middlename = middlename
	def setName(self, firstname, middlename, lastname):
		self.fistname=firstname
		self.middlename=middlename
		self.lastname=lastname
	def getName(self):
		fullname = "{0} {1} {2}".format( self.firstname, self.middlename, self.lastname)
		return fullname	
#
class Singaporean(Person):
	NATIONALITY= "Singaporean"
	def getName(self):
		fullname = "{0} {1}".format( self.lastname, self.firstname)
		return fullname
#
class Japanese(Person):
	NATIONALITY="日本"
	def getName(self):
		fullname = "{0} {1}".format( self.lastname, self.firstname)
		return fullname

	
#
class PersonDB:
	FILENAME = "data.pickle"
	MENU_1="１：個人情報入力、２：個人情報保存、３：個人情報表示、９：終了　―　"
	MENU_2="１：アメリカ国籍、２：シンガポール国籍、３：日本国籍、９：戻る　―　"
	def __init__(self):
		self.db=[]
	def disMenu1(self):
		return int(input(self.MENU_1))
		
	def disMenu2(self):
		return int(input(self.MENU_2))
		

	def inputAmerican(self):
		input_firstname = input("ファーストネーム：")
		input_middlename = input("ミドルネーム：")
		input_lastname = input("ラストネーム：")
		input_age=int(input("年齢："))
		input_gender = input("性別を入力（M or F）：")
		self.db.append(American(input_firstname, input_middlename, input_lastname, input_age, input_gender))

	def inputSingaporean(self):
		input_firstname = input("ファーストネーム：")
		input_lastname = input("ラストネーム：")
		input_age=int(input("年齢："))
		input_gender = input("性別を入力（M or F）：")
		self.db.append(Singaporean(input_firstname, input_lastname, input_age, input_gender))
	def inputJapanese(self):
		input_firstname = input("姓：")
		input_lastname = input("名：")
		input_age=int(input("年齢："))	
		input_gender = input("性別を入力（M or F）：")
		self.db.append(Japanese(input_firstname,  input_lastname, input_age, input_gender))
	def dumpDB(self):	
		try:	
			with open(self.FILENAME, mode="wb") as file:
				pickle.dump(self.db, file)
		except Exception as e:
			print("ファイル入力エラー, {0}".format(e))

	def loadDB(self):
		
		buf = ""
		try:
			with open(self.FILENAME, mode="rb") as file:
				buf = pickle.load(file)

		except Exception as e:
			print("エラー, {0}".format(e))
		return buf
		
			

###########################################################################
persondb = PersonDB()

#ループ継続フラグ
loop_flag_1 = True
loop_flag_2 = True




while loop_flag_1 == True:
	loop_flag_2 = True
	input_data_1=persondb.disMenu1()

	if input_data_1 == 1:

		while loop_flag_2 == True:
			input_data_2= persondb.disMenu2()

			if input_data_2 == 9:
				loop_flag_2 = False

			elif input_data_2 == 1:
				persondb.inputAmerican()

			elif input_data_2 == 2:
				persondb.inputSingaporean()

			elif input_data_2 == 3:
				persondb.inputJapanese()
	elif input_data_1 == 2:
		
		persondb.dumpDB()
	elif input_data_1 == 3:
		list = persondb.loadDB()
		for obj in list:
			print("{0},{1},{2},{3}".format(obj.getName(),obj.getAge(),obj.getGender(),obj.NATIONALITY)	)	
	elif input_data_1 == 9:
		loop_flag_1 = False

print("プログラム終了")	



