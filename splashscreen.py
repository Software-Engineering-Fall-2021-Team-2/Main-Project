import wx
import wx.adv


class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,  size=(500, 500))

        bitmap = wx.Bitmap('logo.jpg')
        splash = wx.adv.SplashScreen(
            bitmap,
            wx.adv.SPLASH_CENTER_ON_SCREEN | wx.adv.SPLASH_TIMEOUT,
            3000, self)
        splash.Show()




# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop