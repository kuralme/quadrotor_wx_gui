import wx

class Examples(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Example',
                          size=(340, 320))
        panel = wx.Panel(self, -1)
        self.count = 0
        global k,slider1,slider2,rb

        #Slider
        slider1 = wx.Slider(panel, 20, 10, 1, 20, pos=(30, 10),
                           size=(200, -1),
                           style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS)
        slider1.SetTickFreq(5)
        # -----------------------------------------------------
        slider2 = wx.Slider(panel, 100, 25, 1, 100, pos=(250, 50),
                           size=(-1, 200),
                           style=wx.SL_VERTICAL | wx.SL_AUTOTICKS | wx.SL_LABELS)
        slider2.SetTickFreq(10)
        button = wx.Button(panel, -1, "Show", pos=(170, 210))
        button.Bind(wx.EVT_BUTTON, self.OnClick)

        #Spinner
        sc = wx.SpinCtrl(panel, -1, "", (30, 80), (60, -1))
        sc.SetRange(1.2, 100.1)
        sc.SetValue(5.1)

        #Checkbox
        cb1 = wx.CheckBox(panel, -1, "Alpha", (35, 140), (70, 20))
        cb2 = wx.CheckBox(panel, -1, "Beta", (35, 160), (70, 20))
        cb3 = wx.CheckBox(panel, -1, "Gamma", (35, 180), (70, 20))
        cb1.SetValue(1)

        #Radiobox
        sampleList = ['zero', 'one', 'two']
        rb = wx.RadioBox(panel, -1, "A Radio Box", (130, 70), wx.DefaultSize,
                    sampleList, 1, wx.RA_SPECIFY_COLS)
        rb.Bind(wx.EVT_RADIOBOX, self.RadioClick)

        #Choice box
        sampleList = ['zero', 'one', 'two', 'three', 'four', 'five',
                      'six', 'seven', 'eight']
        wx.StaticText(panel, -1, "Select one:", (15, 230))
        wx.ComboBox(panel, -1, "default value", (80, 230), (80, 30), sampleList, wx.CB_DROPDOWN)



    def OnClick(self, event):
        #self.button.SetLabel("Clicked")
        print(slider2.GetValue())

    def RadioClick(self, event):
        print(rb.GetStringSelection())


if __name__ == '__main__':
    app = wx.App()
    frame = Examples()
    frame.Show()
    app.MainLoop()