import wx


class TextFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Text Entry Example',
                          size=(300, 100))
        panel = wx.Panel(self, -1)
        basicLabel = wx.StaticText(panel, -1, "Basic Control:")
        basicText = wx.TextCtrl(panel, -1, "I've entered some text!",
                                size=(175, -1))
        basicText.SetInsertionPoint(0)

        pwdLabel = wx.StaticText(panel, -1, "Password:")
        pwdText = wx.TextCtrl(panel, -1, "password",
                              size=(175, -1), style=wx.TE_PASSWORD)
        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([basicLabel, basicText, pwdLabel, pwdText])
        panel.SetSizer(sizer)

class RichFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Text Entry Example',
                          size=(300, 250))
        panel = wx.Panel(self, -1)
        multiLabel = wx.StaticText(panel, -1, "Multi-line")
        multiText = wx.TextCtrl(panel, -1,
                                "Here is a looooooooooooooong line "
                                "of text set in the control.\n\n"
                                "See that it wrapped, and that "
                                "this line is after a blank",
                                size=(200, 100), style=wx.TE_MULTILINE)
        multiText.SetInsertionPoint(0)
        richLabel = wx.StaticText(panel, -1, "Rich Text")
        richText = wx.TextCtrl(panel, -1,
                               "If supported by the native control, "
                               "this is reversed, and this is a different font.",
                               size=(200, 100),
                               style=wx.TE_MULTILINE | wx.TE_RICH2)
        richText.SetInsertionPoint(0)
        richText.SetStyle(44, 52, wx.TextAttr("white", "black"))
        points = richText.GetFont().GetPointSize()
        f = wx.Font(points + 3, wx.ROMAN,
                    wx.ITALIC, wx.BOLD, True)
        richText.SetStyle(68, 82, wx.TextAttr("blue",
                                              wx.NullColour, f))
        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([multiLabel, multiText, richLabel, richText])
        panel.SetSizer(sizer)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = TextFrame()
    #frame = RichFrame()
    frame.Show()
    app.MainLoop()






