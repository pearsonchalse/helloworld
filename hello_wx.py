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
       
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.label = wx.StaticText(self, label = "Hello, Toggle")
        sizer.Add(self.label, 0 , wx.EXPAND) 
        
        self.tBtn = wx.ToggleButton(self, label = "Click to On")    
        self.tBtn.SetValue(True)
        sizer.Add(self.tBtn, 0) 
        self.tBtn.Bind(wx.EVT_TOGGLEBUTTON, self.onClickMe) 

        self.SetSizer(sizer)
        
    def onClickMe(self, event): #event handling
        state = event.GetEventObject().GetValue()
        
        if state == True:
            self.label.SetLabelText("Off")
            event.GetEventObject().SetLabel("Click To On")
        else:
            self.label.SetLabelText("On")
            event.GetEventObject().SetLabel("Click To Off")
        
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, title="Hello World App")
        frame.Show(True)
        return True

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()