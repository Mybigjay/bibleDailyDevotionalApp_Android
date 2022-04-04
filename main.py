
import kivy
import kivymd

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
#from database import DataBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

from kivy.uix.scrollview import ScrollView

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivymd.uix.button import MDRoundFlatButton
from kivy.graphics import Rectangle, Color
from kivy.uix.button import ButtonBehavior
from kivy.properties import BooleanProperty
from kivy.properties import NumericProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.label import Label
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior


#import sqlite3
#Window.clearcolor = (1,1,1,1)
#Window.size = (300,100)


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)


    def loginBtn(self):
        self


    def JanuaryBtn(self):

        sm.current = "Januarycreate"

    def FebruaryBtn(self):

        sm.current = "Februarycreate"

    def MarchBtn(self):

        sm.current = "Marchcreate"

    def AprilBtn(self):

        sm.current = "Aprilcreate"

    def MayBtn(self):

        sm.current = "Maycreate"
    def JuneBtn(self):

        sm.current = "Junecreate"

    def JulyBtn(self):

        sm.current = "Julycreate"

    def AugustBtn(self):

        sm.current = "Augustcreate"

    def SeptemberBtn(self):

        sm.current = "Septembercreate"

    def OctoberBtn(self):

        sm.current = "Octobercreate"

    def NovemberBtn(self):

        sm.current = "Novembercreate"

    def DecemberBtn(self):

        sm.current = "Decembercreate"



class WindowManager(ScreenManager):
    pass
class WindowManagerFeb(ScreenManager):
    pass


class JanuaryCreateWindow(Screen):
    pass

class circularButton(ButtonBehavior, Label):
    pass
Build_Grace = Builder.load_file('my.kv')


class MainApp(BoxLayout):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGrey"
        return Build_Grace

class ResizableDraggablePicture(BoxLayout):
    def on_touch_down(self, touch):
        # Override Scatter's `on_touch_down` behavior for mouse scroll
        if touch.is_mouse_scrolling:
            factor = None
            if touch.button == 'scrolldown':
                if self.scale < self.scale_max:
                    factor = 1.1
            elif touch.button == 'scrollup':
                if self.scale > self.scale_min:
                    factor = 1 / 1.1
            if factor is not None:
                self.apply_transform(Matrix().scale(factor, factor, factor),
                                     anchor=touch.pos)

class JanuaryCreateWindow(Screen):

    email = ObjectProperty(None)
    password = ObjectProperty(None)



    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""



    def JanuaryWeek1Btn(self):

        sm.current = "Januaryweek1"

    def JanuaryWeek2Btn(self):

        sm.current = "Januaryweek2"

    def JanuaryWeek3Btn(self):

        sm.current = "Januaryweek3"

    def JanuaryWeek4Btn(self):

        sm.current = "Januaryweek4"

    def JanuaryWeek5Btn(self):

        sm.current = "Januaryweek5"


"""  January week1"""
class Januaryweek1Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)




    def Januarycreate(self):
        self.reset()
        sm.current = "Januarycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def January1Btn(self):

        sm.current = "January1"

    def January2Btn(self):

        sm.current = "January2"
    def January3Btn(self):

        sm.current = "January3"
    def January4Btn(self):

        sm.current = "January4"
    def January5Btn(self):

        sm.current = "January5"
    def January6Btn(self):

        sm.current = "January6"
    def January7Btn(self):

        sm.current = "January7"


"""  January 1"""
class January1Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Januaryweek1(self):

        sm.current = "Januaryweek1"



    def login(self):

        sm.current = "login"

    def showJanuary1(self):
        with open("January1.txt", "r") as f:
            return (f.read())

"""  January 2"""
class January2Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)




    def Januaryweek1(self):

        sm.current = "Januaryweek1"



    def login(self):

        sm.current = "login"

    def showJanuary2(self):
        with open("January2.txt", "r") as f:
            return (f.read())

"""  January 3"""
class January3Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)




    def Januaryweek1(self):

        sm.current = "Januaryweek1"



    def login(self):

        sm.current = "login"

    def showJanuary3(self):
        with open("January3.txt", "r") as f:
            return (f.read())


"""  January 4"""
class January4Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)




    def Januaryweek1(self):

        sm.current = "Januaryweek1"



    def login(self):

        sm.current = "login"

    def showJanuary4(self):
        with open("January4.txt", "r") as f:
            return (f.read())

"""  January 5"""
class January5Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()

    def Januaryweek1(self):

        sm.current = "Januaryweek1"



    def login(self):

        sm.current = "login"

    def showJanuary5(self):
        with open("January5.txt", "r") as f:
            return (f.read())

"""  January 6"""
class January6Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()

    def Januaryweek1(self):

        sm.current = "Januaryweek1"



    def login(self):

        sm.current = "login"

    def showJanuary6(self):
        with open("January6.txt", "r") as f:
            return (f.read())

"""  January 7"""
class January7Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()


    def login(self):

        sm.current = "login"

    def showJanuary7(self):
        with open("January7.txt", "r") as f:
            return (f.read())

"""  January week2"""
class Januaryweek2Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()

    def Januarycreate(self):
        self.reset()
        sm.current = "Januarycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def January8Btn(self):

        sm.current = "January8"

    def January9Btn(self):

        sm.current = "January9"
    def January10Btn(self):

        sm.current = "January10"
    def January11Btn(self):

        sm.current = "January11"
    def January12Btn(self):

        sm.current = "January12"
    def January13Btn(self):

        sm.current = "January13"
    def January14Btn(self):

        sm.current = "January14"


"""  January 8"""
class January8Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()


    def login(self):

        sm.current = "login"

    def showJanuary8(self):
        with open("January8.txt", "r") as f:
            return (f.read())

"""  January 9"""
class January9Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()



    def login(self):

        sm.current = "login"

    def showJanuary9(self):
        with open("January9.txt", "r") as f:
            return (f.read())

"""  January 10"""
class January10Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()


    def login(self):

        sm.current = "login"

    def showJanuary10(self):
        with open("January10.txt", "r") as f:
            return (f.read())

"""  January 11"""
class January11Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()


    def login(self):

        sm.current = "login"

    def showJanuary11(self):
        with open("January11.txt", "r") as f:
            return (f.read())

"""  January 12"""
class January12Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()


    def login(self):

        sm.current = "login"

    def showJanuary12(self):
        with open("January12.txt", "r") as f:
            return (f.read())

"""  January 13"""
class January13Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()


    def login(self):

        sm.current = "login"

    def showJanuary13(self):
        with open("January13.txt", "r") as f:
            return (f.read())

"""  January 14"""
class January14Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()



    def login(self):

        sm.current = "login"

    def showJanuary14(self):
        with open("January14.txt", "r") as f:
            return (f.read())

"""  January week3"""
class Januaryweek3Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()

    def Januarycreate(self):
        self.reset()
        sm.current = "Januarycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def January15Btn(self):

        sm.current = "January15"

    def January16Btn(self):

        sm.current = "January16"
    def January17Btn(self):

        sm.current = "January17"
    def January18Btn(self):

        sm.current = "January18"
    def January19Btn(self):

        sm.current = "January19"
    def January20Btn(self):

        sm.current = "January20"
    def January21Btn(self):

        sm.current = "January21"

"""  January 15"""
class January15Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()

    def Januaryweek3(self):

        sm.current = "Januaryweek3"



    def login(self):

        sm.current = "login"

    def showJanuary15(self):
        with open("January15.txt", "r") as f:
            return (f.read())

"""  January 16"""
class January16Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()

    def Januaryweek3(self):

        sm.current = "Januaryweek3"



    def login(self):

        sm.current = "login"

    def showJanuary16(self):
        with open("January16.txt", "r") as f:
            return (f.read())

"""  January 17"""
class January17Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()

    def Januaryweek3(self):

        sm.current = "Januaryweek3"



    def login(self):

        sm.current = "login"

    def showJanuary17(self):
        with open("January17.txt", "r") as f:
            return (f.read())

"""  January 18"""
class January18Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()

    def Januaryweek3(self):

        sm.current = "Januaryweek3"



    def login(self):

        sm.current = "login"

    def showJanuary18(self):
        with open("January18.txt", "r") as f:
            return (f.read())

"""  January 19"""
class January19Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()

    def Januaryweek3(self):

        sm.current = "Januaryweek3"



    def login(self):

        sm.current = "login"

    def showJanuary19(self):
        with open("January19.txt", "r") as f:
            return (f.read())

"""  January 20"""
class January20Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()

    def Januaryweek3(self):

        sm.current = "Januaryweek3"



    def login(self):

        sm.current = "login"

    def showJanuary20(self):
        with open("January20.txt", "r") as f:
            return (f.read())

"""  January 21"""
class January21Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()

    def Januaryweek3(self):

        sm.current = "Januaryweek3"



    def login(self):

        sm.current = "login"

    def showJanuary21(self):
        with open("January21.txt", "r") as f:
            return (f.read())

"""  January week4"""
class Januaryweek4Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()

    def Januarycreate(self):
        self.reset()
        sm.current = "Januarycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def January22Btn(self):

        sm.current = "January22"

    def January23Btn(self):

        sm.current = "January23"
    def January24Btn(self):

        sm.current = "January24"
    def January25Btn(self):

        sm.current = "January25"
    def January26Btn(self):

        sm.current = "January26"
    def January27Btn(self):

        sm.current = "January27"
    def January28Btn(self):

        sm.current = "January28"

"""  January 22"""
class January22Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()

    def Januaryweek4(self):

        sm.current = "Januaryweek4"



    def login(self):

        sm.current = "login"

    def showJanuary22(self):
        with open("January22.txt", "r") as f:
            return (f.read())

"""  January 23"""
class January23Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()

    def Januaryweek4(self):

        sm.current = "Januaryweek4"



    def login(self):

        sm.current = "login"

    def showJanuary23(self):
        with open("January23.txt", "r") as f:
            return (f.read())

"""  January 24"""
class January24Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()

    def Januaryweek4(self):

        sm.current = "Januaryweek4"



    def login(self):

        sm.current = "login"

    def showJanuary24(self):
        with open("January24.txt", "r") as f:
            return (f.read())

"""  January 25"""
class January25Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()

    def Januaryweek4(self):

        sm.current = "Januaryweek4"



    def login(self):

        sm.current = "login"

    def showJanuary25(self):
        with open("January25.txt", "r") as f:
            return (f.read())

"""  January 26"""
class January26Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()

    def Januaryweek4(self):

        sm.current = "Januaryweek4"



    def login(self):

        sm.current = "login"

    def showJanuary26(self):
        with open("January26.txt", "r") as f:
            return (f.read())

"""  January 27"""
class January27Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()

    def Januaryweek4(self):

        sm.current = "Januaryweek4"



    def login(self):

        sm.current = "login"

    def showJanuary27(self):
        with open("January27.txt", "r") as f:
            return (f.read())

"""  January 28"""
class January28Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()

    def Januaryweek4(self):

        sm.current = "Januaryweek4"



    def login(self):

        sm.current = "login"

    def showJanuary28(self):
        with open("January28.txt", "r") as f:
            return (f.read())

"""  January week5"""
class Januaryweek5Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()

    def Januarycreate(self):
        self.reset()
        sm.current = "Januarycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def January29Btn(self):

        sm.current = "January29"

    def January30Btn(self):

        sm.current = "January30"
    def January31Btn(self):

        sm.current = "January31"

"""  January 29"""
class January29Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()

    def Januaryweek5(self):

        sm.current = "Januaryweek5"



    def login(self):

        sm.current = "login"

    def showJanuary29(self):
        with open("January29.txt", "r") as f:
            return (f.read())

"""  January 30"""
class January30Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()

    def Januaryweek5(self):

        sm.current = "Januaryweek5"



    def login(self):

        sm.current = "login"

    def showJanuary30(self):
        with open("January30.txt", "r") as f:
            return (f.read())

"""  January 31"""
class January31Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Januarycreate"

        else:
            invalidForm()

    def Januaryweek5(self):

        sm.current = "Januaryweek5"



    def login(self):

        sm.current = "login"

    def showJanuary31(self):
        with open("January31.txt", "r") as f:
            return (f.read())

class FebruaryCreateWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "login"

        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


    def FebruaryWeek5Btn(self):

        sm.current = "Februaryweek5"

    def FebruaryWeek6Btn(self):

        sm.current = "week6"

    def FebruaryWeek7Btn(self):

        sm.current = "week7"

    def FebruaryWeek8Btn(self):

        sm.current = "week8"

    def FebruaryWeek9Btn(self):

        sm.current = "week9"




"""  February week5"""
class Februaryweek5Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def Februarycreate(self):
        self.reset()
        sm.current = "Februarycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def February1Btn(self):

        sm.current = "February1"

    def February2Btn(self):

        sm.current = "February2"
    def February3Btn(self):

        sm.current = "February3"
    def February4Btn(self):

        sm.current = "February4"

"""  February 1"""
class February1Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def Februaryweek5(self):

        sm.current = "Februaryweek5"



    def login(self):

        sm.current = "login"

    def showFebruary1(self):
        with open("February1.txt", "r") as f:
            return (f.read())



"""  February 2"""
class February2Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def Februaryweek5(self):

        sm.current = "Februaryweek5"



    def login(self):

        sm.current = "login"

    def showFebruary2(self):
        with open("February2.txt", "r") as f:
            return (f.read())

"""  February 3"""
class February3Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def Februaryweek5(self):

        sm.current = "Februaryweek5"



    def login(self):

        sm.current = "login"

    def showFebruary3(self):
        with open("February3.txt", "r") as f:
            return (f.read())

"""  February 4"""
class February4Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def Februaryweek5(self):

        sm.current = "Februaryweek5"



    def login(self):

        sm.current = "login"

    def showFebruary4(self):
        with open("February4.txt", "r") as f:
            return (f.read())


"""  week6"""
class week6Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def Februarycreate(self):
        self.reset()
        sm.current = "Februarycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"

    def showweek6(self):
        with open("week6.txt", "r") as f:
            return (f.read())


    def February5Btn(self):

        sm.current = "February5"

    def February6Btn(self):

        sm.current = "February6"
    def February7Btn(self):

        sm.current = "February7"
    def February8Btn(self):

        sm.current = "February8"

    def February9Btn(self):

        sm.current = "February9"

    def February10Btn(self):

        sm.current = "February10"

    def February11Btn(self):

        sm.current = "February11"

"""  February 5"""
class February5Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def week6(self):

        sm.current = "week6"



    def login(self):

        sm.current = "login"

    def showFebruary5(self):
        with open("February5.txt", "r") as f:
            return (f.read())

"""  February 6"""
class February6Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def week6(self):

        sm.current = "week6"



    def login(self):

        sm.current = "login"

    def showFebruary6(self):
        with open("February6.txt", "r") as f:
            return (f.read())



"""  February 7"""
class February7Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def week6(self):

        sm.current = "week6"



    def login(self):

        sm.current = "login"

    def showFebruary7(self):
        with open("February7.txt", "r") as f:
            return (f.read())

"""  February 8"""
class February8Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def week6(self):

        sm.current = "week6"



    def login(self):

        sm.current = "login"

    def showFebruary8(self):
        with open("February8.txt", "r") as f:
            return (f.read())


"""  February 9"""
class February9Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def week6(self):

        sm.current = "week6"



    def login(self):

        sm.current = "login"

    def showFebruary9(self):
        with open("February9.txt", "r") as f:
            return (f.read())


"""  February 10"""
class February10Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def week6(self):

        sm.current = "week6"



    def login(self):

        sm.current = "login"

    def showFebruary10(self):
        with open("February10.txt", "r") as f:
            return (f.read())


"""  February 11"""
class February11Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def week6(self):

        sm.current = "week6"



    def login(self):

        sm.current = "login"

    def showFebruary11(self):
        with open("February11.txt", "r") as f:
            return (f.read())


"""  week7"""
class week7Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def Februarycreate(self):
        self.reset()
        sm.current = "Februarycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def February12Btn(self):

        sm.current = "February12"

    def February13Btn(self):

        sm.current = "February13"
    def February14Btn(self):

        sm.current = "February14"
    def February15Btn(self):

        sm.current = "February15"

    def February16Btn(self):

        sm.current = "February16"

    def February17Btn(self):

        sm.current = "February17"

    def February18Btn(self):

        sm.current = "February18"

"""  February 12"""
class February12Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def week7(self):

        sm.current = "week7"



    def login(self):

        sm.current = "login"

    def showFebruary12(self):
        with open("February12.txt", "r") as f:
            return (f.read())

"""  February 13"""
class February13Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def week7(self):

        sm.current = "week7"



    def login(self):

        sm.current = "login"

    def showFebruary13(self):
        with open("February13.txt", "r") as f:
            return (f.read())

