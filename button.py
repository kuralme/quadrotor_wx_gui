import wx
import wx.lib.buttons as buttons

class ButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Button Example',
                          size=(300, 100))
        panel = wx.Panel(self, -1)
        self.button = wx.Button(panel, -1, "Hello", pos=(100, 20))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()

    def OnClick(self, event):
        self.button.SetLabel("Clicked")


class BitmapButtonFrame(wx.Frame):
    def __init__(bit):
        wx.Frame.__init__(bit, None, -1, 'Bitmap Button Example',
                          size=(300, 150))
        panel = wx.Panel(bit, -1)
        bmp = wx.Image("bitmap.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        bit.button = wx.BitmapButton(panel, -1, bmp, pos=(10, 20))
        bit.Bind(wx.EVT_BUTTON, bit.OnClick, bit.button)
        bit.button.SetDefault()
        bit.button2 = wx.BitmapButton(panel, -1, bmp, pos=(100, 20),
                                       style=0)
        bit.Bind(wx.EVT_BUTTON, bit.OnClick, bit.button2)

    def OnClick(bit, event):
        bit.Destroy()

class GenericButtonFrame(wx.Frame):
    def __init__(gen):
        wx.Frame.__init__(gen, None, -1, 'Generic Button Example',
                          size=(500, 350))
        panel = wx.Panel(gen, -1)
        sizer = wx.FlexGridSizer(1, 3, 20, 20)
        b = wx.Button(panel, -1, "A wx.Button")
        b.SetDefault()
        sizer.Add(b)
        b = wx.Button(panel, -1, "non-default wx.Button")
        sizer.Add(b)
        sizer.Add((10, 10))
        b = buttons.GenButton(panel, -1, 'Generic Button')
        sizer.Add(b)
        b = buttons.GenButton(panel, -1, 'disabled Generic')
        b.Enable(False)
        sizer.Add(b)
        b = buttons.GenButton(panel, -1, 'bigger')
        b.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD, False))
        b.SetBezelWidth(5)
        b.SetBackgroundColour("Navy")
        b.SetForegroundColour("white")
        b.SetToolTipString("This is a BIG button...")
        sizer.Add(b)
        bmp = wx.Image("bitmap.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        b = buttons.GenBitmapButton(panel, -1, bmp)
        sizer.Add(b)
        b = buttons.GenBitmapToggleButton(panel, -1, bmp)
        sizer.Add(b)
        b = buttons.GenBitmapTextButton(panel, -1, bmp,
                                        "Bitmapped Text", size=(175, 75))
        b.SetUseFocusIndicator(False)
        sizer.Add(b)
        b = buttons.GenToggleButton(panel, -1, "Toggle Button")
        sizer.Add(b)
        panel.SetSizer(sizer)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    #frame = ButtonFrame()
    frame = BitmapButtonFrame()
    #frame = GenericButtonFrame()
    frame.Show()
    app.MainLoop()

