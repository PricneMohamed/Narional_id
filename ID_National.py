import re
name = input("""
    Hello , Sir 
        What's Your Name?
        """).capitalize().strip()
id = input("""
        Enter National id please: 
        """).strip()

detect = input("""
            Do You Want SQLITE OR CSV OR No?
            """).upper().strip()



male = ['1','3','5','7','9']
female = ['2','4','6' ,'8']
cairo = '01'
alexandria = '02'
port_said = '03'
suez = '04'
damietta = '11'
dakahlia = '12'
sharqia = '13'
qalyubia = '14'
kafr_el_sheikh = '15'
gharbia = '16'
menoufia = '17'
beheira = '18'
ismailia = '19'
giza = '21'
beni_suef = '22'
fayoum = '23'
minya = '24'
assyut = '25'
sohag = '26'
qena = '27'
aswan = '28'
luxor = '29'
red_sea = '31'
new_valley = '32'
matrouh = '33'
north_sinai = '34'
south_sinai = '35'

def time(id):
    if id[0:1] == '2':
        print(f"You Born in 19{id[1:3]}/{id[3:5]}/{id[5:7]}")
        return f"19{id[1:3]}/{id[3:5]}/{id[5:7]}"
    elif id[0:1] == '3':
        print(f"You Born in 20{id[1:3]}/{id[3:5]}/{id[5:7]}")
        return f"20{id[1:3]}/{id[3:5]}/{id[5:7]}"
def born(id):
        if id[7:9] == cairo:
            print("You Born in Cairo")
            return "Cairo"
        elif id[7:9] == alexandria:
            print("You Born in Alexandria")
            return "Alexandria"
        elif id[7:9] == port_said:
            print("You Born in Port Said")
            return "Port Said"
        elif id[7:9] == suez:
            print("You Born in Suez")
            return "Suez"
        elif id[7:9] == damietta:
            print("You Born in Damietta")
            return "Damietta"
        elif id[7:9] == dakahlia:
            print("You Born in dakahlia")
            return "dakahlia"
        elif id[7:9] == sharqia:
            print("You Born in Sharqia")
            return "Sharqia"
        elif id[7:9] == qalyubia:
            print("You Born in Qalyubia")
            return "Qalyubia"
        elif id[7:9] == kafr_el_sheikh:
            print("You Born in Kafr El Sheikh")
            return "Kafr El Sheikh"
        elif id[7:9] == gharbia:
            print("You Born in Gharbia")
            return "Gharbia"
        elif id[7:9] == menoufia:
            print("You Born in Menoufia")
            return "Menoufia"
        elif id[7:9] == beheira:
            print("You Born in Beheira")
            return "Beheira"
        elif id[7:9] == ismailia:
            print("You Born in Ismailia")
            return "Ismailia"
        elif id[7:9] == giza:
            print("You Born in Giza")
            return "Giza"
        elif id[7:9] == beni_suef:
            print("You Born in Beni Suef")
            return "Beni Suef"
        elif id[7:9] == fayoum:
            print("You Born in Fayoum")
            return "Fayoum"
        elif id[7:9] == minya:
            print("You Born in Minya")
            return "Minya"
        elif id[7:9] == assyut:
            print("You Born in Assyut")
            return "Assyut"
        elif id[7:9] == sohag:
            print("You Born in Sohag")
            return "Sohag"
        elif id[7:9] == qena:
            print("You Born in Qena")
            return "Qena"
        elif id[7:9] == aswan:
            print("You Born in Aswan")
            return "Aswan"
        elif id[7:9] == luxor:
            print("You Born in Luxor")
            return "Luxor"
        elif id[7:9] == red_sea:
            print("You Born in Red Sea")
            return "Red Sea"
        elif id[7:9] == new_valley:
            print("You Born in New Valley")
            return "New Valley"
        elif id[7:9] == matrouh:
            print("You Born in Matrouh")
            return "Matrouh"
        elif id[7:9] == north_sinai:
            print("You Born in North Sinai")
            return "North Sinai"
        elif id[7:9] == south_sinai:
            print("You Born in South Sinai")
            return "South Sinai"
def sequence(id):
    print(f"Your sequence {id[9:12]}")
    return f"{id[9:12]}"

def document(id):
    print(f"Document number {id[13:14]}")
    return f"{id[13:14]}"

def normal(id,name ='Sir'):
    print(f"Hello {name}")
    time(id)
    sequence(id)
    born(id)
    type(id)
    document(id)

def type(id):
        if id[12:13] in male:
            print("Your Type is Male")
            return "Your Type is Male"
        elif id[12:13] in female:
            print("Your Type is FeMale")
            return "Your Type is FeMale"

def sql(id,name):
    import sqlite3
    fname = input("""
        Enter File Name Please:
        """)
    ntable = input("""
        Enter Table Name Please:
        """)
    print(f"Hello {name}")
    db = sqlite3.connect(f"{fname}.db")
    cr = db.cursor()
    cr.execute(f"CREATE TABLE IF NOT EXISTS {ntable}(Name TEXT , Birthday TEXT , Pleace TEXT, sequence TEXT , Type TEXT , Authorization TEXT)")
    cr.execute(f"INSERT INTO {ntable} (Name, Birthday, Pleace, sequence, Type, Authorization) VALUES ('{name}', '{time(id)}', '{born(id)}', '{sequence(id)}', '{type(id)}', '{document(id)}')")  
    db.commit()
    db.close()

def csv(id,name):

    import csv
    data = []

    fname = input("""
        Enter File Name Please:
        """)
    key = ['Name' , 'Birthday' , 'Pleace' , 'Sequence' , 'Type' , 'Document']
    with open(f"{fname}.csv" , 'w' ,newline= '') as f:
        w = csv.DictWriter(f ,fieldnames= key)
        w.writeheader()
        list_data = {}
        list_data['Name'] = name
        list_data['Birthday'] = time(id)
        list_data['Pleace'] = born(id)
        list_data['Sequence'] = sequence(id)
        list_data['Type'] = type(id)
        list_data['Document'] = document(id)
        data.append(list_data)
        w.writerows(data)
if len(id) == 14: 
        if re.match(r'^[\w\s]+$', name):
            if  detect == "SQL" or detect == "SQLITE":
                sql(id,name)
            elif  detect == "CSV":
                csv(id,name)
            else:
                normal(id,name)
        else:
            error = "The Name is not Valid"
            raise NameError(error)
elif len(id) >= 14:
    print("The id more than 14 ")
elif len(id) <= 14:
    print("The id less than 14 ")