"""  February 14"""
class February14Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def week7(self):

        sm.current = "week7"



    def login(self):

        sm.current = "login"

    def showFebruary14(self):
        with open("February14.txt", "r") as f:
            return (f.read())

"""  February 15"""
class February15Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def week7(self):

        sm.current = "week7"



    def login(self):

        sm.current = "login"

    def showFebruary15(self):
        with open("February15.txt", "r") as f:
            return (f.read())

"""  February 16"""
class February16Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def week7(self):

        sm.current = "week7"



    def login(self):

        sm.current = "login"

    def showFebruary16(self):
        with open("February16.txt", "r") as f:
            return (f.read())


"""  February 16"""
class February16Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def week7(self):

        sm.current = "week7"



    def login(self):

        sm.current = "login"

    def showFebruary16(self):
        with open("February16.txt", "r") as f:
            return (f.read())

"""  February 17"""
class February17Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def week7(self):

        sm.current = "week7"



    def login(self):

        sm.current = "login"

    def showFebruary17(self):
        with open("February17.txt", "r") as f:
            return (f.read())

"""  February 18"""
class February18Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def week7(self):

        sm.current = "week7"



    def login(self):

        sm.current = "login"

    def showFebruary18(self):
        with open("February18.txt", "r") as f:
            return (f.read())

"""  week8"""
class week8Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def Februarycreate(self):
        self.reset()
        sm.current = "Februarycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def February19Btn(self):

        sm.current = "February19"

    def February20Btn(self):

        sm.current = "February20"
    def February21Btn(self):

        sm.current = "February21"
    def February22Btn(self):

        sm.current = "February22"

    def February23Btn(self):

        sm.current = "February23"

    def February24Btn(self):

        sm.current = "February24"

    def February25Btn(self):

        sm.current = "February25"


"""  February 19"""
class February19Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def week8(self):

        sm.current = "week8"



    def login(self):

        sm.current = "login"

    def showFebruary19(self):
        with open("February19.txt", "r") as f:
            return (f.read())

"""  February 20"""
class February20Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def week8(self):

        sm.current = "week8"



    def login(self):

        sm.current = "login"

    def showFebruary20(self):
        with open("February20.txt", "r") as f:
            return (f.read())


"""  February 21"""
class February21Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def week8(self):

        sm.current = "week8"



    def login(self):

        sm.current = "login"

    def showFebruary21(self):
        with open("February21.txt", "r") as f:
            return (f.read())


"""  February 22"""
class February22Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def week8(self):

        sm.current = "week8"



    def login(self):

        sm.current = "login"

    def showFebruary22(self):
        with open("February22.txt", "r") as f:
            return (f.read())

"""  February 23"""
class February23Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def week8(self):

        sm.current = "week8"



    def login(self):

        sm.current = "login"

    def showFebruary23(self):
        with open("February23.txt", "r") as f:
            return (f.read())

"""  February 24"""
class February24Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def week8(self):

        sm.current = "week8"



    def login(self):

        sm.current = "login"

    def showFebruary24(self):
        with open("February24.txt", "r") as f:
            return (f.read())

"""  February 25"""
class February25Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def week8(self):

        sm.current = "week8"



    def login(self):

        sm.current = "login"

    def showFebruary25(self):
        with open("February25.txt", "r") as f:
            return (f.read())

"""  February 26"""
class February26Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def week9(self):

        sm.current = "week9"



    def login(self):

        sm.current = "login"

    def showFebruary26(self):
        with open("February26.txt", "r") as f:
            return (f.read())


"""  February 27"""
class February27Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def week9(self):

        sm.current = "week9"



    def login(self):

        sm.current = "login"

    def showFebruary27(self):
        with open("February27.txt", "r") as f:
            return (f.read())

"""  February 28"""
class February28Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def week9(self):

        sm.current = "week9"



    def login(self):

        sm.current = "login"

    def showFebruary28(self):
        with open("February28.txt", "r") as f:
            return (f.read())


"""  February week9"""
class week9Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Februarycreate"

        else:
            invalidForm()

    def Februarycreate(self):
        self.reset()
        sm.current = "Februarycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"

    def showweek9(self):
        with open("week9.txt", "r") as f:
            return (f.read())


    def February26Btn(self):

        sm.current = "February26"

    def February27Btn(self):

        sm.current = "February27"
    def February28Btn(self):

        sm.current = "February28"

""" MARCH"""
class MarchCreateWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "login"

        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


    def MarchWeek9Btn(self):

        sm.current = "Marchweek9"

    def MarchWeek10Btn(self):

        sm.current = "week10"

    def MarchWeek11Btn(self):

        sm.current = "week11"

    def MarchWeek12Btn(self):

        sm.current = "week12"

    def MarchWeek13Btn(self):

        sm.current = "week13"



"""  March week9"""
class Marchweek9Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def Marchcreate(self):
        self.reset()
        sm.current = "Marchcreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"



    def March1Btn(self):

        sm.current = "March1"

    def March2Btn(self):

        sm.current = "March2"
    def March3Btn(self):

        sm.current = "March3"
    def March4Btn(self):

        sm.current = "March4"

"""  March 1"""
class March1Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def Marchweek9(self):

        sm.current = "Marchweek9"



    def login(self):

        sm.current = "login"

    def showMarch1(self):
        with open("March1.txt", "r") as f:
            return (f.read())

"""  March 2"""
class March2Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def Marchweek9(self):

        sm.current = "Marchweek9"



    def login(self):

        sm.current = "login"

    def showMarch2(self):
        with open("March2.txt", "r") as f:
            return (f.read())


"""  March 3"""
class March3Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def Marchweek9(self):

        sm.current = "Marchweek9"



    def login(self):

        sm.current = "login"

    def showMarch3(self):
        with open("March3.txt", "r") as f:
            return (f.read())


"""  March 4"""
class March4Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def Marchweek9(self):

        sm.current = "Marchweek9"



    def login(self):

        sm.current = "login"

    def showMarch4(self):
        with open("March4.txt", "r") as f:
            return (f.read())

"""  March week10"""
class week10Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def Marchcreate(self):
        self.reset()
        sm.current = "Marchcreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def March5Btn(self):

        sm.current = "March5"

    def March6Btn(self):

        sm.current = "March6"

    def March7Btn(self):

        sm.current = "March7"

    def March8Btn(self):

        sm.current = "March8"

    def March9Btn(self):

        sm.current = "March9"
    def March10Btn(self):

        sm.current = "March10"
    def March11Btn(self):

        sm.current = "March11"

"""  March 5"""
class March5Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week10(self):

        sm.current = "week10"



    def login(self):

        sm.current = "login"

    def showMarch5(self):
        with open("March5.txt", "r") as f:
            return (f.read())

"""  March 6"""
class March6Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week10(self):

        sm.current = "week10"



    def login(self):

        sm.current = "login"

    def showMarch6(self):
        with open("March6.txt", "r") as f:
            return (f.read())

"""  March 7"""
class March7Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week10(self):

        sm.current = "week10"



    def login(self):

        sm.current = "login"

    def showMarch7(self):
        with open("March7.txt", "r") as f:
            return (f.read())

"""  March 8"""
class March8Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week10(self):

        sm.current = "week10"



    def login(self):

        sm.current = "login"

    def showMarch8(self):
        with open("March8.txt", "r") as f:
            return (f.read())

"""  March 9"""
class March9Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week10(self):

        sm.current = "week10"



    def login(self):

        sm.current = "login"

    def showMarch9(self):
        with open("March9.txt", "r") as f:
            return (f.read())

"""  March 10"""
class March10Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week10(self):

        sm.current = "week10"



    def login(self):

        sm.current = "login"

    def showMarch10(self):
        with open("March10.txt", "r") as f:
            return (f.read())

"""  March 11"""
class March11Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week10(self):

        sm.current = "week10"



    def login(self):

        sm.current = "login"

    def showMarch11(self):
        with open("March11.txt", "r") as f:
            return (f.read())


"""  March week11"""
class week11Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def Marchcreate(self):
        self.reset()
        sm.current = "Marchcreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def March12Btn(self):

        sm.current = "March12"

    def March13Btn(self):

        sm.current = "March13"
    def March14Btn(self):

        sm.current = "March14"
    def March15Btn(self):

        sm.current = "March15"

    def March16Btn(self):

        sm.current = "March16"

    def March17Btn(self):

        sm.current = "March17"
    def March18Btn(self):

        sm.current = "March18"



"""  March 12"""
class March12Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week11(self):

        sm.current = "week11"



    def login(self):

        sm.current = "login"

    def showMarch12(self):
        with open("March12.txt", "r") as f:
            return (f.read())

"""  March 13"""
class March13Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week11(self):

        sm.current = "week11"



    def login(self):

        sm.current = "login"

    def showMarch13(self):
        with open("March13.txt", "r") as f:
            return (f.read())

"""  March 14"""
class March14Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week11(self):

        sm.current = "week11"



    def login(self):

        sm.current = "login"

    def showMarch14(self):
        with open("March14.txt", "r") as f:
            return (f.read())

"""  March 15"""
class March15Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week11(self):

        sm.current = "week11"



    def login(self):

        sm.current = "login"

    def showMarch15(self):
        with open("March15.txt", "r") as f:
            return (f.read())

"""  March 16"""
class March16Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week11(self):

        sm.current = "week11"



    def login(self):

        sm.current = "login"

    def showMarch16(self):
        with open("March16.txt", "r") as f:
            return (f.read())

"""  March 17"""
class March17Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week11(self):

        sm.current = "week11"



    def login(self):

        sm.current = "login"

    def showMarch17(self):
        with open("March17.txt", "r") as f:
            return (f.read())

"""  March 18"""
class March18Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week11(self):

        sm.current = "week11"



    def login(self):

        sm.current = "login"

    def showMarch18(self):
        with open("March18.txt", "r") as f:
            return (f.read())


"""  March week12"""
class week12Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def Marchcreate(self):
        self.reset()
        sm.current = "Marchcreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def March19Btn(self):

        sm.current = "March19"

    def March20Btn(self):

        sm.current = "March20"
    def March21Btn(self):

        sm.current = "March21"
    def March22Btn(self):

        sm.current = "March22"

    def March23Btn(self):

        sm.current = "March23"

    def March24Btn(self):

        sm.current = "March24"
    def March25Btn(self):

        sm.current = "March25"


"""  March 19"""
class March19Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week12(self):

        sm.current = "week12"



    def login(self):

        sm.current = "login"

    def showMarch19(self):
        with open("March19.txt", "r") as f:
            return (f.read())

"""  March 20"""
class March20Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week12(self):

        sm.current = "week12"



    def login(self):

        sm.current = "login"

    def showMarch20(self):
        with open("March20.txt", "r") as f:
            return (f.read())

"""  March 21"""
class March21Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week12(self):

        sm.current = "week12"



    def login(self):

        sm.current = "login"

    def showMarch21(self):
        with open("March21.txt", "r") as f:
            return (f.read())



"""  March 22"""
class March22Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week12(self):

        sm.current = "week12"



    def login(self):

        sm.current = "login"

    def showMarch22(self):
        with open("March22.txt", "r") as f:
            return (f.read())


"""  March 23"""
class March23Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week12(self):

        sm.current = "week12"



    def login(self):

        sm.current = "login"

    def showMarch23(self):
        with open("March23.txt", "r") as f:
            return (f.read())


"""  March 24"""
class March24Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week12(self):

        sm.current = "week12"



    def login(self):

        sm.current = "login"

    def showMarch24(self):
        with open("March24.txt", "r") as f:
            return (f.read())

"""  March 25"""
class March25Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week12(self):

        sm.current = "week12"



    def login(self):

        sm.current = "login"

    def showMarch25(self):
        with open("March25.txt", "r") as f:
            return (f.read())

"""  March week13"""
class week13Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def Marchcreate(self):
        self.reset()
        sm.current = "Marchcreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def March26Btn(self):

        sm.current = "March26"

    def March27Btn(self):

        sm.current = "March27"
    def March28Btn(self):

        sm.current = "March28"
    def March29Btn(self):

        sm.current = "March29"

    def March30Btn(self):

        sm.current = "March30"

    def March31Btn(self):

        sm.current = "March31"


"""  March 26"""
class March26Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week13(self):

        sm.current = "week13"



    def login(self):

        sm.current = "login"

    def showMarch26(self):
        with open("March26.txt", "r") as f:
            return (f.read())

"""  March 27"""
class March27Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week13(self):

        sm.current = "week13"



    def login(self):

        sm.current = "login"

    def showMarch27(self):
        with open("March27.txt", "r") as f:
            return (f.read())

"""  March 28"""
class March28Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week13(self):

        sm.current = "week13"



    def login(self):

        sm.current = "login"

    def showMarch28(self):
        with open("March28.txt", "r") as f:
            return (f.read())

"""  March 29"""
class March29Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week13(self):

        sm.current = "week13"



    def login(self):

        sm.current = "login"

    def showMarch29(self):
        with open("March29.txt", "r") as f:
            return (f.read())

"""  March 30"""
class March30Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week13(self):

        sm.current = "week13"



    def login(self):

        sm.current = "login"

    def showMarch30(self):
        with open("March30.txt", "r") as f:
            return (f.read())

"""  March 31"""
class March31Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Marchcreate"

        else:
            invalidForm()

    def week13(self):

        sm.current = "week13"



    def login(self):

        sm.current = "login"

    def showMarch31(self):
        with open("March31.txt", "r") as f:
            return (f.read())

""" APRIL"""
class AprilCreateWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)




    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


    def AprilWeek13Btn(self):

        sm.current = "Aprilweek13"

    def AprilWeek14Btn(self):

        sm.current = "week14"

    def AprilWeek15Btn(self):

        sm.current = "week15"

    def AprilWeek16Btn(self):

        sm.current = "week16"

    def AprilWeek17Btn(self):

        sm.current = "week17"

    def AprilWeek18Btn(self):

        sm.current = "week18"


"""  April week13"""
class Aprilweek13Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)




    def Aprilcreate(self):
        self.reset()
        sm.current = "Aprilcreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def April1Btn(self):

        sm.current = "April1"





"""  April 1"""
class April1Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)





    def Aprilweek13(self):

        sm.current = "Aprilweek13"



    def login(self):

        sm.current = "login"

    def showApril1(self):
        with open("April1.txt", "r") as f:
            return (f.read())


"""  April week14"""
class week14Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Aprilcreate"

        else:
            invalidForm()

    def Aprilcreate(self):
        self.reset()
        sm.current = "Aprilcreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def April2Btn(self):

        sm.current = "April2"

    def April3Btn(self):

        sm.current = "April3"
    def April4Btn(self):

        sm.current = "April4"
    def April5Btn(self):

        sm.current = "April5"

    def April6Btn(self):

        sm.current = "April6"

    def April7Btn(self):

        sm.current = "April7"

    def April8Btn(self):

        sm.current = "April8"


"""  April 2"""
class April2Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Aprilcreate"

        else:
            invalidForm()

    def week14(self):

        sm.current = "week14"



    def login(self):

        sm.current = "login"

    def showApril2(self):
        with open("April2.txt", "r") as f:
            return (f.read())


"""  April 3"""
class April3Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Aprilcreate"

        else:
            invalidForm()

    def week14(self):

        sm.current = "week14"



    def login(self):

        sm.current = "login"

    def showApril3(self):
        with open("April3.txt", "r") as f:
            return (f.read())


"""  April 4"""
class April4Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Aprilcreate"

        else:
            invalidForm()

    def week14(self):

        sm.current = "week14"



    def login(self):

        sm.current = "login"

    def showApril4(self):
        with open("April4.txt", "r") as f:
            return (f.read())


"""  April 5"""
class April5Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Aprilcreate"

        else:
            invalidForm()

    def week14(self):

        sm.current = "week14"



    def login(self):

        sm.current = "login"

    def showApril5(self):
        with open("April5.txt", "r") as f:
            return (f.read())


"""  April 6"""
class April6Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Aprilcreate"

        else:
            invalidForm()

    def week14(self):

        sm.current = "week14"



    def login(self):

        sm.current = "login"

    def showApril6(self):
        with open("April6.txt", "r") as f:
            return (f.read())



"""  April 7"""
class April7Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Aprilcreate"

        else:
            invalidForm()

    def week14(self):

        sm.current = "week14"



    def login(self):

        sm.current = "login"

    def showApril7(self):
        with open("April7.txt", "r") as f:
            return (f.read())

"""  April 8"""
class April8Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Aprilcreate"

        else:
            invalidForm()

    def week14(self):

        sm.current = "week14"



    def login(self):

        sm.current = "login"

    def showApril8(self):
        with open("April8.txt", "r") as f:
            return (f.read())

