import wx

class tcsl(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Slider-Text',size=(300, 200))
        panel = wx.Panel(self, -1)

        self.tc = tc = wx.TextCtrl(panel, -1, "Enter an integer here", pos=(30, 10),
                                size=(175, -1))
        tc.Bind(wx.EVT_TEXT, self.OnText)

        self.sl = sl = wx.Slider(panel, 20, 0, 0, 20, pos=(30, 60),
                           size=(200, -1),
                           style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS)
        sl.Bind(wx.EVT_SCROLL, self.OnScroll)

    def OnText(self, evt):
        try:
            v = int(self.tc.GetValue())
        except:
            return
        if self.sl.GetValue() == v:
            return
        if self.sl.GetMin() <= v <= self.sl.GetMax():
            self.sl.SetValue(v)

    def OnScroll(self, evt):
        try:
            v = int(self.tc.GetValue())
        except:
            return
        if self.sl.GetValue() == v:
            return
        self.tc.SetValue(str(self.sl.GetValue()))


if __name__ == '__main__':
    app = wx.App()
    frame = tcsl()
    frame.Show()
    app.MainLoop()