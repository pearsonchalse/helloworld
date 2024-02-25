import sys
sys.path.append("c:\\users\\realn\\anaconda3\\lib\\site-packages")


import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))
        
        #2nd way
        panel = MyPanel(self)
        
class MyPanel(wx.Panel):
    def __init__(self,parent):
        super(MyPanel, self).__init__(parent)
       
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.label = wx.StaticText(self, label = "Hello, Label!")
        sizer.Add(self.label, 1 , wx.EXPAND) # 1 : 비율 / 아래 0 과 비교
        
        self.button = wx.Button(self, label = "Btn!!!")    
        sizer.Add(self.button, 0) # 0 : 비율 / 위 1 과 비교
        self.button.Bind(wx.EVT_BUTTON, self.onClickMe) # event handler 

        self.SetSizer(sizer)
        
    def onClickMe(self, event): #event handling
        self.label.SetLabelText("Text has been changed!")
        
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, title="Hello World App")
        frame.Show(True)
        return True

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()