"""  April week15"""
class week15Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Aprilcreate"

        else:
            invalidForm()

    def Aprilcreate(self):
        self.reset()
        sm.current = "Aprilcreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"

    def April9Btn(self):

        sm.current = "April9"

    def April10Btn(self):

        sm.current = "April10"
    def April11Btn(self):

        sm.current = "April11"
    def April12Btn(self):

        sm.current = "April12"

    def April13Btn(self):

        sm.current = "April13"

    def April14Btn(self):

        sm.current = "April14"

    def April15Btn(self):

        sm.current = "April15"


"""  April 9"""
class April9Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Aprilcreate"

        else:
            invalidForm()

    def week15(self):

        sm.current = "week15"



    def login(self):

        sm.current = "login"

    def showApril9(self):
        with open("April9.txt", "r") as f:
            return (f.read())


"""  April 10"""
class April10Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Aprilcreate"

        else:
            invalidForm()

    def week15(self):

        sm.current = "week15"



    def login(self):

        sm.current = "login"

    def showApril10(self):
        with open("April10.txt", "r") as f:
            return (f.read())


"""  April 11"""
class April11Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Aprilcreate"

        else:
            invalidForm()

    def week15(self):

        sm.current = "week15"



    def login(self):

        sm.current = "login"

    def showApril11(self):
        with open("April11.txt", "r") as f:
            return (f.read())

"""  April 12"""
class April12Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Aprilcreate"

        else:
            invalidForm()

    def week15(self):

        sm.current = "week15"



    def login(self):

        sm.current = "login"

    def showApril12(self):
        with open("April12.txt", "r") as f:
            return (f.read())



"""  April 13"""
class April13Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Aprilcreate"

        else:
            invalidForm()

    def week15(self):

        sm.current = "week15"



    def login(self):

        sm.current = "login"

    def showApril13(self):
        with open("April13.txt", "r") as f:
            return (f.read())


"""  April 14"""
class April14Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Aprilcreate"

        else:
            invalidForm()

    def week15(self):

        sm.current = "week15"



    def login(self):

        sm.current = "login"

    def showApril14(self):
        with open("April14.txt", "r") as f:
            return (f.read())


"""  April 15"""
class April15Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Aprilcreate"

        else:
            invalidForm()

    def week15(self):

        sm.current = "week15"



    def login(self):

        sm.current = "login"

    def showApril15(self):
        with open("April15.txt", "r") as f:
            return (f.read())


"""  April week16"""
class week16Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Aprilcreate"

        else:
            invalidForm()

    def Aprilcreate(self):
        self.reset()
        sm.current = "Aprilcreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def April16Btn(self):

        sm.current = "April16"

    def April17Btn(self):

        sm.current = "April17"
    def April18Btn(self):

        sm.current = "April18"
    def April19Btn(self):

        sm.current = "April19"

    def April20Btn(self):

        sm.current = "April20"

    def April21Btn(self):

        sm.current = "April21"

    def April22Btn(self):

        sm.current = "April22"

"""  April 16"""
class April16Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Aprilcreate"

        else:
            invalidForm()

    def week16(self):

        sm.current = "week16"



    def login(self):

        sm.current = "login"

    def showApril16(self):
        with open("April16.txt", "r") as f:
            return (f.read())



"""  April 17"""
class April17Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Aprilcreate"

        else:
            invalidForm()

    def week16(self):

        sm.current = "week16"



    def login(self):

        sm.current = "login"

    def showApril17(self):
        with open("April17.txt", "r") as f:
            return (f.read())


"""  April 18"""
class April18Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Aprilcreate"

        else:
            invalidForm()

    def week16(self):

        sm.current = "week16"



    def login(self):

        sm.current = "login"

    def showApril18(self):
        with open("April18.txt", "r") as f:
            return (f.read())



"""  April 19"""
class April19Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Aprilcreate"

        else:
            invalidForm()

    def week16(self):

        sm.current = "week16"



    def login(self):

        sm.current = "login"

    def showApril19(self):
        with open("April19.txt", "r") as f:
            return (f.read())


"""  April 20"""
class April20Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)




    def week16(self):

        sm.current = "week16"



    def login(self):

        sm.current = "login"

    def showApril20(self):
        with open("April20.txt", "r") as f:
            return (f.read())


"""  April 21"""
class April21Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def week16(self):
        sm.current = "week16"

    def login(self):
        sm.current = "login"

    def showApril21(self):
        with open("April21.txt", "r") as f:
            return (f.read())



"""  April 22"""
class April22Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def week16(self):
        sm.current = "week16"

    def login(self):
        sm.current = "login"

    def showApril22(self):
        with open("April22.txt", "r") as f:
            return (f.read())



"""  April week17"""
class week17Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Aprilcreate"

        else:
            invalidForm()

    def Aprilcreate(self):
        self.reset()
        sm.current = "Aprilcreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"

    def April23Btn(self):

        sm.current = "April23"

    def April24Btn(self):

        sm.current = "April24"
    def April25Btn(self):

        sm.current = "April25"
    def April26Btn(self):

        sm.current = "April26"

    def April27Btn(self):

        sm.current = "April27"

    def April28Btn(self):

        sm.current = "April28"

    def April29Btn(self):

        sm.current = "April29"


"""  April 23"""
class April23Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def week17(self):
        sm.current = "week17"

    def login(self):
        sm.current = "login"

    def showApril23(self):
        with open("April23.txt", "r") as f:
            return (f.read())



"""  April 24"""
class April24Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def week17(self):
        sm.current = "week17"

    def login(self):
        sm.current = "login"

    def showApril24(self):
        with open("April24.txt", "r") as f:
            return (f.read())


"""  April 25"""
class April25Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def week17(self):
        sm.current = "week17"

    def login(self):
        sm.current = "login"

    def showApril25(self):
        with open("April25.txt", "r") as f:
            return (f.read())


"""  April 26"""
class April26Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def week17(self):
        sm.current = "week17"

    def login(self):
        sm.current = "login"

    def showApril26(self):
        with open("April26.txt", "r") as f:
            return (f.read())



"""  April 27"""
class April27Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def week17(self):
        sm.current = "week17"

    def login(self):
        sm.current = "login"

    def showApril27(self):
        with open("April27.txt", "r") as f:
            return (f.read())


"""  April 28"""
class April28Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def week17(self):
        sm.current = "week17"

    def login(self):
        sm.current = "login"
    def showApril28(self):
        with open("April28.txt", "r") as f:
            return (f.read())



"""  April 29"""
class April29Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def week17(self):
        sm.current = "week17"

    def login(self):
        sm.current = "login"

    def showApril29(self):
        with open("April29.txt", "r") as f:
            return (f.read())


"""  April week18"""
class week18Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Aprilcreate"

        else:
            invalidForm()

    def Aprilcreate(self):
        self.reset()
        sm.current = "Aprilcreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"

    def April30Btn(self):

        sm.current = "April30"

"""  April 30"""
class April30Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def week18(self):
        sm.current = "week18"

    def login(self):
        sm.current = "login"

    def showApril30(self):
        with open("April30.txt", "r") as f:
            return (f.read())



""" May"""
class MayCreateWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "login"

        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


    def MayWeek18Btn(self):

        sm.current = "Mayweek18"

    def MayWeek19Btn(self):

        sm.current = "Mayweek19"

    def MayWeek20Btn(self):

        sm.current = "Mayweek20"

    def MayWeek21Btn(self):

        sm.current = "Mayweek21"

    def MayWeek22Btn(self):

        sm.current = "Mayweek22"



"""  May week18"""
class Mayweek18Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Maycreate"

        else:
            invalidForm()

    def Maycreate(self):
        self.reset()
        sm.current = "Maycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"

    def showmayweek18(self):
        with open("mayweek18.txt", "r") as f:
            return (f.read())


    def May1Btn(self):

        sm.current = "May1"

    def May2Btn(self):

        sm.current = "May2"
    def May3Btn(self):

        sm.current = "May3"
    def May4Btn(self):

        sm.current = "May4"
    def May5Btn(self):

        sm.current = "May5"
    def May6Btn(self):

        sm.current = "May6"



"""  May 1"""
class May1Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek18(self):
        sm.current = "Mayweek18"

    def login(self):
        sm.current = "login"

    def showMay1(self):
        with open("May1.txt", "r") as f:
            return (f.read())


"""  May 2"""
class May2Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek18(self):
        sm.current = "Mayweek18"

    def login(self):
        sm.current = "login"

    def showMay2(self):
        with open("May2.txt", "r") as f:
            return (f.read())



"""  May 3"""
class May3Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek18(self):
        sm.current = "Mayweek18"

    def login(self):
        sm.current = "login"

    def showMay3(self):
        with open("May3.txt", "r") as f:
            return (f.read())


"""  May 4"""
class May4Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek18(self):
        sm.current = "Mayweek18"

    def login(self):
        sm.current = "login"

    def showMay4(self):
        with open("May4.txt", "r") as f:
            return (f.read())



"""  May 5"""
class May5Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek18(self):
        sm.current = "Mayweek18"

    def login(self):
        sm.current = "login"

    def showMay5(self):
        with open("May5.txt", "r") as f:
            return (f.read())


"""  May 6"""
class May6Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek18(self):
        sm.current = "Mayweek18"

    def login(self):
        sm.current = "login"

    def showMay6(self):
        with open("May6.txt", "r") as f:
            return (f.read())


"""  May week19"""
class Mayweek19Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Maycreate"

        else:
            invalidForm()

    def Maycreate(self):
        self.reset()
        sm.current = "Maycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def May7Btn(self):

        sm.current = "May7"

    def May8Btn(self):

        sm.current = "May8"
    def May9Btn(self):

        sm.current = "May9"
    def May10Btn(self):

        sm.current = "May10"
    def May11Btn(self):

        sm.current = "May11"
    def May12Btn(self):

        sm.current = "May12"
    def May13Btn(self):

        sm.current = "May13"



"""  May 7"""
class May7Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek19(self):
        sm.current = "Mayweek19"

    def login(self):
        sm.current = "login"

    def showMay7(self):
        with open("May7.txt", "r") as f:
            return (f.read())


"""  May 8"""
class May8Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek19(self):
        sm.current = "Mayweek19"

    def login(self):
        sm.current = "login"

    def showMay8(self):
        with open("May8.txt", "r") as f:
            return (f.read())



"""  May 9"""
class May9Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek19(self):
        sm.current = "Mayweek19"

    def login(self):
        sm.current = "login"

    def showMay9(self):
        with open("May9.txt", "r") as f:
            return (f.read())



"""  May 10"""
class May10Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek19(self):
        sm.current = "Mayweek19"

    def login(self):
        sm.current = "login"

    def showMay10(self):
        with open("May10.txt", "r") as f:
            return (f.read())



"""  May 11"""
class May11Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek19(self):
        sm.current = "Mayweek19"

    def login(self):
        sm.current = "login"

    def showMay11(self):
        with open("May11.txt", "r") as f:
            return (f.read())


"""  May 12"""
class May12Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek19(self):
        sm.current = "Mayweek19"

    def login(self):
        sm.current = "login"

    def showMay12(self):
        with open("May12.txt", "r") as f:
            return (f.read())



"""  May 13"""
class May13Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek19(self):
        sm.current = "Mayweek19"

    def login(self):
        sm.current = "login"

    def showMay13(self):
        with open("May13.txt", "r") as f:
            return (f.read())


"""  May week20"""
class Mayweek20Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Maycreate"

        else:
            invalidForm()

    def Maycreate(self):
        self.reset()
        sm.current = "Maycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def May14Btn(self):

        sm.current = "May14"

    def May15Btn(self):

        sm.current = "May15"
    def May16Btn(self):

        sm.current = "May16"
    def May17Btn(self):

        sm.current = "May17"
    def May18Btn(self):

        sm.current = "May18"
    def May19Btn(self):

        sm.current = "May19"
    def May20Btn(self):

        sm.current = "May20"

"""  May 14"""
class May14Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek20(self):
        sm.current = "Mayweek20"

    def login(self):
        sm.current = "login"

    def showMay14(self):
        with open("May14.txt", "r") as f:
            return (f.read())


"""  May 15"""
class May15Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek20(self):
        sm.current = "Mayweek20"

    def login(self):
        sm.current = "login"

    def showMay15(self):
        with open("May15.txt", "r") as f:
            return (f.read())


"""  May 16"""
class May16Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek20(self):
        sm.current = "Mayweek20"

    def login(self):
        sm.current = "login"

    def showMay16(self):
        with open("May16.txt", "r") as f:
            return (f.read())


"""  May 17"""
class May17Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek20(self):
        sm.current = "Mayweek20"

    def login(self):
        sm.current = "login"

    def showMay17(self):
        with open("May17.txt", "r") as f:
            return (f.read())


"""  May 18"""
class May18Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek20(self):
        sm.current = "Mayweek20"

    def login(self):
        sm.current = "login"

    def showMay18(self):
        with open("May18.txt", "r") as f:
            return (f.read())


"""  May 19"""
class May19Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek20(self):
        sm.current = "Mayweek20"

    def login(self):
        sm.current = "login"

    def showMay19(self):
        with open("May19.txt", "r") as f:
            return (f.read())


"""  May 20"""
class May20Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek20(self):
        sm.current = "Mayweek20"

    def login(self):
        sm.current = "login"

    def showMay20(self):
        with open("May20.txt", "r") as f:
            return (f.read())


"""  May week21"""
class Mayweek21Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Maycreate"

        else:
            invalidForm()

    def Maycreate(self):
        self.reset()
        sm.current = "Maycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"



    def May21Btn(self):

        sm.current = "May21"

    def May22Btn(self):

        sm.current = "May22"
    def May23Btn(self):

        sm.current = "May23"
    def May24Btn(self):

        sm.current = "May24"
    def May25Btn(self):

        sm.current = "May25"
    def May26Btn(self):

        sm.current = "May26"
    def May27Btn(self):

        sm.current = "May27"


"""  May 21"""
class May21Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek21(self):
        sm.current = "Mayweek21"

    def login(self):
        sm.current = "login"

    def showMay21(self):
        with open("May21.txt", "r") as f:
            return (f.read())


"""  May 22"""
class May22Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek21(self):
        sm.current = "Mayweek21"

    def login(self):
        sm.current = "login"

    def showMay22(self):
        with open("May22.txt", "r") as f:
            return (f.read())



"""  May 23"""
class May23Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek21(self):
        sm.current = "Mayweek21"

    def login(self):
        sm.current = "login"

    def showMay23(self):
        with open("May23.txt", "r") as f:
            return (f.read())


"""  May 24"""
class May24Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek21(self):
        sm.current = "Mayweek21"

    def login(self):
        sm.current = "login"

    def showMay24(self):
        with open("May24.txt", "r") as f:
            return (f.read())


"""  May 25"""
class May25Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek21(self):
        sm.current = "Mayweek21"

    def login(self):
        sm.current = "login"

    def showMay25(self):
        with open("May25.txt", "r") as f:
            return (f.read())


"""  May 26"""
class May26Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek21(self):
        sm.current = "Mayweek21"

    def login(self):
        sm.current = "login"

    def showMay26(self):
        with open("May26.txt", "r") as f:
            return (f.read())


"""  May 27"""
class May27Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek21(self):
        sm.current = "Mayweek21"

    def login(self):
        sm.current = "login"

    def showMay27(self):
        with open("May27.txt", "r") as f:
            return (f.read())


"""  May week22"""
class Mayweek22Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Maycreate"

        else:
            invalidForm()

    def Maycreate(self):
        self.reset()
        sm.current = "Maycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"



    def May28Btn(self):

        sm.current = "May28"

    def May29Btn(self):

        sm.current = "May29"
    def May30Btn(self):

        sm.current = "May30"
    def May31Btn(self):

        sm.current = "May31"



"""  May 28"""
class May28Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek22(self):
        sm.current = "Mayweek22"

    def login(self):
        sm.current = "login"

    def showMay28(self):
        with open("May28.txt", "r") as f:
            return (f.read())


"""  May 29"""
class May29Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek22(self):
        sm.current = "Mayweek22"

    def login(self):
        sm.current = "login"

    def showMay29(self):
        with open("May29.txt", "r") as f:
            return (f.read())


"""  May 30"""
class May30Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek22(self):
        sm.current = "Mayweek22"

    def login(self):
        sm.current = "login"

    def showMay30(self):
        with open("May30.txt", "r") as f:
            return (f.read())


"""  May 31"""
class May31Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Mayweek22(self):
        sm.current = "Mayweek22"

    def login(self):
        sm.current = "login"

    def showMay31(self):
        with open("May31.txt", "r") as f:
            return (f.read())


