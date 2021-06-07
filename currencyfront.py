import currencyback
import wx

def onclick(click):
    value = float(inputbox.GetValue())
    outputbox.SetLabel(str(currencyback. currency(value)))

app=wx.App()
frame=wx.Frame(parent=None, title= "Currency Converter")
panel=wx.Panel(frame)
size=wx.GridBagSizer()

inputtext= wx.StaticText(panel, label= "Dollars:  ")
inputbox= wx.TextCtrl(panel)
outputtext= wx.StaticText(panel, label="Rupees:  ")
outputbox=wx.StaticText(panel, label= " ")
button= wx.Button(panel, label= "Convert?")
button.Bind(wx.EVT_BUTTON, onclick)

size.Add(inputtext, (0,0))
size.Add(inputbox, (0,1))
size.Add(outputtext, (1,0))
size.Add(outputbox, (1,1))
size.Add(button, (3,1))


frame.SetSizerAndFit(size)
panel.SetSizerAndFit(size)

frame.Show()
app.MainLoop()

