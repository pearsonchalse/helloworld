import sys
sys.path.append("c:\\users\\realn\\anaconda3\\lib\\site-packages")


import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))
        
        panel = wx.Panel(self)
        text = wx.StaticText(panel, label="Hello World", pos=(100, 50))

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, title="Hello World App")
        frame.Show(True)
        return True

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()