""" June"""
class JuneCreateWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "login"

        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


    def JuneWeek22Btn(self):

        sm.current = "Juneweek22"

    def JuneWeek23Btn(self):

        sm.current = "Juneweek23"

    def JuneWeek24Btn(self):

        sm.current = "Juneweek24"

    def JuneWeek25Btn(self):

        sm.current = "Juneweek25"

    def JuneWeek26Btn(self):

        sm.current = "Juneweek26"



"""  June week22"""
class Juneweek22Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Junecreate"

        else:
            invalidForm()

    def Junecreate(self):
        self.reset()
        sm.current = "Junecreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def June1Btn(self):

        sm.current = "June1"

    def June2Btn(self):

        sm.current = "June2"
    def June3Btn(self):

        sm.current = "June3"


"""  June 1"""
class June1Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek22(self):
        sm.current = "Juneweek22"

    def login(self):
        sm.current = "login"

    def showJune1(self):
        with open("June1.txt", "r") as f:
            return (f.read())



"""  June 2"""
class June2Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek22(self):
        sm.current = "Juneweek22"

    def login(self):
        sm.current = "login"

    def showJune2(self):
        with open("June2.txt", "r") as f:
            return (f.read())


"""  June 3"""
class June3Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek22(self):
        sm.current = "Juneweek22"

    def login(self):
        sm.current = "login"

    def showJune3(self):
        with open("June3.txt", "r") as f:
            return (f.read())


"""  June week23"""
class Juneweek23Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Junecreate"

        else:
            invalidForm()

    def Junecreate(self):
        self.reset()
        sm.current = "Junecreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def June4Btn(self):

        sm.current = "June4"

    def June5Btn(self):

        sm.current = "June5"
    def June6Btn(self):

        sm.current = "June6"

    def June7Btn(self):

        sm.current = "June7"

    def June8Btn(self):

        sm.current = "June8"

    def June9Btn(self):

        sm.current = "June9"

    def June10Btn(self):

        sm.current = "June10"



"""  June 4"""
class June4Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek23(self):
        sm.current = "Juneweek23"

    def login(self):
        sm.current = "login"

    def showJune4(self):
        with open("June4.txt", "r") as f:
            return (f.read())


"""  June 5"""
class June5Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek23(self):
        sm.current = "Juneweek23"

    def login(self):
        sm.current = "login"

    def showJune5(self):
        with open("June5.txt", "r") as f:
            return (f.read())


"""  June 6"""
class June6Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek23(self):
        sm.current = "Juneweek23"

    def login(self):
        sm.current = "login"

    def showJune6(self):
        with open("June6.txt", "r") as f:
            return (f.read())


"""  June 7"""
class June7Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek23(self):
        sm.current = "Juneweek23"

    def login(self):
        sm.current = "login"

    def showJune7(self):
        with open("June7.txt", "r") as f:
            return (f.read())


"""  June 8"""
class June8Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek23(self):
        sm.current = "Juneweek23"

    def login(self):
        sm.current = "login"

    def showJune8(self):
        with open("June8.txt", "r") as f:
            return (f.read())


"""  June 9"""
class June9Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek23(self):
        sm.current = "Juneweek23"

    def login(self):
        sm.current = "login"

    def showJune9(self):
        with open("June9.txt", "r") as f:
            return (f.read())


"""  June 10"""
class June10Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek23(self):
        sm.current = "Juneweek23"

    def login(self):
        sm.current = "login"

    def showJune10(self):
        with open("June10.txt", "r") as f:
            return (f.read())



"""  June week24"""
class Juneweek24Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:


                sm.current = "Junecreate"

        else:
            invalidForm()

    def Junecreate(self):
        self.reset()
        sm.current = "Junecreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"



    def June11Btn(self):

        sm.current = "June11"

    def June12Btn(self):

        sm.current = "June12"

    def June13Btn(self):

        sm.current = "June13"

    def June14Btn(self):

        sm.current = "June14"

    def June15Btn(self):

        sm.current = "June15"

    def June16Btn(self):

        sm.current = "June16"

    def June17Btn(self):

        sm.current = "June17"


"""  June 11"""
class June11Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek24(self):
        sm.current = "Juneweek24"

    def login(self):
        sm.current = "login"

    def showJune11(self):
        with open("June11.txt", "r") as f:
            return (f.read())



"""  June 12"""
class June12Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek24(self):
        sm.current = "Juneweek24"

    def login(self):
        sm.current = "login"

    def showJune12(self):
        with open("June12.txt", "r") as f:
            return (f.read())


"""  June 13"""
class June13Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek24(self):
        sm.current = "Juneweek24"

    def login(self):
        sm.current = "login"

    def showJune13(self):
        with open("June13.txt", "r") as f:
            return (f.read())


"""  June 14"""
class June14Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek24(self):
        sm.current = "Juneweek24"

    def login(self):
        sm.current = "login"

    def showJune14(self):
        with open("June14.txt", "r") as f:
            return (f.read())


"""  June 15"""
class June15Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek24(self):
        sm.current = "Juneweek24"

    def login(self):
        sm.current = "login"

    def showJune15(self):
        with open("June15.txt", "r") as f:
            return (f.read())


"""  June 16"""
class June16Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek24(self):
        sm.current = "Juneweek24"

    def login(self):
        sm.current = "login"

    def showJune16(self):
        with open("June16.txt", "r") as f:
            return (f.read())


"""  June 17"""
class June17Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek24(self):
        sm.current = "Juneweek24"

    def login(self):
        sm.current = "login"

    def showJune17(self):
        with open("June17.txt", "r") as f:
            return (f.read())



"""  June week25"""
class Juneweek25Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Junecreate"

        else:
            invalidForm()

    def Junecreate(self):
        self.reset()
        sm.current = "Junecreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def June18Btn(self):

        sm.current = "June18"

    def June19Btn(self):

        sm.current = "June19"

    def June20Btn(self):

        sm.current = "June20"

    def June21Btn(self):

        sm.current = "June21"

    def June22Btn(self):

        sm.current = "June22"

    def June23Btn(self):

        sm.current = "June23"

    def June24Btn(self):

        sm.current = "June24"


"""  June 18"""
class June18Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek25(self):
        sm.current = "Juneweek25"

    def login(self):
        sm.current = "login"

    def showJune18(self):
        with open("June18.txt", "r") as f:
            return (f.read())



"""  June 19"""
class June19Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek25(self):
        sm.current = "Juneweek25"

    def login(self):
        sm.current = "login"

    def showJune19(self):
        with open("June19.txt", "r") as f:
            return (f.read())


"""  June 20"""
class June20Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek25(self):
        sm.current = "Juneweek25"

    def login(self):
        sm.current = "login"

    def showJune20(self):
        with open("June20.txt", "r") as f:
            return (f.read())


"""  June 21"""
class June21Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek25(self):
        sm.current = "Juneweek25"

    def login(self):
        sm.current = "login"

    def showJune21(self):
        with open("June21.txt", "r") as f:
            return (f.read())


"""  June 22"""
class June22Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek25(self):
        sm.current = "Juneweek25"

    def login(self):
        sm.current = "login"

    def showJune22(self):
        with open("June22.txt", "r") as f:
            return (f.read())


"""  June 23"""
class June23Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek25(self):
        sm.current = "Juneweek25"

    def login(self):
        sm.current = "login"

    def showJune23(self):
        with open("June23.txt", "r") as f:
            return (f.read())


"""  June 24"""
class June24Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek25(self):
        sm.current = "Juneweek25"

    def login(self):
        sm.current = "login"

    def showJune24(self):
        with open("June24.txt", "r") as f:
            return (f.read())



"""  June week26"""
class Juneweek26Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Junecreate"

        else:
            invalidForm()

    def Junecreate(self):
        self.reset()
        sm.current = "Junecreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def June25Btn(self):

        sm.current = "June25"

    def June26Btn(self):

        sm.current = "June26"

    def June27Btn(self):

        sm.current = "June27"

    def June27Btn(self):

        sm.current = "June27"

    def June28Btn(self):

        sm.current = "June28"

    def June29Btn(self):

        sm.current = "June29"

    def June30Btn(self):

        sm.current = "June30"


"""  June 25"""
class June25Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek26(self):
        sm.current = "Juneweek26"

    def login(self):
        sm.current = "login"

    def showJune25(self):
        with open("June25.txt", "r") as f:
            return (f.read())


"""  June 26"""
class June26Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek26(self):
        sm.current = "Juneweek26"

    def login(self):
        sm.current = "login"

    def showJune26(self):
        with open("June26.txt", "r") as f:
            return (f.read())



"""  June 27"""
class June27Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek26(self):
        sm.current = "Juneweek26"

    def login(self):
        sm.current = "login"

    def showJune27(self):
        with open("June27.txt", "r") as f:
            return (f.read())



"""  June 28"""
class June28Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek26(self):
        sm.current = "Juneweek26"

    def login(self):
        sm.current = "login"

    def showJune28(self):
        with open("June28.txt", "r") as f:
            return (f.read())


"""  June 29"""
class June29Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek26(self):
        sm.current = "Juneweek26"

    def login(self):
        sm.current = "login"

    def showJune29(self):
        with open("June29.txt", "r") as f:
            return (f.read())



"""  June 30"""
class June30Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Juneweek26(self):
        sm.current = "Juneweek26"

    def login(self):
        sm.current = "login"

    def showJune30(self):
        with open("June30.txt", "r") as f:
            return (f.read())


""" July"""
class JulyCreateWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:



                sm.current = "login"

        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


    def JulyWeek26Btn(self):

        sm.current = "Julyweek26"

    def JulyWeek27Btn(self):

        sm.current = "Julyweek27"

    def JulyWeek28Btn(self):

        sm.current = "Julyweek28"

    def JulyWeek29Btn(self):

        sm.current = "Julyweek29"

    def JulyWeek30Btn(self):

        sm.current = "Julyweek30"

    def JulyWeek31Btn(self):

        sm.current = "Julyweek31"


"""  July week26"""
class Julyweek26Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Julycreate"

        else:
            invalidForm()

    def Julycreate(self):
        self.reset()
        sm.current = "Julycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def July1Btn(self):

        sm.current = "July1"


"""  July 1"""
class July1Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek26(self):
        sm.current = "Julyweek26"

    def login(self):
        sm.current = "login"

    def showJuly1(self):
        with open("July1.txt", "r") as f:
            return (f.read())



"""  July week27"""
class Julyweek27Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Julycreate"

        else:
            invalidForm()

    def Julycreate(self):
        self.reset()
        sm.current = "Julycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"



    def July2Btn(self):

        sm.current = "July2"

    def July3Btn(self):

        sm.current = "July3"

    def July4Btn(self):

        sm.current = "July4"

    def July5Btn(self):

        sm.current = "July5"

    def July6Btn(self):

        sm.current = "July6"

    def July7Btn(self):

        sm.current = "July7"

    def July8Btn(self):

        sm.current = "July8"


"""  July 2"""
class July2Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek27(self):
        sm.current = "Julyweek27"

    def login(self):
        sm.current = "login"

    def showJuly2(self):
        with open("July2.txt", "r") as f:
            return (f.read())



"""  July 3"""
class July3Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek27(self):
        sm.current = "Julyweek27"

    def login(self):
        sm.current = "login"

    def showJuly3(self):
        with open("July3.txt", "r") as f:
            return (f.read())


"""  July 4"""
class July4Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek27(self):
        sm.current = "Julyweek27"

    def login(self):
        sm.current = "login"

    def showJuly4(self):
        with open("July4.txt", "r") as f:
            return (f.read())


"""  July 5"""
class July5Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek27(self):
        sm.current = "Julyweek27"

    def login(self):
        sm.current = "login"

    def showJuly5(self):
        with open("July5.txt", "r") as f:
            return (f.read())


"""  July 6"""
class July6Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek27(self):
        sm.current = "Julyweek27"

    def login(self):
        sm.current = "login"

    def showJuly6(self):
        with open("July6.txt", "r") as f:
            return (f.read())


"""  July 7"""
class July7Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek27(self):
        sm.current = "Julyweek27"

    def login(self):
        sm.current = "login"

    def showJuly7(self):
        with open("July7.txt", "r") as f:
            return (f.read())


"""  July 8"""
class July8Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek27(self):
        sm.current = "Julyweek27"

    def login(self):
        sm.current = "login"

    def showJuly8(self):
        with open("July8.txt", "r") as f:
            return (f.read())



"""  July week28"""
class Julyweek28Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Julycreate"

        else:
            invalidForm()

    def Julycreate(self):
        self.reset()
        sm.current = "Julycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"



    def July9Btn(self):

        sm.current = "July9"

    def July10Btn(self):

        sm.current = "July10"

    def July11Btn(self):

        sm.current = "July11"

    def July12Btn(self):

        sm.current = "July12"


    def July13Btn(self):

        sm.current = "July13"

    def July14Btn(self):

        sm.current = "July14"

    def July15Btn(self):

        sm.current = "July15"




"""  July 9"""
class July9Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek28(self):
        sm.current = "Julyweek28"

    def login(self):
        sm.current = "login"

    def showJuly9(self):
        with open("July9.txt", "r") as f:
            return (f.read())


"""  July 10"""
class July10Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek28(self):
        sm.current = "Julyweek28"

    def login(self):
        sm.current = "login"

    def showJuly10(self):
        with open("July10.txt", "r") as f:
            return (f.read())


"""  July 11"""
class July11Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek28(self):
        sm.current = "Julyweek28"

    def login(self):
        sm.current = "login"

    def showJuly11(self):
        with open("July11.txt", "r") as f:
            return (f.read())


"""  July 12"""
class July12Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek28(self):
        sm.current = "Julyweek28"

    def login(self):
        sm.current = "login"

    def showJuly12(self):
        with open("July12.txt", "r") as f:
            return (f.read())



"""  July 13"""
class July13Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek28(self):
        sm.current = "Julyweek28"

    def login(self):
        sm.current = "login"

    def showJuly13(self):
        with open("July13.txt", "r") as f:
            return (f.read())


"""  July 14"""
class July14Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek28(self):
        sm.current = "Julyweek28"

    def login(self):
        sm.current = "login"

    def showJuly14(self):
        with open("July14.txt", "r") as f:
            return (f.read())



"""  July 15"""
class July15Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek28(self):
        sm.current = "Julyweek28"

    def login(self):
        sm.current = "login"

    def showJuly15(self):
        with open("July15.txt", "r") as f:
            return (f.read())




"""  July week29"""
class Julyweek29Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Julycreate"

        else:
            invalidForm()

    def Julycreate(self):
        self.reset()
        sm.current = "Julycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def July16Btn(self):

        sm.current = "July16"

    def July17Btn(self):

        sm.current = "July17"

    def July18Btn(self):

        sm.current = "July18"

    def July19Btn(self):

        sm.current = "July19"


    def July20Btn(self):

        sm.current = "July20"

    def July21Btn(self):

        sm.current = "July21"

    def July22Btn(self):

        sm.current = "July22"



"""  July 16"""
class July16Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek29(self):
        sm.current = "Julyweek29"

    def login(self):
        sm.current = "login"

    def showJuly16(self):
        with open("July16.txt", "r") as f:
            return (f.read())



"""  July 17"""
class July17Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek29(self):
        sm.current = "Julyweek29"

    def login(self):
        sm.current = "login"

    def showJuly17(self):
        with open("July17.txt", "r") as f:
            return (f.read())


"""  July 18"""
class July18Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek29(self):
        sm.current = "Julyweek29"

    def login(self):
        sm.current = "login"

    def showJuly18(self):
        with open("July18.txt", "r") as f:
            return (f.read())



"""  July 19"""
class July19Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek29(self):
        sm.current = "Julyweek29"

    def login(self):
        sm.current = "login"

    def showJuly19(self):
        with open("July19.txt", "r") as f:
            return (f.read())



"""  July 20"""
class July20Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek29(self):
        sm.current = "Julyweek29"

    def login(self):
        sm.current = "login"

    def showJuly20(self):
        with open("July20.txt", "r") as f:
            return (f.read())


"""  July 21"""
class July21Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek29(self):
        sm.current = "Julyweek29"

    def login(self):
        sm.current = "login"

    def showJuly21(self):
        with open("July21.txt", "r") as f:
            return (f.read())


"""  July 22"""
class July22Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek29(self):
        sm.current = "Julyweek29"

    def login(self):
        sm.current = "login"

    def showJuly22(self):
        with open("July22.txt", "r") as f:
            return (f.read())


