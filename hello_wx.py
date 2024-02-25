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
       
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        imgFile1 = "copy.png"
        img1 = wx.Image(imgFile1, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.btn1 = wx.BitmapButton(
            self, 
            id=-1,
            bitmap = img1,
            size = (img1.GetWidth()+40,  img1.GetHeight()+40)
            )
        
        self.btn1.SetLabel("Copy")
        hbox.Add(self.btn1,0,wx.ALIGN_CENTER)
        self.btn1.Bind(wx.EVT_BUTTON, self.onClickMe)
        
        imgFile2 = "save.png"
        img2 = wx.Image(imgFile2, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.btn2 = wx.BitmapButton(
            self, 
            id=-1,
            bitmap = img2,
            size = (img2.GetWidth()+40,  img2.GetHeight()+40)
            )
        
        self.btn2.SetLabel("Save")
        hbox.Add(self.btn2,0,wx.ALIGN_CENTER)
        self.btn2.Bind(wx.EVT_BUTTON,self.onClickMe)
        
        imgFile3 = "folder.png"
        img3 = wx.Image(imgFile3, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.btn3 = wx.BitmapButton(
            self, 
            id=-1,
            bitmap = img3,
            size = (img3.GetWidth()+40,  img3.GetHeight()+40)
            )
        
        self.btn3.SetLabel("Folder")
        hbox.Add(self.btn3,0,wx.ALIGN_CENTER)
        self.btn3.Bind(wx.EVT_BUTTON, self.onClickMe)
                
        vbox.Add(hbox,1,wx.ALIGN_CENTER)
        
        self.SetSizer(vbox)
        
    def onClickMe(self, event): #event handling
        btn = event.GetEventObject().GetLabel()
        print("Label is " + btn)
        
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, title="Hello World App")
        frame.Show(True)
        return True

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()