import kivy
import pickle
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from User import UserDate
import re
from datetime import datetime as dt
import datetime

class CreateWindow(Screen):
    user = ObjectProperty(None)
    password = ObjectProperty(None)
    email = ObjectProperty(None)
    def submit(self):
        if self.user.text != "" and self.email.text !="" and self.email.text.count("@") ==1 and self.email.text.count(".")>0:
            if self.password.text != "":
                testuser = Users.add_user(self.user.text, self.password.text, self.email.text)
                if testuser == 1:
                    self.reset()
                    WM.current = "Login"
                else:
                    Poperror().invalidForm()
            else:
                Poperror().invalidForm()
        else:
            Poperror().invalidForm()

    def cancel(self):
        self.reset()
        WM.current = "Login"

    def reset(self):
        self.user.text = ""
        self.password.text = ""
        self.email.text = ""


class LoginWindow(Screen):
    user = ObjectProperty(None)
    password = ObjectProperty(None)

    def login(self):
        if Users.validata(self.user.text, self.password.text):
            MianWindow.currentuser = self.user.text
            self.reset()
            WM.current = "Main"
        else:
            Poperror().invalidLogin()

    def register(self):
        self.reset()
        WM.current = "Create"

    def forgot(self):
        self.reset()
        WM.current = "Forget"

    def reset(self):
        self.user.text = ""
        self.password.text = ""


class ForgetWindow(Screen):
    user = ObjectProperty(None)
    email = ObjectProperty(None)

    def check_pass(self):
        if Users.find_password(self.user.text, self.email.text):
            self.found()
            self.reset()
        else:
            Poperror().invalidInfo()
            self.reset()

    def found(self):

        Pasword = Users.find_password(self.user.text, self.email.text)

        pop = Popup(title='Found Password',
                    content=Label(text=Pasword),
                    size_hint=(None, None), size=(400, 400))
        pop.open()

    def reset(self):
        self.user.text = ""
        self.email.text = ""


class MianWindow(Screen):
    currentuser =""
    username = ObjectProperty(None)
    def Addpet(self):
        WM.current = "Add"

    def Printpet(self):
        WM.current = "Print"

    def Printall(self):
        WM.current = "All"

    def logoff(self):
        WM.current = "Login"

    def on_enter(self, *args):
        self.username.text = "User:  " + str(self.currentuser)



class AddWindow(Screen):
    Manmal = {}
    Fish = {}
    Amphibians = {}

    isAmphibians = BooleanProperty(False)
    isFishMenu = BooleanProperty(False)
    isMamMenu = BooleanProperty(False)
    Atype = StringProperty("")
    hasClaws = StringProperty("")
    isVenomous = StringProperty("")

    litter = ObjectProperty(None)
    condition = ObjectProperty(None)
    length = ObjectProperty(None)
    nNamee = ObjectProperty(None)
    dOB = ObjectProperty(None)
    weight = ObjectProperty(None)
    owner = ObjectProperty(None)
    address = ObjectProperty(None)

    def check(self,floatnum):
        regex = '^[A-Za-z0-9]*$'
        if (re.search(regex, floatnum)):
            return True
        else:
            return False

    def checkcon(self,floatnum):
        regex = '^[A-Za-z0-9]*$'
        if (re.search(regex, floatnum)):
            return True
        else:
            return False

    def checkdate(self,date):
        regex = r'\d{4}[-/]\d{2}[-/]\d{2}'
        if (re.search(regex, date)):
            return True
        else:
            return False


    def insert_data(self,litter,condition, length, nNamee,dOB,weight,owner,address):
        print("Type={}".format(self.Atype))
        print("Has Claws={}".format(self.hasClaws))
        print("Is Venomous={}".format(self.isVenomous))
        print("Litter={}".format(litter))
        print("Condition={}".format(condition))
        print("Length={}".format(length))
        print("Age={}".format(nNamee))
        print("DOB={}".format(dOB))
        print("Weight={}".format(weight))
        print("Owner={}".format(owner))
        print("Address={}".format(address))

        if self.check(nNamee) is True and self.check(owner) is True and self.check(address) is True:
            if self.checkdate(dOB) is True:
                if self.Atype == "Mammal":
                    self.Manmal["Animal Type"] = self.Atype
                    self.Manmal["Pet Name"] = nNamee
                    self.Manmal["Pet DOB"] = dOB
                    self.Manmal["Birth Weight"] = weight
                    self.Manmal["Owner Name"] = owner
                    self.Manmal["Owner Address"] = address
                    self.Manmal["Litter Size"] = litter
                    self.Manmal["Has Claws"] = self.hasClaws

                    self.save(self.Manmal)

                if self.checkcon(condition) is True:

                    if self.Atype == "Fish":
                        self.Fish["Animal Type"] = self.Atype
                        self.Fish["Pet Name"] = nNamee
                        self.Fish["Pet DOB"] = dOB
                        self.Fish["Birth Weight"] = weight
                        self.Fish["Owner Name"] = owner
                        self.Fish["Owner Address"] = address
                        self.Fish["Scale Condition"] = condition
                        self.Fish["Length"] = length

                        self.save(self.Fish)
                else:
                    Poperror().invalidValue()

                if self.Atype == "Amphibians":
                    self.Amphibians["Animal Type"] = self.Atype
                    self.Amphibians["Pet Name"] = nNamee
                    self.Amphibians["Pet DOB"] = dOB
                    self.Amphibians["Birth Weight"] = weight
                    self.Amphibians["Owner Name"] = owner
                    self.Amphibians["Owner Address"] = address
                    self.Amphibians["Is Venomous"] = self.isVenomous

                    self.save(self.Amphibians)
            else:
                Poperror().invalidValue()
        else:
            Poperror().invalidValue()

    def clearn(self):
        self.litter.text = ""
        self.condition.text = ""
        self.length.text = ""
        self.nNamee.text = ""
        self.dOB.text = ""
        self.weight.text = ""
        self.owner.text = ""
        self.address.text = ""
        self.ids.mammal.active = False
        self.ids.fish.active = False
        self.ids.amphibians.active = False
        self.ids.mammal_yes.active = False
        self.ids.mammal_no.active = False
        self.ids.venomous_yes.active = False
        self.ids.venomous_no.active = False

    def save(self, dir):
        with open('data.p', 'ab') as fb:
            pickle.dump(dir, fb, protocol=pickle.HIGHEST_PROTOCOL)
        fb.close()