"""  July week30"""
class Julyweek30Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Julycreate"

        else:
            invalidForm()

    def Julycreate(self):
        self.reset()
        sm.current = "Julycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"

    def July23Btn(self):

        sm.current = "July23"

    def July24Btn(self):

        sm.current = "July24"

    def July25Btn(self):

        sm.current = "July25"

    def July26Btn(self):

        sm.current = "July26"


    def July27Btn(self):

        sm.current = "July27"

    def July28Btn(self):

        sm.current = "July28"

    def July29Btn(self):

        sm.current = "July29"




"""  July 23"""
class July23Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek30(self):
        sm.current = "Julyweek30"

    def login(self):
        sm.current = "login"

    def showJuly23(self):
        with open("July23.txt", "r") as f:
            return (f.read())


"""  July 24"""
class July24Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek30(self):
        sm.current = "Julyweek30"

    def login(self):
        sm.current = "login"

    def showJuly24(self):
        with open("July24.txt", "r") as f:
            return (f.read())


"""  July 25"""
class July25Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek30(self):
        sm.current = "Julyweek30"

    def login(self):
        sm.current = "login"

    def showJuly25(self):
        with open("July25.txt", "r") as f:
            return (f.read())


"""  July 26"""
class July26Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek30(self):
        sm.current = "Julyweek30"

    def login(self):
        sm.current = "login"

    def showJuly26(self):
        with open("July26.txt", "r") as f:
            return (f.read())


"""  July 27"""
class July27Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek30(self):
        sm.current = "Julyweek30"

    def login(self):
        sm.current = "login"

    def showJuly27(self):
        with open("July27.txt", "r") as f:
            return (f.read())



"""  July 28"""
class July28Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek30(self):
        sm.current = "Julyweek30"

    def login(self):
        sm.current = "login"

    def showJuly28(self):
        with open("July28.txt", "r") as f:
            return (f.read())


"""  July 29"""
class July29Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek30(self):
        sm.current = "Julyweek30"

    def login(self):
        sm.current = "login"

    def showJuly29(self):
        with open("July29.txt", "r") as f:
            return (f.read())


"""  July week31"""
class Julyweek31Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Julycreate"

        else:
            invalidForm()

    def Julycreate(self):
        self.reset()
        sm.current = "Julycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def July30Btn(self):

        sm.current = "July30"

    def July31Btn(self):

        sm.current = "July31"


"""  July 30"""
class July30Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek31(self):
        sm.current = "Julyweek31"

    def login(self):
        sm.current = "login"

    def showJuly30(self):
        with open("July30.txt", "r") as f:
            return (f.read())



"""  July 31"""
class July31Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Julyweek31(self):
        sm.current = "Julyweek31"

    def login(self):
        sm.current = "login"

    def showJuly31(self):
        with open("July31.txt", "r") as f:
            return (f.read())



""" August"""
class AugustCreateWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:



                sm.current = "login"

        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


    def AugustWeek31Btn(self):

        sm.current = "Augustweek31"

    def AugustWeek32Btn(self):

        sm.current = "Augustweek32"

    def AugustWeek33Btn(self):

        sm.current = "Augustweek33"

    def AugustWeek34Btn(self):

        sm.current = "Augustweek34"

    def AugustWeek35Btn(self):

        sm.current = "Augustweek35"



"""  August week31"""
class Augustweek31Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Augustcreate"

        else:
            invalidForm()

    def Augustcreate(self):
        self.reset()
        sm.current = "Augustcreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def August1Btn(self):

        sm.current = "August1"

    def August2Btn(self):

        sm.current = "August2"

    def August3Btn(self):

        sm.current = "August3"

    def August4Btn(self):

        sm.current = "August4"


    def August5Btn(self):

        sm.current = "August5"



"""  August 1"""
class August1Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek31(self):
        sm.current = "Augustweek31"

    def login(self):
        sm.current = "login"

    def showAugust1(self):
        with open("August1.txt", "r") as f:
            return (f.read())




"""  August 2"""
class August2Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek31(self):
        sm.current = "Augustweek31"

    def login(self):
        sm.current = "login"

    def showAugust2(self):
        with open("August2.txt", "r") as f:
            return (f.read())




"""  August 3"""
class August3Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek31(self):
        sm.current = "Augustweek31"

    def login(self):
        sm.current = "login"

    def showAugust3(self):
        with open("August3.txt", "r") as f:
            return (f.read())



"""  August 4"""
class August4Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek31(self):
        sm.current = "Augustweek31"

    def login(self):
        sm.current = "login"

    def showAugust4(self):
        with open("August4.txt", "r") as f:
            return (f.read())



"""  August 5"""
class August5Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek31(self):
        sm.current = "Augustweek31"

    def login(self):
        sm.current = "login"

    def showAugust5(self):
        with open("August5.txt", "r") as f:
            return (f.read())




"""  August week32"""
class Augustweek32Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Augustcreate"

        else:
            invalidForm()

    def Augustcreate(self):
        self.reset()
        sm.current = "Augustcreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def August6Btn(self):

        sm.current = "August6"

    def August6Btn(self):

        sm.current = "August6"

    def August7Btn(self):

        sm.current = "August7"

    def August8Btn(self):

        sm.current = "August8"


    def August9Btn(self):

        sm.current = "August9"

    def August10Btn(self):

        sm.current = "August10"

    def August11Btn(self):

        sm.current = "August11"


    def August12Btn(self):

        sm.current = "August12"



"""  August 6"""
class August6Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek32(self):
        sm.current = "Augustweek32"

    def login(self):
        sm.current = "login"

    def showAugust6(self):
        with open("August6.txt", "r") as f:
            return (f.read())



"""  August 7"""
class August7Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek32(self):
        sm.current = "Augustweek32"

    def login(self):
        sm.current = "login"

    def showAugust7(self):
        with open("August7.txt", "r") as f:
            return (f.read())



"""  August 8"""
class August8Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek32(self):
        sm.current = "Augustweek32"

    def login(self):
        sm.current = "login"

    def showAugust8(self):
        with open("August8.txt", "r") as f:
            return (f.read())




"""  August 9"""
class August9Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek32(self):
        sm.current = "Augustweek32"

    def login(self):
        sm.current = "login"

    def showAugust9(self):
        with open("August9.txt", "r") as f:
            return (f.read())




"""  August 10"""
class August10Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek32(self):
        sm.current = "Augustweek32"

    def login(self):
        sm.current = "login"

    def showAugust10(self):
        with open("August10.txt", "r") as f:
            return (f.read())



"""  August 11"""
class August11Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek32(self):
        sm.current = "Augustweek32"

    def login(self):
        sm.current = "login"

    def showAugust11(self):
        with open("August11.txt", "r") as f:
            return (f.read())



"""  August 12"""
class August12Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek32(self):
        sm.current = "Augustweek32"

    def login(self):
        sm.current = "login"

    def showAugust12(self):
        with open("August12.txt", "r") as f:
            return (f.read())



"""  August week33"""
class Augustweek33Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Augustcreate"

        else:
            invalidForm()

    def Augustcreate(self):
        self.reset()
        sm.current = "Augustcreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def August13Btn(self):

        sm.current = "August13"

    def August14Btn(self):

        sm.current = "August14"


    def August15Btn(self):

        sm.current = "August15"


    def August16Btn(self):

        sm.current = "August16"

    def August17Btn(self):

        sm.current = "August17"

    def August18Btn(self):

        sm.current = "August18"


    def August19Btn(self):

        sm.current = "August19"



"""  August 13"""
class August13Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek33(self):
        sm.current = "Augustweek33"

    def login(self):
        sm.current = "login"

    def showAugust13(self):
        with open("August13.txt", "r") as f:
            return (f.read())



"""  August 14"""
class August14Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek33(self):
        sm.current = "Augustweek33"

    def login(self):
        sm.current = "login"

    def showAugust14(self):
        with open("August14.txt", "r") as f:
            return (f.read())



"""  August 15"""
class August15Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek33(self):
        sm.current = "Augustweek33"

    def login(self):
        sm.current = "login"

    def showAugust15(self):
        with open("August15.txt", "r") as f:
            return (f.read())



"""  August 16"""
class August16Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek33(self):
        sm.current = "Augustweek33"

    def login(self):
        sm.current = "login"

    def showAugust16(self):
        with open("August16.txt", "r") as f:
            return (f.read())



"""  August 17"""
class August17Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek33(self):
        sm.current = "Augustweek33"

    def login(self):
        sm.current = "login"

    def showAugust17(self):
        with open("August17.txt", "r") as f:
            return (f.read())



"""  August 18"""
class August18Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek33(self):
        sm.current = "Augustweek33"

    def login(self):
        sm.current = "login"

    def showAugust18(self):
        with open("August18.txt", "r") as f:
            return (f.read())



"""  August 19"""
class August19Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek33(self):
        sm.current = "Augustweek33"

    def login(self):
        sm.current = "login"

    def showAugust19(self):
        with open("August19.txt", "r") as f:
            return (f.read())



"""  August week34"""
class Augustweek34Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Augustcreate"

        else:
            invalidForm()

    def Augustcreate(self):
        self.reset()
        sm.current = "Augustcreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def August20Btn(self):

        sm.current = "August20"

    def August21Btn(self):

        sm.current = "August21"

    def August22Btn(self):

        sm.current = "August22"

    def August23Btn(self):

        sm.current = "August23"


    def August24Btn(self):

        sm.current = "August24"

    def August25Btn(self):

        sm.current = "August25"

    def August26Btn(self):

        sm.current = "August26"



"""  August 20"""
class August20Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek34(self):
        sm.current = "Augustweek34"

    def login(self):
        sm.current = "login"

    def showAugust20(self):
        with open("August20.txt", "r") as f:
            return (f.read())


"""  August 21"""
class August21Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek34(self):
        sm.current = "Augustweek34"

    def login(self):
        sm.current = "login"

    def showAugust21(self):
        with open("August21.txt", "r") as f:
            return (f.read())



"""  August 22"""
class August22Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek34(self):
        sm.current = "Augustweek34"

    def login(self):
        sm.current = "login"

    def showAugust22(self):
        with open("August22.txt", "r") as f:
            return (f.read())



"""  August 23"""
class August23Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek34(self):
        sm.current = "Augustweek34"

    def login(self):
        sm.current = "login"

    def showAugust23(self):
        with open("August23.txt", "r") as f:
            return (f.read())


"""  August 24"""
class August24Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek34(self):
        sm.current = "Augustweek34"

    def login(self):
        sm.current = "login"

    def showAugust24(self):
        with open("August24.txt", "r") as f:
            return (f.read())



"""  August 25"""
class August25Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek34(self):
        sm.current = "Augustweek34"

    def login(self):
        sm.current = "login"

    def showAugust25(self):
        with open("August25.txt", "r") as f:
            return (f.read())


"""  August 26"""
class August26Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek34(self):
        sm.current = "Augustweek34"

    def login(self):
        sm.current = "login"

    def showAugust26(self):
        with open("August26.txt", "r") as f:
            return (f.read())





"""  August week35"""
class Augustweek35Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Augustcreate"

        else:
            invalidForm()

    def Augustcreate(self):
        self.reset()
        sm.current = "Augustcreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def August27Btn(self):

        sm.current = "August27"

    def August28Btn(self):

        sm.current = "August28"

    def August29Btn(self):

        sm.current = "August29"

    def August30Btn(self):

        sm.current = "August30"


    def August31Btn(self):

        sm.current = "August31"



"""  August 27"""
class August27Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek35(self):
        sm.current = "Augustweek35"

    def login(self):
        sm.current = "login"

    def showAugust27(self):
        with open("August27.txt", "r") as f:
            return (f.read())




"""  August 28"""
class August28Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek35(self):
        sm.current = "Augustweek35"

    def login(self):
        sm.current = "login"

    def showAugust28(self):
        with open("August28.txt", "r") as f:
            return (f.read())



"""  August 29"""
class August29Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek35(self):
        sm.current = "Augustweek35"

    def login(self):
        sm.current = "login"

    def showAugust29(self):
        with open("August29.txt", "r") as f:
            return (f.read())



"""  August 30"""

class August30Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek35(self):
        sm.current = "Augustweek35"

    def login(self):
        sm.current = "login"

    def showAugust30(self):
        with open("August30.txt", "r") as f:
            return (f.read())




"""  August 31"""
class August31Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Augustweek35(self):
        sm.current = "Augustweek35"

    def login(self):
        sm.current = "login"

    def showAugust31(self):
        with open("August31.txt", "r") as f:
            return (f.read())




""" September"""
class SeptemberCreateWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:



                sm.current = "login"

        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


    def SeptemberWeek35Btn(self):

        sm.current = "Septemberweek35"

    def SeptemberWeek36Btn(self):

        sm.current = "Septemberweek36"

    def SeptemberWeek37Btn(self):

        sm.current = "Septemberweek37"

    def SeptemberWeek38Btn(self):

        sm.current = "Septemberweek38"

    def SeptemberWeek39Btn(self):

        sm.current = "Septemberweek39"



"""  September week35"""
class Septemberweek35Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Septembercreate"

        else:
            invalidForm()

    def Septembercreate(self):
        self.reset()
        sm.current = "Septembercreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def September1Btn(self):

        sm.current = "September1"

    def September2Btn(self):

        sm.current = "September2"


"""  September 1"""
class September1Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek35(self):
        sm.current = "Septemberweek35"

    def login(self):
        sm.current = "login"

    def showSeptember1(self):
        with open("September1.txt", "r") as f:
            return (f.read())


"""  September 2"""
class September2Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek35(self):
        sm.current = "Septemberweek35"

    def login(self):
        sm.current = "login"

    def showSeptember2(self):
        with open("September2.txt", "r") as f:
            return (f.read())


"""  September week36"""
class Septemberweek36Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Septembercreate"

        else:
            invalidForm()

    def Septembercreate(self):
        self.reset()
        sm.current = "Septembercreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def September3Btn(self):

        sm.current = "September3"

    def September4Btn(self):

        sm.current = "September4"

    def September5Btn(self):

        sm.current = "September5"

    def September6Btn(self):

        sm.current = "September6"

    def September7Btn(self):

        sm.current = "September7"

    def September8Btn(self):

        sm.current = "September8"

    def September9Btn(self):

        sm.current = "September9"


"""  September 3"""
class September3Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek36(self):
        sm.current = "Septemberweek36"

    def login(self):
        sm.current = "login"

    def showSeptember3(self):
        with open("September3.txt", "r") as f:
            return (f.read())


"""  September 4"""
class September4Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek36(self):
        sm.current = "Septemberweek36"

    def login(self):
        sm.current = "login"

    def showSeptember4(self):
        with open("September4.txt", "r") as f:
            return (f.read())


"""  September 5"""
class September5Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek36(self):
        sm.current = "Septemberweek36"

    def login(self):
        sm.current = "login"

    def showSeptember5(self):
        with open("September5.txt", "r") as f:
            return (f.read())


"""  September 6"""
class September6Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek36(self):
        sm.current = "Septemberweek36"

    def login(self):
        sm.current = "login"

    def showSeptember6(self):
        with open("September6.txt", "r") as f:
            return (f.read())



"""  September 7"""
class September7Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek36(self):
        sm.current = "Septemberweek36"

    def login(self):
        sm.current = "login"

    def showSeptember7(self):
        with open("September7.txt", "r") as f:
            return (f.read())


"""  September 8"""
class September8Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek36(self):
        sm.current = "Septemberweek36"

    def login(self):
        sm.current = "login"

    def showSeptember8(self):
        with open("September8.txt", "r") as f:
            return (f.read())


"""  September 9"""
class September9Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek36(self):
        sm.current = "Septemberweek36"

    def login(self):
        sm.current = "login"

    def showSeptember9(self):
        with open("September9.txt", "r") as f:
            return (f.read())


"""  September week37"""
class Septemberweek37Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Septembercreate"

        else:
            invalidForm()

    def Septembercreate(self):
        self.reset()
        sm.current = "Septembercreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def September10Btn(self):

        sm.current = "September10"

    def September11Btn(self):

        sm.current = "September11"

    def September12Btn(self):

        sm.current = "September12"

    def September13Btn(self):

        sm.current = "September13"

    def September14Btn(self):

        sm.current = "September14"

    def September15Btn(self):

        sm.current = "September15"

    def September16Btn(self):

        sm.current = "September16"




"""  September 10"""
class September10Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek37(self):
        sm.current = "Septemberweek37"

    def login(self):
        sm.current = "login"

    def showSeptember10(self):
        with open("September10.txt", "r") as f:
            return (f.read())


