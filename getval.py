import wx

########################################################################
class MyFrame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, parent=None, title="Example")
        panel = wx.Panel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)

        self.text = wx.TextCtrl(panel)
        sizer.Add(self.text, 0, wx.ALL|wx.EXPAND, 5)

        button = wx.Button(panel, label="Get Value")
        button.Bind(wx.EVT_BUTTON, self.onButton)
        sizer.Add(button, 0, wx.ALL, 2)

        panel.SetSizer(sizer)
        self.Show()

    #----------------------------------------------------------------------
    def onButton(self, event):
        """"""
        print(self.text.GetValue())

#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()