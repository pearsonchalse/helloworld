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
        gridsizer = wx.GridSizer(4,4,15,15)
        
        for i in range (1,17):
            lbl = "Btn" + str(i)
            
            gridsizer.Add(wx.Button(self, label=lbl), 0, wx.EXPAND)

        self.SetSizer(gridsizer)
        
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, title="Hello World App")
        frame.Show(True)
        return True

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()