"""  September 11"""
class September11Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek37(self):
        sm.current = "Septemberweek37"

    def login(self):
        sm.current = "login"

    def showSeptember11(self):
        with open("September11.txt", "r") as f:
            return (f.read())


"""  September 12"""
class September12Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek37(self):
        sm.current = "Septemberweek37"

    def login(self):
        sm.current = "login"

    def showSeptember12(self):
        with open("September12.txt", "r") as f:
            return (f.read())


"""  September 13"""
class September13Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek37(self):
        sm.current = "Septemberweek37"

    def login(self):
        sm.current = "login"

    def showSeptember13(self):
        with open("September13.txt", "r") as f:
            return (f.read())


"""  September 14"""
class September14Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek37(self):
        sm.current = "Septemberweek37"

    def login(self):
        sm.current = "login"

    def showSeptember14(self):
        with open("September14.txt", "r") as f:
            return (f.read())


"""  September 15"""
class September15Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek37(self):
        sm.current = "Septemberweek37"

    def login(self):
        sm.current = "login"

    def showSeptember15(self):
        with open("September15.txt", "r") as f:
            return (f.read())


"""  September 16"""
class September16Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek37(self):
        sm.current = "Septemberweek37"

    def login(self):
        sm.current = "login"

    def showSeptember16(self):
        with open("September16.txt", "r") as f:
            return (f.read())



"""  September week38"""
class Septemberweek38Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Septembercreate"

        else:
            invalidForm()

    def Septembercreate(self):
        self.reset()
        sm.current = "Septembercreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def September17Btn(self):

        sm.current = "September17"

    def September18Btn(self):

        sm.current = "September18"

    def September19Btn(self):

        sm.current = "September19"

    def September20Btn(self):

        sm.current = "September20"

    def September21Btn(self):

        sm.current = "September21"

    def September22Btn(self):

        sm.current = "September22"

    def September23Btn(self):

        sm.current = "September23"


"""  September 17"""
class September17Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek38(self):
        sm.current = "Septemberweek38"

    def login(self):
        sm.current = "login"

    def showSeptember17(self):
        with open("September17.txt", "r") as f:
            return (f.read())



"""  September 18"""
class September18Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek38(self):
        sm.current = "Septemberweek38"

    def login(self):
        sm.current = "login"

    def showSeptember18(self):
        with open("September18.txt", "r") as f:
            return (f.read())


"""  September 19"""
class September19Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek38(self):
        sm.current = "Septemberweek38"

    def login(self):
        sm.current = "login"

    def showSeptember19(self):
        with open("September19.txt", "r") as f:
            return (f.read())



"""  September 20"""
class September20Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek38(self):
        sm.current = "Septemberweek38"

    def login(self):
        sm.current = "login"

    def showSeptember20(self):
        with open("September20.txt", "r") as f:
            return (f.read())


"""  September 21"""
class September21Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek38(self):
        sm.current = "Septemberweek38"

    def login(self):
        sm.current = "login"

    def showSeptember21(self):
        with open("September21.txt", "r") as f:
            return (f.read())


"""  September 22"""
class September22Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek38(self):
        sm.current = "Septemberweek38"

    def login(self):
        sm.current = "login"

    def showSeptember22(self):
        with open("September22.txt", "r") as f:
            return (f.read())


"""  September 23"""
class September23Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek38(self):
        sm.current = "Septemberweek38"

    def login(self):
        sm.current = "login"

    def showSeptember23(self):
        with open("September23.txt", "r") as f:
            return (f.read())


"""  September week39"""
class Septemberweek39Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Septembercreate"

        else:
            invalidForm()

    def Septembercreate(self):
        self.reset()
        sm.current = "Septembercreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def September24Btn(self):

        sm.current = "September24"

    def September25Btn(self):

        sm.current = "September25"

    def September26Btn(self):

        sm.current = "September26"

    def September27Btn(self):

        sm.current = "September27"

    def September28Btn(self):

        sm.current = "September28"

    def September29Btn(self):

        sm.current = "September29"

    def September30Btn(self):

        sm.current = "September30"



"""  September 24"""
class September24Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek39(self):
        sm.current = "Septemberweek39"

    def login(self):
        sm.current = "login"

    def showSeptember24(self):
        with open("September24.txt", "r") as f:
            return (f.read())



"""  September 25"""
class September25Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek39(self):
        sm.current = "Septemberweek39"

    def login(self):
        sm.current = "login"

    def showSeptember25(self):
        with open("September25.txt", "r") as f:
            return (f.read())



"""  September 26"""
class September26Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek39(self):
        sm.current = "Septemberweek39"

    def login(self):
        sm.current = "login"

    def showSeptember26(self):
        with open("September26.txt", "r") as f:
            return (f.read())


"""  September 27"""
class September27Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek39(self):
        sm.current = "Septemberweek39"

    def login(self):
        sm.current = "login"

    def showSeptember27(self):
        with open("September27.txt", "r") as f:
            return (f.read())



"""  September 28"""
class September28Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek39(self):
        sm.current = "Septemberweek39"

    def login(self):
        sm.current = "login"

    def showSeptember28(self):
        with open("September28.txt", "r") as f:
            return (f.read())


"""  September 29"""
class September29Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek39(self):
        sm.current = "Septemberweek39"

    def login(self):
        sm.current = "login"

    def showSeptember29(self):
        with open("September29.txt", "r") as f:
            return (f.read())



"""  September 30"""
class September30Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Septemberweek39(self):
        sm.current = "Septemberweek39"

    def login(self):
        sm.current = "login"

    def showSeptember30(self):
        with open("September30.txt", "r") as f:
            return (f.read())


""" October"""
class OctoberCreateWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:



                sm.current = "login"

        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


    def OctoberWeek40Btn(self):

        sm.current = "Octoberweek40"

    def OctoberWeek41Btn(self):

        sm.current = "Octoberweek41"

    def OctoberWeek42Btn(self):

        sm.current = "Octoberweek42"

    def OctoberWeek43Btn(self):

        sm.current = "Octoberweek43"

    def OctoberWeek44Btn(self):

        sm.current = "Octoberweek44"


"""  October week40"""
class Octoberweek40Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Octobercreate"

        else:
            invalidForm()

    def Octobercreate(self):
        self.reset()
        sm.current = "Octobercreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def October1Btn(self):

        sm.current = "October1"

    def October2Btn(self):

        sm.current = "October2"

    def October3Btn(self):

        sm.current = "October3"

    def October4Btn(self):

        sm.current = "October4"

    def October5Btn(self):

        sm.current = "October5"

    def October6Btn(self):

        sm.current = "October6"

    def October7Btn(self):

        sm.current = "October7"



""" October  1"""
class October1Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek40(self):
        sm.current = "Octoberweek40"

    def login(self):
        sm.current = "login"

    def showOctober1(self):
        with open("October1.txt", "r") as f:
            return (f.read())



""" October  2"""
class October2Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek40(self):
        sm.current = "Octoberweek40"

    def login(self):
        sm.current = "login"

    def showOctober2(self):
        with open("October2.txt", "r") as f:
            return (f.read())





""" October  3"""
class October3Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek40(self):
        sm.current = "Octoberweek40"

    def login(self):
        sm.current = "login"

    def showOctober3(self):
        with open("October3.txt", "r") as f:
            return (f.read())


""" October  4"""
class October4Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek40(self):
        sm.current = "Octoberweek40"

    def login(self):
        sm.current = "login"

    def showOctober4(self):
        with open("October4.txt", "r") as f:
            return (f.read())


""" October  5"""
class October5Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)





    def login(self):
        sm.current = "login"

    def showOctober5(self):
        with open("October5.txt", "r") as f:
            return (f.read())



""" October  5"""
class October5Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek40(self):
        sm.current = "Octoberweek40"

    def login(self):
        sm.current = "login"

    def showOctober5(self):
        with open("October5.txt", "r") as f:
            return (f.read())



""" October  6"""
class October6Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek40(self):
        sm.current = "Octoberweek40"

    def login(self):
        sm.current = "login"

    def showOctober6(self):
        with open("October6.txt", "r") as f:
            return (f.read())


""" October  7"""
class October7Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek40(self):
        sm.current = "Octoberweek40"

    def login(self):
        sm.current = "login"

    def showOctober7(self):
        with open("October7.txt", "r") as f:
            return (f.read())



"""  October week41"""
class Octoberweek41Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Octobercreate"

        else:
            invalidForm()

    def Octobercreate(self):
        self.reset()
        sm.current = "Octobercreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def October8Btn(self):

        sm.current = "October8"

    def October9Btn(self):

        sm.current = "October9"

    def October10Btn(self):

        sm.current = "October10"

    def October11Btn(self):

        sm.current = "October11"

    def October12Btn(self):

        sm.current = "October12"

    def October13Btn(self):

        sm.current = "October13"

    def October14Btn(self):

        sm.current = "October14"


""" October  8"""
class October8Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek41(self):
        sm.current = "Octoberweek41"

    def login(self):
        sm.current = "login"

    def showOctober8(self):
        with open("October8.txt", "r") as f:
            return (f.read())


""" October  9"""
class October9Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek41(self):
        sm.current = "Octoberweek41"

    def login(self):
        sm.current = "login"

    def showOctober9(self):
        with open("October9.txt", "r") as f:
            return (f.read())



""" October  10"""
class October10Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek41(self):
        sm.current = "Octoberweek41"

    def login(self):
        sm.current = "login"

    def showOctober10(self):
        with open("October10.txt", "r") as f:
            return (f.read())



""" October  11"""
class October11Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek41(self):
        sm.current = "Octoberweek41"

    def login(self):
        sm.current = "login"

    def showOctober11(self):
        with open("October11.txt", "r") as f:
            return (f.read())



""" October  12"""
class October12Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek41(self):
        sm.current = "Octoberweek41"

    def login(self):
        sm.current = "login"

    def showOctober12(self):
        with open("October12.txt", "r") as f:
            return (f.read())



""" October  13"""
class October13Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek41(self):
        sm.current = "Octoberweek41"

    def login(self):
        sm.current = "login"

    def showOctober13(self):
        with open("October13.txt", "r") as f:
            return (f.read())


""" October  14"""
class October14Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek41(self):
        sm.current = "Octoberweek41"

    def login(self):
        sm.current = "login"

    def showOctober14(self):
        with open("October14.txt", "r") as f:
            return (f.read())


"""  October week42"""
class Octoberweek42Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Octobercreate"

        else:
            invalidForm()

    def Octobercreate(self):
        self.reset()
        sm.current = "Octobercreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def October15Btn(self):

        sm.current = "October15"

    def October16Btn(self):

        sm.current = "October16"

    def October17Btn(self):

        sm.current = "October17"

    def October18Btn(self):

        sm.current = "October18"

    def October19Btn(self):

        sm.current = "October19"

    def October20Btn(self):

        sm.current = "October20"

    def October21Btn(self):

        sm.current = "October21"


""" October  15"""
class October15Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek42(self):
        sm.current = "Octoberweek42"

    def login(self):
        sm.current = "login"

    def showOctober15(self):
        with open("October15.txt", "r") as f:
            return (f.read())



""" October  16"""
class October16Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek42(self):
        sm.current = "Octoberweek42"

    def login(self):
        sm.current = "login"

    def showOctober16(self):
        with open("October16.txt", "r") as f:
            return (f.read())


""" October  17"""
class October17Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek42(self):
        sm.current = "Octoberweek42"

    def login(self):
        sm.current = "login"

    def showOctober17(self):
        with open("October17.txt", "r") as f:
            return (f.read())


""" October  18"""
class October18Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek42(self):
        sm.current = "Octoberweek42"

    def login(self):
        sm.current = "login"

    def showOctober18(self):
        with open("October18.txt", "r") as f:
            return (f.read())


""" October  19"""
class October19Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek42(self):
        sm.current = "Octoberweek42"

    def login(self):
        sm.current = "login"

    def showOctober19(self):
        with open("October19.txt", "r") as f:
            return (f.read())


""" October  20"""
class October20Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek42(self):
        sm.current = "Octoberweek42"

    def login(self):
        sm.current = "login"

    def showOctober20(self):
        with open("October20.txt", "r") as f:
            return (f.read())


""" October  21"""
class October21Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek42(self):
        sm.current = "Octoberweek42"

    def login(self):
        sm.current = "login"

    def showOctober21(self):
        with open("October21.txt", "r") as f:
            return (f.read())


"""  October week43"""
class Octoberweek43Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Octobercreate"

        else:
            invalidForm()

    def Octobercreate(self):
        self.reset()
        sm.current = "Octobercreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def October22Btn(self):

        sm.current = "October22"


    def October23Btn(self):

        sm.current = "October23"

    def October24Btn(self):

        sm.current = "October24"

    def October25Btn(self):

        sm.current = "October25"

    def October26Btn(self):

        sm.current = "October26"

    def October27Btn(self):

        sm.current = "October27"

    def October28Btn(self):

        sm.current = "October28"



""" October  22"""
class October22Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek43(self):
        sm.current = "Octoberweek43"

    def login(self):
        sm.current = "login"

    def showOctober22(self):
        with open("October22.txt", "r") as f:
            return (f.read())


""" October  23"""
class October23Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek43(self):
        sm.current = "Octoberweek43"

    def login(self):
        sm.current = "login"

    def showOctober23(self):
        with open("October23.txt", "r") as f:
            return (f.read())



""" October  24"""
class October24Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek43(self):
        sm.current = "Octoberweek43"

    def login(self):
        sm.current = "login"

    def showOctober24(self):
        with open("October24.txt", "r") as f:
            return (f.read())


""" October  25"""
class October25Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek43(self):
        sm.current = "Octoberweek43"

    def login(self):
        sm.current = "login"

    def showOctober25(self):
        with open("October25.txt", "r") as f:
            return (f.read())



""" October  26"""
class October26Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek43(self):
        sm.current = "Octoberweek43"

    def login(self):
        sm.current = "login"

    def showOctober26(self):
        with open("October26.txt", "r") as f:
            return (f.read())


""" October  27"""
class October27Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek43(self):
        sm.current = "Octoberweek43"

    def login(self):
        sm.current = "login"

    def showOctober27(self):
        with open("October27.txt", "r") as f:
            return (f.read())


""" October  28"""
class October28Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek43(self):
        sm.current = "Octoberweek43"

    def login(self):
        sm.current = "login"

    def showOctober28(self):
        with open("October28.txt", "r") as f:
            return (f.read())


"""  October week44"""
class Octoberweek44Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Octobercreate"

        else:
            invalidForm()

    def Octobercreate(self):
        self.reset()
        sm.current = "Octobercreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def October29Btn(self):

        sm.current = "October29"


    def October30Btn(self):

        sm.current = "October30"

    def October31Btn(self):

        sm.current = "October31"



    """ October  28"""

    class October28Window(Screen):
        namee = ObjectProperty(None)
        email = ObjectProperty(None)
        password = ObjectProperty(None)
        namejan = ObjectProperty(None)
        nameFeb = ObjectProperty(None)



        def Octoberweek43(self):
            sm.current = "Octoberweek43"

        def login(self):
            sm.current = "login"

        def showOctober28(self):
            with open("October28.txt", "r") as f:
                return (f.read())


""" October  29"""
class October29Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek44(self):
        sm.current = "Octoberweek44"

    def login(self):
        sm.current = "login"

    def showOctober29(self):
        with open("October29.txt", "r") as f:
            return (f.read())


""" October  30"""
class October30Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek44(self):
        sm.current = "Octoberweek44"

    def login(self):
        sm.current = "login"

    def showOctober30(self):
        with open("October30.txt", "r") as f:
            return (f.read())


""" October  31"""
class October31Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Octoberweek44(self):
        sm.current = "Octoberweek44"

    def login(self):
        sm.current = "login"

    def showOctober31(self):
        with open("October31.txt", "r") as f:
            return (f.read())


""" November"""
class NovemberCreateWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:



                sm.current = "login"

        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


    def NovemberWeek44Btn(self):

        sm.current = "Novemberweek44"

    def NovemberWeek45Btn(self):

        sm.current = "Novemberweek45"

    def NovemberWeek46Btn(self):

        sm.current = "Novemberweek46"

    def NovemberWeek47Btn(self):

        sm.current = "Novemberweek47"

    def NovemberWeek48Btn(self):

        sm.current = "Novemberweek48"




"""  November week44"""
class Novemberweek44Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Novembercreate"

        else:
            invalidForm()

    def Novembercreate(self):
        self.reset()
        sm.current = "Novembercreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def November1Btn(self):

        sm.current = "November1"


    def November2Btn(self):

        sm.current = "November2"

    def November3Btn(self):

        sm.current = "November3"


    def November4Btn(self):

        sm.current = "November4"



