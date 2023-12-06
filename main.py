from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.anchorlayout import MDAnchorLayout
# ----------------------------------------------------
from kivymd.uix.list import ThreeLineIconListItem,IconLeftWidgetWithoutTouch
from kivymd.uix.list import MDList 
from kivymd.uix.scrollview import MDScrollView
from kivy.properties import ObjectProperty
# --------------------------------------------
import os
import time  
import psutil
# --------------Builder------------------------
Builder.load_file('style.kv')
# -------------------Global---------------------
global_ld=[]
global_address='' 
# ------------------STYLE & Calculator------------------------
class FileManagerZ(MDScrollView):
    register=ObjectProperty()
    def __init__(self,*args,**kwargs):
        super(FileManagerZ,self).__init__(*args,**kwargs)
    def find_disks(self):
        partitions=psutil.disk_partitions()
        for partition in partitions:
            global_ld.append(partition[0])
    def create_disks(self):
        try:
            self.register.clear_widgets()
            self.find_disks()
            for ld in global_ld:
                name=ld 
                address=ld 
                list_file=os.listdir(address)
                items=str(len(list_file))
                td=os.path.getmtime(address)
                td=time.ctime(td)
                date=td
                self.register.add_widget(ThreeLineIconListItem(
                    IconLeftWidgetWithoutTouch(icon='folder-home'),
                    text=name,
                    secondary_text=items,
                    tertiary_text=date, 
                ))
                self.goto_items(list_file,address)
        except:pass
    def goto_items(self,list_file,address):
        try:
            for file_name in list_file:
                if '.' not in file_name and ' ' not in file_name:
                    at=address
                    at+=file_name
                    lt=os.listdir(at)
                    tt=os.path.getmtime(at)
                    tt=time.ctime(tt)
                    self.register.add_widget(ThreeLineIconListItem(
                        IconLeftWidgetWithoutTouch(icon='folder'),
                        text=file_name,
                        secondary_text=str(len(lt)),
                        tertiary_text=tt, 
                    ))
                elif ' ' not in file_name:
                    at=address
                    at+=file_name 
                    tt=os.path.getmtime(at)
                    tt=time.ctime(tt)
                    s=os.path.getsize(at)
                    z=self.return_size(s)
                    self.register.add_widget(ThreeLineIconListItem(
                        IconLeftWidgetWithoutTouch(icon='file'),
                        text=file_name,
                        secondary_text=str(z[0])+z[1],
                        tertiary_text=tt, 
                    ))
                else:
                    pass 
        except:pass 
    def return_size(self,size):
        s=size
        if len(str(s))<=3:
            return([s,'B'])
        elif len(str(s))<=6:
            s=float(s/1024)
            ts=str(s)
            n=ts.find('.')
            s=ts[0:n+2+1]
            return([s,'KB'])
        elif len(str(s))<=9:
            s=float(s/(1024*1024))
            ts=str(s)
            n=ts.find('.')
            s=ts[0:n+2+1]
            return([s,'MB'])
        elif len(str(s))<=12:
            s=float(s/(1024*1024*1024))
            ts=str(s)
            n=ts.find('.')
            s=ts[0:n+2+1]
            return([s,'GB'])
        elif len(str(s))<=15:
            s=float(s/(1024*1024*1024*1024))
            ts=str(s)
            n=ts.find('.')
            s=ts[0:n+2+1]
            return([s,'TB'])
        else:pass    
# -------------------------------------------------
class Style(MDAnchorLayout):
    mn=ObjectProperty() 
    def __init__(self,*args,**kwargs):
        super(Style,self).__init__(*args,**kwargs) 
#------------------APP-----------------------
class MainApp(MDApp):
    def __init__(self,*args,**kwargs):
        super(MainApp,self).__init__(*args,**kwargs)
#=================================
        # self.fmz=FileManagerZ()
    def build(self):
        self.theme_cls.theme_style='Dark'
        return Style()
# ===============================
    # def on_start(self):
#         self.fmz.create_disks()
# ------------------------------------------------
MainApp().run()