class PrintWindow(Screen):

    def printdata(self):
        with open('data.p', 'rb') as fb:
            try:
                while (True):
                    allinfor = pickle.load(fb)
                    texts = ""+allinfor.get("Pet Name")+" current weights is "+ str(round(self.calweight(allinfor.get("Animal Type"),allinfor.get("Birth Weight"),allinfor.get("Pet DOB")),2)) + " and is " + str(self.calage(allinfor.get("Pet DOB"))) +" days old"
                    self.ids.result.add_widget(Label(text=texts, color=[0, 0, 0, 1]))
            except EOFError:
                pass
            fb.close()

    def calage(self,B):
        Year, Month, Day = map(int, B.split('/'))
        dob = datetime.date(Year, Month, Day)
        age = (dt.now().date() - dob).days
        age = int(age)
        return age

    def calweight(self, animal, weight, dob):
        age = self.calage(dob)
        newweight = float(weight)

        if animal == "Mammal":
            if age < 301:
                current = newweight * (pow((1 + 8 / 100), age // 50))
                return current
            elif age > 300:
                current = newweight * (pow((1 + 8 / 100), 6))
                return current

        if animal == "Fish":
            if age < 361:
                current = newweight * (pow((1 + 4 / 100), age // 90))
                return current
            elif age > 360:
                current = newweight * (pow((1 + 4 / 100), 4))
                return current

        if animal == "Amphibians":
            if age < 361:
                current = newweight * (pow((1 + 5 / 100), age // 120))
                return current

            elif age > 360 and age < 601:
                current = newweight * (pow((1 + 5 / 100), 3)) * (pow((1 + 3 / 100), (age - 360) // 120))
                return current
            elif age > 600:
                current = newweight * (pow((1 + 5 / 100), 3)) * (pow((1 + 3 / 100), 2))
                return current

    def clearn(self):
        self.ids.result.clear_widgets()


class AllWindow(Screen):

    def printall(self):
        with open('data.p', 'rb') as fb:
            try:
                while (True):
                    allinfor = pickle.load(fb)
                    #print(allinfor)
                    texts = str(allinfor)
                    #texts = ""+allinfor
                    self.ids.Allresult.add_widget(Label(text=texts,  font_size = '9dp', color=[0, 0, 0, 1]))
            except EOFError:
                pass
            fb.close()

    def clearn(self):
        self.ids.Allresult.clear_widgets()


class WindowManager(ScreenManager):
    pass


class Poperror():

    def invalidLogin(self):
        pop = Popup(title='Invalid Login',
                    content=Label(text='Invalid username or password.'),
                    size_hint=(None, None), size=(400, 400))
        pop.open()

    def invalidForm(self):
        pop = Popup(title='Invalid Form',
                    content=Label(text='Please fill in all inputs with valid information.'),
                    size_hint=(None, None), size=(400, 400))

        pop.open()

    def invalidInfo(self):
        pop = Popup(title='Invalid Information',
                    content=Label(text='Your user name or email does not match our record'),
                    size_hint=(None, None), size=(400, 400))

        pop.open()

    def invalidValue(self):
        pop = Popup(title='Invalid Information',
                    content=Label(text='You have input invalid data type, please check it'),
                    size_hint=(None, None), size=(400, 400))

        pop.open()


kv = Builder.load_file("my.kv")

Window.clearcolor = (0.34, 0.3, 0.42, 0.3)
WM = WindowManager()
Users = UserDate("User.txt")

screens = [CreateWindow(name="Create"), LoginWindow(name="Login"),ForgetWindow(name="Forget"),MianWindow(name="Main"),AddWindow(name="Add"),PrintWindow(name ="Print"),AllWindow(name = "All") ]
for screen in screens:
    WM.add_widget(screen)

WM.current = "Login"

class MyApp(App):
    def build(self):
        return WM

def main():
    MyApp().run()

if __name__ == "__main__":
     main()