""" November  1"""
class November1Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek44(self):
        sm.current = "Novemberweek44"

    def login(self):
        sm.current = "login"

    def showNovember1(self):
        with open("November1.txt", "r") as f:
            return (f.read())


""" November  2"""
class November2Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek44(self):
        sm.current = "Novemberweek44"

    def login(self):
        sm.current = "login"

    def showNovember2(self):
        with open("November2.txt", "r") as f:
            return (f.read())


""" November  3"""
class November3Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek44(self):
        sm.current = "Novemberweek44"

    def login(self):
        sm.current = "login"

    def showNovember3(self):
        with open("November3.txt", "r") as f:
            return (f.read())


""" November  4"""
class November4Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek44(self):
        sm.current = "Novemberweek44"

    def login(self):
        sm.current = "login"

    def showNovember4(self):
        with open("November4.txt", "r") as f:
            return (f.read())


"""  November week45"""
class Novemberweek45Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Novembercreate"

        else:
            invalidForm()

    def Novembercreate(self):
        self.reset()
        sm.current = "Novembercreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def November5Btn(self):

        sm.current = "November5"


    def November6Btn(self):

        sm.current = "November6"

    def November7Btn(self):

        sm.current = "November7"


    def November8Btn(self):

        sm.current = "November8"


    def November9Btn(self):

        sm.current = "November9"

    def November10Btn(self):

        sm.current = "November10"


    def November11Btn(self):

        sm.current = "November11"


""" November  5"""
class November5Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek45(self):
        sm.current = "Novemberweek45"

    def login(self):
        sm.current = "login"

    def showNovember5(self):
        with open("November5.txt", "r") as f:
            return (f.read())



""" November  6"""
class November6Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek45(self):
        sm.current = "Novemberweek45"

    def login(self):
        sm.current = "login"

    def showNovember6(self):
        with open("November6.txt", "r") as f:
            return (f.read())



""" November  7"""
class November7Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek45(self):
        sm.current = "Novemberweek45"

    def login(self):
        sm.current = "login"

    def showNovember7(self):
        with open("November7.txt", "r") as f:
            return (f.read())


""" November  8"""
class November8Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek45(self):
        sm.current = "Novemberweek45"

    def login(self):
        sm.current = "login"

    def showNovember8(self):
        with open("November8.txt", "r") as f:
            return (f.read())


""" November  9"""
class November9Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek45(self):
        sm.current = "Novemberweek45"

    def login(self):
        sm.current = "login"

    def showNovember9(self):
        with open("November9.txt", "r") as f:
            return (f.read())



""" November  10"""
class November10Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek45(self):
        sm.current = "Novemberweek45"

    def login(self):
        sm.current = "login"

    def showNovember10(self):
        with open("November10.txt", "r") as f:
            return (f.read())



""" November  11"""
class November11Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek45(self):
        sm.current = "Novemberweek45"

    def login(self):
        sm.current = "login"

    def showNovember11(self):
        with open("November11.txt", "r") as f:
            return (f.read())



"""  November week46"""
class Novemberweek46Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Novembercreate"

        else:
            invalidForm()

    def Novembercreate(self):
        self.reset()
        sm.current = "Novembercreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def November12Btn(self):

        sm.current = "November12"


    def November13Btn(self):

        sm.current = "November13"


    def November14Btn(self):

        sm.current = "November14"

    def November15Btn(self):

        sm.current = "November15"


    def November16Btn(self):

        sm.current = "November16"


    def November17Btn(self):

        sm.current = "November17"

    def November18Btn(self):

        sm.current = "November18"




""" November  12"""
class November12Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek46(self):
        sm.current = "Novemberweek46"

    def login(self):
        sm.current = "login"

    def showNovember12(self):
        with open("November12.txt", "r") as f:
            return (f.read())


""" November  13"""
class November13Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek46(self):
        sm.current = "Novemberweek46"

    def login(self):
        sm.current = "login"

    def showNovember13(self):
        with open("November13.txt", "r") as f:
            return (f.read())



""" November  14"""
class November14Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek46(self):
        sm.current = "Novemberweek46"

    def login(self):
        sm.current = "login"

    def showNovember14(self):
        with open("November14.txt", "r") as f:
            return (f.read())



""" November  15"""
class November15Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek46(self):
        sm.current = "Novemberweek46"

    def login(self):
        sm.current = "login"

    def showNovember15(self):
        with open("November15.txt", "r") as f:
            return (f.read())



""" November  16"""
class November16Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek46(self):
        sm.current = "Novemberweek46"

    def login(self):
        sm.current = "login"

    def showNovember16(self):
        with open("November16.txt", "r") as f:
            return (f.read())



""" November  17"""
class November17Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek46(self):
        sm.current = "Novemberweek46"

    def login(self):
        sm.current = "login"

    def showNovember17(self):
        with open("November17.txt", "r") as f:
            return (f.read())



""" November  18"""
class November18Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek46(self):
        sm.current = "Novemberweek46"

    def login(self):
        sm.current = "login"

    def showNovember18(self):
        with open("November18.txt", "r") as f:
            return (f.read())



"""  November week47"""
class Novemberweek47Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Novembercreate"

        else:
            invalidForm()

    def Novembercreate(self):
        self.reset()
        sm.current = "Novembercreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"



    def November19Btn(self):

        sm.current = "November19"


    def November20Btn(self):

        sm.current = "November20"


    def November21Btn(self):

        sm.current = "November21"

    def November22Btn(self):

        sm.current = "November22"


    def November23Btn(self):

        sm.current = "November23"


    def November24Btn(self):

        sm.current = "November24"

    def November25Btn(self):

        sm.current = "November25"



""" November  19"""
class November19Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek47(self):
        sm.current = "Novemberweek47"

    def login(self):
        sm.current = "login"

    def showNovember19(self):
        with open("November19.txt", "r") as f:
            return (f.read())


""" November  20"""
class November20Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek47(self):
        sm.current = "Novemberweek47"

    def login(self):
        sm.current = "login"

    def showNovember20(self):
        with open("November20.txt", "r") as f:
            return (f.read())



""" November  21"""
class November21Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek47(self):
        sm.current = "Novemberweek47"

    def login(self):
        sm.current = "login"

    def showNovember21(self):
        with open("November21.txt", "r") as f:
            return (f.read())


""" November  22"""
class November22Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek47(self):
        sm.current = "Novemberweek47"

    def login(self):
        sm.current = "login"

    def showNovember22(self):
        with open("November22.txt", "r") as f:
            return (f.read())


""" November  23"""
class November23Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek47(self):
        sm.current = "Novemberweek47"

    def login(self):
        sm.current = "login"

    def showNovember23(self):
        with open("November23.txt", "r") as f:
            return (f.read())



""" November  24"""
class November24Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek47(self):
        sm.current = "Novemberweek47"

    def login(self):
        sm.current = "login"

    def showNovember24(self):
        with open("November24.txt", "r") as f:
            return (f.read())



""" November  25"""
class November25Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek47(self):
        sm.current = "Novemberweek47"

    def login(self):
        sm.current = "login"

    def showNovember25(self):
        with open("November25.txt", "r") as f:
            return (f.read())


"""  November week48"""
class Novemberweek48Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Novembercreate"

        else:
            invalidForm()

    def Novembercreate(self):
        self.reset()
        sm.current = "Novembercreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"



    def November26Btn(self):

        sm.current = "November26"


    def November27Btn(self):

        sm.current = "November27"


    def November28Btn(self):

        sm.current = "November28"

    def November29Btn(self):

        sm.current = "November29"


    def November30Btn(self):

        sm.current = "November30"



""" November  26"""
class November26Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek48(self):
        sm.current = "Novemberweek48"

    def login(self):
        sm.current = "login"

    def showNovember26(self):
        with open("November26.txt", "r") as f:
            return (f.read())



""" November  27"""
class November27Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek48(self):
        sm.current = "Novemberweek48"

    def login(self):
        sm.current = "login"

    def showNovember27(self):
        with open("November27.txt", "r") as f:
            return (f.read())



""" November  28"""
class November28Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek48(self):
        sm.current = "Novemberweek48"

    def login(self):
        sm.current = "login"

    def showNovember28(self):
        with open("November28.txt", "r") as f:
            return (f.read())



""" November  29"""
class November29Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek48(self):
        sm.current = "Novemberweek48"

    def login(self):
        sm.current = "login"

    def showNovember29(self):
        with open("November29.txt", "r") as f:
            return (f.read())



""" November  30"""
class November30Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Novemberweek48(self):
        sm.current = "Novemberweek48"

    def login(self):
        sm.current = "login"

    def showNovember30(self):
        with open("November30.txt", "r") as f:
            return (f.read())



""" December"""
class DecemberCreateWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:



                sm.current = "login"

        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


    def DecemberWeek48Btn(self):

        sm.current = "Decemberweek48"

    def DecemberWeek49Btn(self):

        sm.current = "Decemberweek49"

    def DecemberWeek50Btn(self):

        sm.current = "Decemberweek50"

    def DecemberWeek51Btn(self):

        sm.current = "Decemberweek51"

    def DecemberWeek52Btn(self):

        sm.current = "Decemberweek52"



"""  December week48"""
class Decemberweek48Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Decembercreate"

        else:
            invalidForm()

    def Decembercreate(self):
        self.reset()
        sm.current = "Decembercreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def December1Btn(self):

        sm.current = "December1"


    def December2Btn(self):

        sm.current = "December2"


""" December  1"""
class December1Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek48(self):
        sm.current = "Decemberweek48"

    def login(self):
        sm.current = "login"

    def showDecember1(self):
        with open("December1.txt", "r") as f:
            return (f.read())



""" December  2"""
class December2Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek48(self):
        sm.current = "Decemberweek48"

    def login(self):
        sm.current = "login"

    def showDecember2(self):
        with open("December2.txt", "r") as f:
            return (f.read())


"""  December week49"""
class Decemberweek49Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Decembercreate"

        else:
            invalidForm()

    def Decembercreate(self):
        self.reset()
        sm.current = "Decembercreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def December3Btn(self):

        sm.current = "December3"


    def December4Btn(self):

        sm.current = "December4"

    def December5Btn(self):

        sm.current = "December5"


    def December6Btn(self):

        sm.current = "December6"

    def December7Btn(self):

        sm.current = "December7"


    def December8Btn(self):

        sm.current = "December8"

    def December9Btn(self):

        sm.current = "December9"


""" December  3"""
class December3Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek49(self):
        sm.current = "Decemberweek49"

    def login(self):
        sm.current = "login"

    def showDecember3(self):
        with open("December3.txt", "r") as f:
            return (f.read())




""" December  4"""
class December4Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek49(self):
        sm.current = "Decemberweek49"

    def login(self):
        sm.current = "login"

    def showDecember4(self):
        with open("December4.txt", "r") as f:
            return (f.read())



""" December  5"""
class December5Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek49(self):
        sm.current = "Decemberweek49"

    def login(self):
        sm.current = "login"

    def showDecember5(self):
        with open("December5.txt", "r") as f:
            return (f.read())




""" December  6"""
class December6Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek49(self):
        sm.current = "Decemberweek49"

    def login(self):
        sm.current = "login"

    def showDecember6(self):
        with open("December6.txt", "r") as f:
            return (f.read())




""" December  7"""
class December7Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek49(self):
        sm.current = "Decemberweek49"

    def login(self):
        sm.current = "login"

    def showDecember7(self):
        with open("December7.txt", "r") as f:
            return (f.read())



""" December  8"""
class December8Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek49(self):
        sm.current = "Decemberweek49"

    def login(self):
        sm.current = "login"

    def showDecember8(self):
        with open("December8.txt", "r") as f:
            return (f.read())



""" December  9"""
class December9Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek49(self):
        sm.current = "Decemberweek49"

    def login(self):
        sm.current = "login"

    def showDecember9(self):
        with open("December9.txt", "r") as f:
            return (f.read())


"""  December week50"""
class Decemberweek50Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Decembercreate"

        else:
            invalidForm()

    def Decembercreate(self):
        self.reset()
        sm.current = "Decembercreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def December10Btn(self):

        sm.current = "December10"


    def December11Btn(self):

        sm.current = "December11"

    def December12Btn(self):

        sm.current = "December12"


    def December13Btn(self):

        sm.current = "December13"

    def December14Btn(self):

        sm.current = "December14"


    def December15Btn(self):

        sm.current = "December15"

    def December16Btn(self):

        sm.current = "December16"

""" December  10"""
class December10Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek50(self):
        sm.current = "Decemberweek50"

    def login(self):
        sm.current = "login"

    def showDecember10(self):
        with open("December10.txt", "r") as f:
            return (f.read())



""" December  11"""
class December11Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek50(self):
        sm.current = "Decemberweek50"

    def login(self):
        sm.current = "login"

    def showDecember11(self):
        with open("December11.txt", "r") as f:
            return (f.read())



""" December  12"""
class December12Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek50(self):
        sm.current = "Decemberweek50"

    def login(self):
        sm.current = "login"

    def showDecember12(self):
        with open("December12.txt", "r") as f:
            return (f.read())



""" December  13"""
class December13Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek50(self):
        sm.current = "Decemberweek50"

    def login(self):
        sm.current = "login"

    def showDecember13(self):
        with open("December13.txt", "r") as f:
            return (f.read())



""" December  14"""
class December14Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek50(self):
        sm.current = "Decemberweek50"

    def login(self):
        sm.current = "login"

    def showDecember14(self):
        with open("December14.txt", "r") as f:
            return (f.read())



""" December  15"""
class December15Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek50(self):
        sm.current = "Decemberweek50"

    def login(self):
        sm.current = "login"

    def showDecember15(self):
        with open("December15.txt", "r") as f:
            return (f.read())



""" December  16"""
class December16Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek50(self):
        sm.current = "Decemberweek50"

    def login(self):
        sm.current = "login"

    def showDecember16(self):
        with open("December16.txt", "r") as f:
            return (f.read())



"""  December week51"""
class Decemberweek51Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Decembercreate"

        else:
            invalidForm()

    def Decembercreate(self):
        self.reset()
        sm.current = "Decembercreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def December17Btn(self):

        sm.current = "December17"


    def December18Btn(self):

        sm.current = "December18"

    def December19Btn(self):

        sm.current = "December19"


    def December20Btn(self):

        sm.current = "December20"

    def December21Btn(self):

        sm.current = "December21"


    def December22Btn(self):

        sm.current = "December22"

    def December23Btn(self):

        sm.current = "December23"


""" December  17"""
class December17Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek51(self):
        sm.current = "Decemberweek51"

    def login(self):
        sm.current = "login"

    def showDecember17(self):
        with open("December17.txt", "r") as f:
            return (f.read())



""" December  18"""
class December18Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek51(self):
        sm.current = "Decemberweek51"

    def login(self):
        sm.current = "login"

    def showDecember18(self):
        with open("December18.txt", "r") as f:
            return (f.read())



""" December  19"""
class December19Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek51(self):
        sm.current = "Decemberweek51"

    def login(self):
        sm.current = "login"

    def showDecember19(self):
        with open("December19.txt", "r") as f:
            return (f.read())




""" December  20"""
class December20Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek51(self):
        sm.current = "Decemberweek51"

    def login(self):
        sm.current = "login"

    def showDecember20(self):
        with open("December20.txt", "r") as f:
            return (f.read())



""" December  21"""
class December21Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek51(self):
        sm.current = "Decemberweek51"

    def login(self):
        sm.current = "login"

    def showDecember21(self):
        with open("December21.txt", "r") as f:
            return (f.read())



""" December  22"""
class December22Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek51(self):
        sm.current = "Decemberweek51"

    def login(self):
        sm.current = "login"

    def showDecember22(self):
        with open("December22.txt", "r") as f:
            return (f.read())




""" December  23"""
class December23Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek51(self):
        sm.current = "Decemberweek51"

    def login(self):
        sm.current = "login"

    def showDecember23(self):
        with open("December23.txt", "r") as f:
            return (f.read())




"""  December week52"""
class Decemberweek52Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:

                sm.current = "Decembercreate"

        else:
            invalidForm()

    def Decembercreate(self):
        self.reset()
        sm.current = "Decembercreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"


    def December24Btn(self):

        sm.current = "December24"


    def December25Btn(self):

        sm.current = "December25"

    def December26Btn(self):

        sm.current = "December26"


    def December27Btn(self):

        sm.current = "December27"

    def December28Btn(self):

        sm.current = "December28"


    def December29Btn(self):

        sm.current = "December29"

    def December30Btn(self):

        sm.current = "December30"

    def December31Btn(self):

        sm.current = "December31"



