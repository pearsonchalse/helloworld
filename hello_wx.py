import sys
sys.path.append("c:\\users\\realn\\anaconda3\\lib\\site-packages")


import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))
        
        #panel - 1st way
        #panel = wx.Panel(self)
        #text = wx.StaticText(panel, label="Hello World", pos=(100, 50))

        #2nd way
        panel = MyPanel(self)
        
class MyPanel(wx.Panel):
    def __init__(self,parent):
        super(MyPanel, self).__init__(parent)
        """ Youtube example
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
                
        label1 = wx.StaticText(self, label = "Hello, Label-1", style = wx.ALIGN_CENTER)        
        vbox.Add(label1,0,wx.EXPAND)
        
        label2 = wx.StaticText(self, label = "Hello, Label-2", style = wx.ALIGN_CENTER)
        vbox.Add(label2,0,wx.EXPAND)
        
        label3 = wx.StaticText(self, label = "Hello, Label-3^^^", style = wx.ALIGN_CENTER)
        hbox.Add(label3,0,wx.EXPAND)
        
        label4 = wx.StaticText(self, label = "Hello, Label-4^^^^", style = wx.ALIGN_CENTER)
        hbox.Add(label4,0,wx.EXPAND)
        hbox.AddStretchSpacer()
        
        vbox.Add(hbox, 1, wx.ALL)
        
        self.SetSizer(vbox)        
        """
        
        """
        # https://hexa-coding.tistory.com/16
        """
        vbox = wx.BoxSizer(wx.VERTICAL)
        #wx.VERTICAL : 세로로 쌓겠다.
        #wx.HORIZONTAL : 가로로 쌓겠다.
        
        button1 = wx.Button(self, id=1, label='Button1')
        button2 = wx.Button(self, id=2, label='Button2')

        
        """
        window : 사이저에 추가할 대상을 지정합니다.
        proportion: 박스사이저에서 위젯 크기가 차지하는 비중이다. 
            사이저가 HORIZONTAL 배열이면 가로방향 전체 길이에서 위젯의 비율을 의미하고, VERTICAL이면 세로방향 전체 길이에서 위젯 세로길이 비율을 의미한다. proportion=0이면, 위젯 크기 비율의 증가/감소 없이 위젯 자체 크기를 그대로 사용하겠다는 의미이다. 자세한 부분은 예제를 통해 확인해보자. 
        flag: 박스사이저 위젯의 border 두께가 적용되는 영역
            (wx.LEFT, wx.RIGHT, wx.TOP, wx.BOTTOM)을 결정하고, 
            프레임의 크기가 변경되었을 때 위젯 크기도 그에 따라 변하게 되는 
            wx.EXPAND 등을 설정할 수 있다. 
        border: 위젯과 박스사이저 가장자리 사이 두께이다. 
        """
                
        vbox.Add(button1, proportion=0, flag=wx.LEFT, border=5)
        vbox.Add(button2, proportion=0, flag=wx.EXPAND, border=0)
        
        
        self.SetSizer(vbox)
        
        

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, title="Hello World App")
        frame.Show(True)
        return True

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()