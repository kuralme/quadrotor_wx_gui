import wx

class MyPanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id, wx.DefaultPosition, wx.DefaultSize)
        self.parent = parent

        self.UserMinValue = 0
        self.UserMaxValue = 10
        self.UserValue = 0.0

        self.SliderMinValue = 0
        self.SliderMaxValue = 100
        self.SliderValue = 0

        self.statxt1 = wx.StaticText(self, wx.ID_ANY, 'left',
                                     style=wx.ST_NO_AUTORESIZE | wx.ALIGN_LEFT)
        self.statxt2 = wx.StaticText(self, wx.ID_ANY, 'middle',
                                     style=wx.ST_NO_AUTORESIZE | wx.ALIGN_CENTRE)
        self.statxt3 = wx.StaticText(self, wx.ID_ANY, 'right',
                                     style=wx.ST_NO_AUTORESIZE | wx.ALIGN_RIGHT)

        self.statxt1.SetLabel(str(self.UserMinValue))
        self.statxt2.SetLabel(str(self.UserValue))
        self.statxt3.SetLabel(str(self.UserMaxValue))

        self.slider = wx.Slider(self, wx.ID_ANY, self.SliderValue, \
                                self.SliderMinValue, self.SliderMaxValue, \
                                style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS)
        self.slider.SetTickFreq(10)

        self.slider.Bind(wx.EVT_SCROLL, self.OnScroll)

        b = 20
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(self.statxt1, 1, wx.RIGHT, b)
        hsizer1.Add(self.statxt2, 1, wx.LEFT | wx.RIGHT, b)
        hsizer1.Add(self.statxt3, 1, wx.LEFT, b)

        b = 4
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(hsizer1, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(self.slider, 0, wx.EXPAND | wx.LEFT | wx.TOP | wx.BOTTOM, b)

        self.SetSizerAndFit(vsizer1)
        self.parent.SetClientSize((500, vsizer1.GetSize()[1]))
        self.parent.CentreOnScreen()



    def OnScroll(self, event):
        self.SliderValue = self.slider.GetValue()
        self.UserValue = self.SliderValue / 10.0
        self.statxt2.SetLabel(str(self.UserValue))



#--------------------------------------------------------------------

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        title = 'Slider...'
        pos = wx.DefaultPosition
        size = wx.DefaultSize
        sty = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, parent, id, title, pos, size, sty)

        self.panel = MyPanel(self, wx.NewId())

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseWindow(self, event):
        self.Destroy()


#--------------------------------------------------------------------

app = wx.App()
frame = MyFrame(None, wx.ID_ANY)
frame.Show()
app.MainLoop()