""" December  24"""
class December24Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek52(self):
        sm.current = "Decemberweek52"

    def login(self):
        sm.current = "login"

    def showDecember24(self):
        with open("December24.txt", "r") as f:
            return (f.read())



""" December  25"""
class December25Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek52(self):
        sm.current = "Decemberweek52"

    def login(self):
        sm.current = "login"

    def showDecember25(self):
        with open("December25.txt", "r") as f:
            return (f.read())




""" December  26"""
class December26Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek52(self):
        sm.current = "Decemberweek52"

    def login(self):
        sm.current = "login"

    def showDecember26(self):
        with open("December26.txt", "r") as f:
            return (f.read())



""" December  27"""
class December27Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek52(self):
        sm.current = "Decemberweek52"

    def login(self):
        sm.current = "login"

    def showDecember27(self):
        with open("December27.txt", "r") as f:
            return (f.read())



""" December  28"""
class December28Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek52(self):
        sm.current = "Decemberweek52"

    def login(self):
        sm.current = "login"

    def showDecember28(self):
        with open("December28.txt", "r") as f:
            return (f.read())



""" December  29"""
class December29Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek52(self):
        sm.current = "Decemberweek52"

    def login(self):
        sm.current = "login"

    def showDecember29(self):
        with open("December29.txt", "r") as f:
            return (f.read())


""" December  30"""
class December30Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek52(self):
        sm.current = "Decemberweek52"

    def login(self):
        sm.current = "login"

    def showDecember30(self):
        with open("December30.txt", "r") as f:
            return (f.read())


""" December  31"""
class December31Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)



    def Decemberweek52(self):
        sm.current = "Decemberweek52"

    def login(self):
        sm.current = "login"

    def showDecember31(self):
        with open("December31.txt", "r") as f:
            return (f.read())



    def loginBtn(self):
       self








class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    JANUARY = ObjectProperty(None)
    current = ""





class WindowManager(ScreenManager):
    pass
class WindowManagerFeb(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()







def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()






class CustomScreen(Screen):
    hue = NumericProperty(0)


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))


class RV(RecycleView):
    sm= ObjectProperty(None)
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(1)]
        Window.bind(on_keyboard=self.Android_back_click)

    def Android_back_click(self,window,key,*largs):
        if key == 27:

            sm.current='login'

            return True

class RVScreen(Screen):
    pass

class BBScreen(Screen):
    pass


sm = WindowManager()
smFeb = WindowManagerFeb()

RVScreens =[LoginWindow(name="login")]

BBScreens = [JanuaryCreateWindow(name="Januarycreate"),Januaryweek1Window(name="Januaryweek1"),January1Window(name="January1"),January2Window(name="January2"),January3Window(name="January3"),January4Window(name="January4"),January5Window(name="January5"),January6Window(name="January6"),January7Window(name="January7"),Januaryweek2Window(name="Januaryweek2"),January8Window(name="January8"),January9Window(name="January9"),January10Window(name="January10"),January11Window(name="January11"),January12Window(name="January12"),January13Window(name="January13"),January14Window(name="January14"),Januaryweek3Window(name="Januaryweek3"),January15Window(name="January15"),January16Window(name="January16"),January17Window(name="January17"),January18Window(name="January18"),January19Window(name="January19"),January20Window(name="January20"),January21Window(name="January21"),Januaryweek4Window(name="Januaryweek4"),January22Window(name="January22"),January23Window(name="January23"),January24Window(name="January24"),January25Window(name="January25"),January26Window(name="January26"),January27Window(name="January27"),January28Window(name="January28"),Januaryweek5Window(name="Januaryweek5"),January29Window(name="January29"),January30Window(name="January30"),January31Window(name="January31"),\
           FebruaryCreateWindow(name="Februarycreate"),Februaryweek5Window(name="Februaryweek5"),February1Window(name="February1"),February2Window(name="February2"),February3Window(name="February3"),February4Window(name="February4"),week6Window(name="week6"),February5Window(name="February5"),February6Window(name="February6"),February7Window(name="February7"),February8Window(name="February8"),February9Window(name="February9"),February10Window(name="February10"),February11Window(name="February11"),week7Window(name="week7"),February12Window(name="February12"),February13Window(name="February13"),February14Window(name="February14"),February15Window(name="February15"),February16Window(name="February16"),February17Window(name="February17"),February18Window(name="February18"),week8Window(name="week8"),week9Window(name="week9"),February19Window(name="February19"),February20Window(name="February20"),February21Window(name="February21"),February22Window(name="February22"),February23Window(name="February23"),February24Window(name="February24"),February25Window(name="February25"),February26Window(name="February26"),February27Window(name="February27"),February28Window(name="February28"),\
           MarchCreateWindow(name="Marchcreate"),Marchweek9Window(name="Marchweek9"),March1Window(name="March1"),March2Window(name="March2"),March3Window(name="March3"),March4Window(name="March4"),week10Window(name="week10"),March5Window(name="March5"),March6Window(name="March6"),March7Window(name="March7"),March8Window(name="March8"),March9Window(name="March9"),March10Window(name="March10"),March11Window(name="March11"),week11Window(name="week11"),March12Window(name="March12"),March13Window(name="March13"),March14Window(name="March14"),March15Window(name="March15"),March16Window(name="March16"),March17Window(name="March17"),March18Window(name="March18"),week12Window(name="week12"),March19Window(name="March19"),March20Window(name="March20"),March21Window(name="March21"),March22Window(name="March22"),March23Window(name="March23"),March24Window(name="March24"),March25Window(name="March25"),week13Window(name="week13"),March26Window(name="March26"),March27Window(name="March27"),March28Window(name="March28"),March29Window(name="March29"),March30Window(name="March30"),March31Window(name="March31"),\
           AprilCreateWindow(name="Aprilcreate"),Aprilweek13Window(name="Aprilweek13"),April1Window(name="April1"),week14Window(name="week14"),April2Window(name="April2"),April3Window(name="April3"),April4Window(name="April4"),April5Window(name="April5"),April6Window(name="April6"),April7Window(name="April7"),April8Window(name="April8"),week15Window(name="week15"),April9Window(name="April9"),April10Window(name="April10"),April11Window(name="April11"),April12Window(name="April12"),April13Window(name="April13"),April14Window(name="April14"),April15Window(name="April15"),week16Window(name="week16"),April16Window(name="April16"),April17Window(name="April17"),April18Window(name="April18"),April19Window(name="April19"),April20Window(name="April20"),April21Window(name="April21"),April22Window(name="April22"),week17Window(name="week17"),April23Window(name="April23"),April24Window(name="April24"),April25Window(name="April25"),April26Window(name="April26"),April27Window(name="April27"),April28Window(name="April28"),April29Window(name="April29"),week18Window(name="week18"),April30Window(name="April30"),\
           MayCreateWindow(name="Maycreate"),Mayweek18Window(name="Mayweek18"),May1Window(name="May1"),May2Window(name="May2"),May3Window(name="May3"),May4Window(name="May4"),May5Window(name="May5"),May6Window(name="May6"),Mayweek19Window(name="Mayweek19"),May7Window(name="May7"),May8Window(name="May8"),May9Window(name="May9"),May10Window(name="May10"),May11Window(name="May11"),May12Window(name="May12"),May13Window(name="May13"),Mayweek20Window(name="Mayweek20"),May14Window(name="May14"),May15Window(name="May15"),May16Window(name="May16"),May17Window(name="May17"),May18Window(name="May18"),May19Window(name="May19"),May20Window(name="May20"),Mayweek21Window(name="Mayweek21"),May21Window(name="May21"),May22Window(name="May22"),May23Window(name="May23"),May24Window(name="May24"),May25Window(name="May25"),May26Window(name="May26"),May27Window(name="May27"),Mayweek22Window(name="Mayweek22"),May28Window(name="May28"),May29Window(name="May29"),May30Window(name="May30"),May31Window(name="May31"),\
           JuneCreateWindow(name="Junecreate"),Juneweek22Window(name="Juneweek22"),June1Window(name="June1"),June2Window(name="June2"),June3Window(name="June3"),Juneweek23Window(name="Juneweek23"),June4Window(name="June4"),June5Window(name="June5"),June6Window(name="June6"),June7Window(name="June7"),June8Window(name="June8"),June9Window(name="June9"),June10Window(name="June10"),Juneweek24Window(name="Juneweek24"),June11Window(name="June11"),June12Window(name="June12"),June13Window(name="June13"),June14Window(name="June14"),June15Window(name="June15"),June16Window(name="June16"),June17Window(name="June17"),Juneweek25Window(name="Juneweek25"),June18Window(name="June18"),June19Window(name="June19"),June20Window(name="June20"),June21Window(name="June21"),June22Window(name="June22"),June23Window(name="June23"),June24Window(name="June24"),Juneweek26Window(name="Juneweek26"),June25Window(name="June25"),June26Window(name="June26"),June27Window(name="June27"),June28Window(name="June28"),June29Window(name="June29"),June30Window(name="June30"),\
           JulyCreateWindow(name="Julycreate"),Julyweek26Window(name="Julyweek26"),July1Window(name="July1"),Julyweek27Window(name="Julyweek27"),July2Window(name="July2"),July3Window(name="July3"),July4Window(name="July4"),July5Window(name="July5"),July6Window(name="July6"),July7Window(name="July7"),July8Window(name="July8"),Julyweek28Window(name="Julyweek28"),July9Window(name="July9"),July10Window(name="July10"),July11Window(name="July11"),July12Window(name="July12"),July13Window(name="July13"),July14Window(name="July14"),July15Window(name="July15"),Julyweek29Window(name="Julyweek29"),July16Window(name="July16"),July17Window(name="July17"),July18Window(name="July18"),July19Window(name="July19"),July20Window(name="July20"),July21Window(name="July21"),July22Window(name="July22"),Julyweek30Window(name="Julyweek30"),July23Window(name="July23"),July24Window(name="July24"),July25Window(name="July25"),July26Window(name="July26") ,July27Window(name="July27"),July28Window(name="July28"),July29Window(name="July29"),Julyweek31Window(name="Julyweek31"),July30Window(name="July30"),July31Window(name="July31"),\
           AugustCreateWindow(name="Augustcreate"),Augustweek31Window(name="Augustweek31"),August1Window(name="August1"),August2Window(name="August2"),August3Window(name="August3"),August4Window(name="August4"),August5Window(name="August5"),Augustweek32Window(name="Augustweek32"),August6Window(name="August6"),August7Window(name="August7"),August8Window(name="August8"),August9Window(name="August9"),August10Window(name="August10"),August11Window(name="August11"),August12Window(name="August12"),Augustweek33Window(name="Augustweek33"),August13Window(name="August13"),August14Window(name="August14"),August15Window(name="August15"),August16Window(name="August16"),August17Window(name="August17"),August18Window(name="August18"),August19Window(name="August19"),Augustweek34Window(name="Augustweek34"),August20Window(name="August20"),August21Window(name="August21"),August22Window(name="August22"),August23Window(name="August23"),August24Window(name="August24"),August25Window(name="August25"),August26Window(name="August26"),Augustweek35Window(name="Augustweek35"),August27Window(name="August27"),August28Window(name="August28"),August29Window(name="August29"),August30Window(name="August30"),August31Window(name="August31"),\
           SeptemberCreateWindow(name="Septembercreate"),Septemberweek35Window(name="Septemberweek35"),September1Window(name="September1"),September2Window(name="September2"),Septemberweek36Window(name="Septemberweek36"),September3Window(name="September3"),September4Window(name="September4"),September5Window(name="September5"),September6Window(name="September6"),September7Window(name="September7"),September8Window(name="September8"),September9Window(name="September9"),Septemberweek37Window(name="Septemberweek37"),September10Window(name="September10"),September11Window(name="September11"),September12Window(name="September12"),September13Window(name="September13"),September14Window(name="September14"),September15Window(name="September15"),September16Window(name="September16"),Septemberweek38Window(name="Septemberweek38"),September17Window(name="September17"),September18Window(name="September18"),September19Window(name="September19"),September20Window(name="September20"),September21Window(name="September21"),September22Window(name="September22"),September23Window(name="September23"),Septemberweek39Window(name="Septemberweek39"),September24Window(name="September24"),September25Window(name="September25"),September26Window(name="September26"),September27Window(name="September27"),September28Window(name="September28"),September29Window(name="September29"),September30Window(name="September30"),\
           OctoberCreateWindow(name="Octobercreate"),Octoberweek40Window(name="Octoberweek40"),October1Window(name="October1"),October2Window(name="October2"),October3Window(name="October3"),October4Window(name="October4"),October5Window(name="October5"),October6Window(name="October6"),October7Window(name="October7"),Octoberweek41Window(name="Octoberweek41"),October8Window(name="October8"),October9Window(name="October9"),October10Window(name="October10"),October11Window(name="October11"),October12Window(name="October12"),October13Window(name="October13"),October14Window(name="October14"),Octoberweek42Window(name="Octoberweek42"),October15Window(name="October15"),October16Window(name="October16"),October17Window(name="October17"),October18Window(name="October18"),October19Window(name="October19"),October20Window(name="October20"),October21Window(name="October21"),Octoberweek43Window(name="Octoberweek43"),October22Window(name="October22"),October23Window(name="October23"),October24Window(name="October24"),October25Window(name="October25"),October26Window(name="October26"),October27Window(name="October27"),October28Window(name="October28"),Octoberweek44Window(name="Octoberweek44"),October29Window(name="October29"),October30Window(name="October30"),October31Window(name="October31"),\
           NovemberCreateWindow(name="Novembercreate"),Novemberweek44Window(name="Novemberweek44"),November1Window(name="November1"),November2Window(name="November2"),November3Window(name="November3"),November4Window(name="November4"),Novemberweek45Window(name="Novemberweek45"),November5Window(name="November5"),November6Window(name="November6"),November7Window(name="November7"),November8Window(name="November8"),November9Window(name="November9"),November10Window(name="November10"),November11Window(name="November11"),Novemberweek46Window(name="Novemberweek46"),November12Window(name="November12"),November13Window(name="November13"),November14Window(name="November14"),November15Window(name="November15"),November16Window(name="November16"),November17Window(name="November17"),November18Window(name="November18"),Novemberweek47Window(name="Novemberweek47"),November19Window(name="November19"),November20Window(name="November20"),November21Window(name="November21"),November22Window(name="November22"),November23Window(name="November23"),November24Window(name="November24"),November25Window(name="November25"),Novemberweek48Window(name="Novemberweek48"),November26Window(name="November26"),November27Window(name="November27"),November28Window(name="November28"),November29Window(name="November29"),November30Window(name="November30"),\
           DecemberCreateWindow(name="Decembercreate"),Decemberweek48Window(name="Decemberweek48"),December1Window(name="December1"),December2Window(name="December2"),Decemberweek49Window(name="Decemberweek49"),December3Window(name="December3"),December4Window(name="December4"),December5Window(name="December5"),December6Window(name="December6"),December7Window(name="December7"),December8Window(name="December8"),December9Window(name="December9"),Decemberweek50Window(name="Decemberweek50"),December10Window(name="December10"),December11Window(name="December11"),December12Window(name="December12"),December13Window(name="December13"),December14Window(name="December14"),December15Window(name="December15"),December16Window(name="December16"),Decemberweek51Window(name="Decemberweek51"),December17Window(name="December17"),December18Window(name="December18"),December19Window(name="December19"),December20Window(name="December20"),December21Window(name="December21"),December22Window(name="December22"),December23Window(name="December23"),Decemberweek52Window(name="Decemberweek52"),December24Window(name="December24"),December25Window(name="December25"),December26Window(name="December26"),December27Window(name="December27"),December28Window(name="December28"),December29Window(name="December29"),December30Window(name="December30"),December31Window(name="December31"),\
           MainWindow(name="main")]
#for RVScreen in screens:
for screen in RVScreens:
    sm.add_widget(screen)
    #root.add_widget(RVScreen(name='RVScreen'))
    #sm.add_widget(RVScreen)
else:
    #sm.add_widget(BBScreen)
    for screen in BBScreens:
        sm.add_widget(screen)
sm.current = "login"




class MainApp(App):
    def build(self):
        #sm = ScreenManager()
        #sm.add_widget(CustomScreen(name='CustomScreen'))
        sm.add_widget(RVScreen(name='RVScreen'))
        #sm.add_widget(BBScreen(name='BBScreen'))
        return sm

if __name__ == "__main__":
    MainApp().run()

