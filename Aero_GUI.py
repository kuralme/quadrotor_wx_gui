import wx
import serial
import struct
import codecs


ser = serial.Serial(
    port='COM6',
    baudrate=230400,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)


const = [""]*4
Kp=8.2
Ki=9.1
Kd=20.4

class Mygui(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Aerobeam PID Tuner',size=(460, 370))
        panel = wx.Panel(self, -1)

        wx.StaticText(panel, -1, "Kp:", (215, 20))
        wx.StaticText(panel, -1, "Ki:", (290, 20))
        wx.StaticText(panel, -1, "Kd:", (365, 20))

        global Kp, Ki, Kd

        #----------------------- Control -------------------------------------------------------------------------------
        self.kp_box = kp_box = wx.TextCtrl(panel, -1, "%1.1f" %Kp , (210, 43), (40, -1))
        kp_box.Bind(wx.EVT_TEXT, self.OnText_1)

        self.slider1 = slider1 = FloatSlider(panel, -1, Kp, 0.0, 20.0, 0.1, pos=(210, 70), size=(-1, 200), style=wx.SL_VERTICAL | wx.SL_AUTOTICKS)
        slider1.SetTickFreq(10)
        slider1.Bind(wx.EVT_SCROLL_CHANGED, self.OnScroll_1)

        #---------------------------------------------------------------------
        self.ki_box = ki_box = wx.TextCtrl(panel, -1, "%1.1f" %Ki, (285, 43), (40, -1))
        ki_box.Bind(wx.EVT_TEXT, self.OnText_2)

        self.slider2 = slider2 = FloatSlider(panel, -1, Ki, 0.0, 20.0, 0.1, pos=(285, 70), size=(-1, 200), style=wx.SL_VERTICAL | wx.SL_AUTOTICKS)
        slider2.SetTickFreq(10)
        slider2.Bind(wx.EVT_SCROLL_CHANGED, self.OnScroll_2)

        # ---------------------------------------------------------------------
        self.kd_box = kd_box = wx.TextCtrl(panel, -1, "%1.1f" %Kd, (360, 43), (40, -1))
        kd_box.Bind(wx.EVT_TEXT, self.OnText_3)

        self.slider3 = slider3 = FloatSlider(panel, -1, Kd, 0.0, 40.0, 0.1, pos=(360, 70), size=(-1, 200), style=wx.SL_VERTICAL | wx.SL_AUTOTICKS)
        slider3.SetTickFreq(20)
        slider3.Bind(wx.EVT_SCROLL_CHANGED, self.OnScroll_3)

        # --------------------------------------------------------------------------------------------------------------------

        #Apply button:  Sends the current PID constants to the system
        self.button = wx.Button(panel, -1, "Apply", pos=(260, 280))
        self.button.Bind(wx.EVT_BUTTON, self.OnClick)

        #Radioboxes
        angles = ['Roll', 'Pitch', 'Yaw']
        self.rb1 = rb1 = wx.RadioBox(panel, -1, "Euler Angle", (20, 25), wx.DefaultSize, angles, 1, wx.RA_SPECIFY_COLS)
        rb1.Bind(wx.EVT_RADIOBOX, self.RadioClick1)
        cs = ['P', 'PI', 'PD', 'PID']
        self.rb2 = rb2 = wx.RadioBox(panel, -1, "Controller Structure", (20, 150), wx.DefaultSize, cs, 1, wx.RA_SPECIFY_COLS)
        rb2.SetSelection(3)
        rb2.Bind(wx.EVT_RADIOBOX, self.RadioClick2)


    def OnText_1(self,event):
        try:
            v = float(self.kp_box.GetValue())
        except:
            return
        if self.slider1.GetValue() == v:
            return
        if self.slider1.GetMin() <= v <= self.slider1.GetMax():
            self.slider1.SetValue(v)

    def OnText_2(self,event):
        try:
            v = float(self.ki_box.GetValue())
        except:
            return
        if self.slider2.GetValue() == v:
            return
        if self.slider2.GetMin() <= v <= self.slider2.GetMax():
            self.slider2.SetValue(v)

    def OnText_3(self,event):
        try:
            v = float(self.kd_box.GetValue())
        except:
            return
        if self.slider3.GetValue() == v:
            return
        if self.slider3.GetMin() <= v <= self.slider3.GetMax():
            self.slider3.SetValue(v)

    def OnScroll_1(self,event):
        self.kp_box.SetValue(str(self.slider1.GetValue()))

    def OnScroll_2(self,event):
        self.ki_box.SetValue(str(self.slider2.GetValue()))

    def OnScroll_3(self,event):
        self.kd_box.SetValue(str(self.slider3.GetValue()))


    def OnClick(self, event):
        self.Kp = Kp = self.slider1.GetValue()
        self.Ki = Ki = self.slider2.GetValue()
        self.Kd = Kd = self.slider3.GetValue()

        if const[0]=="":
             # const[0]=(17.4).hex()
             const[0] =float((ord("R")))

        if const[1]=="" and const[2]=="" and const[3]=="":
            const[1] = Kp
            const[2] = Ki
            const[3] = Kd

        #Serial comm. send the data
        serial_send(const)


    def RadioClick1(self, event):
        if self.rb1.GetStringSelection()=='Roll':
            const[0]= "R"

        if self.rb1.GetStringSelection()=='Pitch':
            const[0] = "P"

        if self.rb1.GetStringSelection()=='Yaw':
            const[0] = "Y"


    def RadioClick2(self, event):
        if self.rb2.GetStringSelection()=='P':
            const[1] = Kp
            const[2] = "0"
            const[3] = "0"
        elif self.rb2.GetStringSelection()=='PI':
            const[1] = Kp
            const[2] = Ki
            const[3] = "0"
        elif self.rb2.GetStringSelection()=='PD':
            const[1] = Kp
            const[2] = "0"
            const[3] = Kd
        elif self.rb2.GetStringSelection()=='PID':
            const[1] = Kp
            const[2] = Ki
            const[3] = Kd


class FloatSlider(wx.Slider):

    def __init__(self, parent, id, value, minval, maxval, res, pos=wx.Position,
                 size=wx.DefaultSize, style=wx.SL_HORIZONTAL,
                 name='floatslider'):
        self._value = value
        self._min = minval
        self._max = maxval
        self._res = res
        ival, imin, imax = [round(v/res) for v in (value, minval, maxval)]
        self._islider = super(FloatSlider, self)
        self._islider.__init__(
            parent, id, ival, imin, imax, pos=pos, size=size, style=style, name=name
        )
        self.Bind(wx.EVT_SCROLL, self._OnScroll)

    def _OnScroll(self, event):
        ival = self._islider.GetValue()
        imin = self._islider.GetMin()
        imax = self._islider.GetMax()
        if ival == imin:
            self._value = self._min
        elif ival == imax:
            self._value = self._max
        else:
            self._value = ival * self._res
        event.Skip()
        #print 'OnScroll: value=%f, ival=%d' % (self._value, ival)

    def GetValue(self):
        return self._value

    def GetMin(self):
        return self._min

    def GetMax(self):
        return self._max

    def GetRes(self):
        return self._res

    def SetValue(self, value):
        self._islider.SetValue(round(value/self._res))
        self._value = value

    def SetMin(self, minval):
        self._islider.SetMin(round(minval/self._res))
        self._min = minval

    def SetMax(self, maxval):
        self._islider.SetMax(round(maxval/self._res))
        self._max = maxval

    def SetRes(self, res):
        self._islider.SetRange(round(self._min/res), round(self._max/res))
        self._islider.SetValue(round(self._value/res))
        self._res = res

    def SetRange(self, minval, maxval):
        self._islider.SetRange(round(minval/self._res), round(maxval/self._res))
        self._min = minval
        self._max = maxval

def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])

def serial_send(data):
    print( data)

    constants = [float_to_hex(data[i]) for i in range(len(data))]
    print(constants)
    val = int('00', 16)
    splitted_data = list(map(''.join, zip(*[iter("".join(constants))] * 2)))

    splitted_data.pop(0)
    splitted_data.pop(4)
    splitted_data.pop(8)
    splitted_data.pop(12)

    new_txt = ""
    for i in splitted_data:
        val = val ^ int(i, 16)
        new_txt += str(chr(int(i, 16)))

    new_txt += str(chr(val))
    new_txt = str(chr(int('A5', 16))) + str(chr(len(splitted_data))) + \
              new_txt + str(chr(int('5A', 16))) + str(chr(int('0A', 16)))
    # print(new_txt)
    new_txt.format(new_txt)

    ser.write(new_txt)


if __name__ == '__main__':
    app = wx.App()
    frame = Mygui()
    frame.Show()
    app.MainLoop()