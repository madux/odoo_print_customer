#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      kingston
#
# Created:     11/11/2015
# Copyright:   (c) kingston 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      kingston
#
# Created:     11/11/2015
# Copyright:   (c) kingston 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import wx
import wx.lib.agw.gradientbutton as gbtn
import wx.lib.agw.supertooltip as supertooltip
import  time
import wx.grid as gridlib
import os
import wx.media

import  wx.gizmos   as  gizmos
import glob

import subprocess


from ObjectListView import ObjectListView, ColumnDefn


class PanelOne(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

        self.SetBackgroundColour('#000000')

        sizer = wx.GridBagSizer(0, 0)

        gool = '\xe5\xb1(x + 5) = y\xb2  = \xe5\x7c'
        goo = u'\u20ac'

        text3 = wx.StaticText(self, -1, gool)
        sizer.Add(text3, (3, 18),(1,1), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=15)
        text3.SetFont(wx.Font(15, wx.ROMAN, wx.NORMAL, wx.BOLD))


        help3 =gbtn.GradientButton(self,1,label=" Coupon  ",
                                  bitmap=wx.Bitmap
                                  ("ima/network.png",wx.BITMAP_TYPE_PNG))
        sizer.Add(help3, (3, 6), flag=wx.LEFT|wx.RIGHT, border=5)

        help4= gbtn.GradientButton(self,19,label="Shop File",
                                  bitmap=wx.Bitmap
                                  ("ima/market.png",wx.BITMAP_TYPE_PNG))
        sizer.Add(help4, (3, 7), flag=wx.LEFT|wx.RIGHT, border=5)

        helpi= gbtn.GradientButton(self,23, label="  Audio  ",
                                  bitmap=wx.Bitmap
                                  ("ima/route.png",wx.BITMAP_TYPE_PNG))
        sizer.Add(helpi, (3, 8), flag=wx.LEFT|wx.RIGHT, border=5)

        helpk= gbtn.GradientButton(self,label="Cloud File",
                                  bitmap=wx.Bitmap
                                  ("ima/wifi.png",wx.BITMAP_TYPE_PNG))
        sizer.Add(helpk, (3, 9), flag=wx.LEFT|wx.RIGHT, border=5)



        help5 = gbtn.GradientButton(self,121,label=" Favourite",
                                  bitmap=wx.Bitmap
                                  ("ima/speedometer.png",wx.BITMAP_TYPE_PNG))
        sizer.Add(help5, (5, 6), flag=wx.LEFT|wx.RIGHT, border=5)

        help6 = gbtn.GradientButton(self,label=" History ",
                                  bitmap=wx.Bitmap
                                  ("ima/his.png",wx.BITMAP_TYPE_PNG))
        sizer.Add(help6, (5, 7), flag=wx.LEFT|wx.RIGHT, border=5)

        help7 = gbtn.GradientButton(self,34, label="Video-s  ",
                                  bitmap=wx.Bitmap
                                  ("ima/video_clip.png",wx.BITMAP_TYPE_PNG))
        sizer.Add(help7, (5, 8), flag=wx.LEFT|wx.RIGHT, border=5)


        helpy = gbtn.GradientButton(self,9, label="Transfers ",
                                  bitmap=wx.Bitmap
                                  ("ima/transfer.png",wx.BITMAP_TYPE_PNG))
        sizer.Add(helpy, (5, 9), flag=wx.LEFT|wx.RIGHT, border=5)

        helpu=gbtn.GradientButton(self,1,label="Sign-Up", bitmap = wx.Bitmap("ima/moneyS.png", wx.BITMAP_TYPE_PNG))

        sizer.Add(helpu, (15, 18), flag=wx.LEFT|wx.RIGHT, border=5)



        led = gizmos.LEDNumberCtrl(self, -1, (0,0),  (280, 50))# | gizmos.LED_DRAW_FADED)


        sizer.Add(led, (15, 10), (1, 5), flag=wx.LEFT|wx.RIGHT, border=5)

###########################################################################
#Bindings
        #self.Bind(wx.EVT_BUTTON, self.onSwitchPanels, id = 121)
###########################################################################

        self.clock = led
        self.OnTimer(None)

        self.timer = wx.Timer(self)
        self.timer.Start(1000)
        self.Bind(wx.EVT_TIMER, self.OnTimer)




        helpu.SetToolTipString('Sign-up')
        helpy.SetToolTipString('Check Transfer')
        help7.SetToolTipString('Choose Video')
        help6.SetToolTipString('Media History')
        help5.SetToolTipString('Available Songs')
        helpk.SetToolTipString('Transfer Files')
        helpi.SetToolTipString('Play Audio Files')
        help4.SetToolTipString('Media Stores')
        help3.SetToolTipString('Album')

        self.SetSizerAndFit(sizer)
        self.Centre()
        self.Show(True)

    def OnTimer(self, event):
        t = time.localtime(time.time())
        st = time.strftime("%I - %M -%S", t)
        self.clock.SetValue(st)

########################################################################
class File(object):
    """
    Model of the file object
    """

    #----------------------------------------------------------------------
    def __init__(self, pathw):
        """Constructor"""

        self.filename = os.path.basename(pathw)
        self.path = pathw


########################################################################

class PanelTwo(wx.ScrolledWindow):
    def __init__(self, parent):
        wx.ScrolledWindow.__init__(self,parent = parent)
        self.SetBackgroundColour('BLACK')
        self.SetScrollbars( 20, 20, 55, 40)
        self.Scroll( 0, 0)

        self.Show( )



        hbox = wx.BoxSizer(wx.HORIZONTAL)
        pnl1 = wx.Panel(self, -1, style = wx.SIMPLE_BORDER)

        #pnl1.Bind(wx.EVT_SCROLLWIN, self.OnScroll)
        #first = pnl1.SetScrollbar(wx.VERTICAL, 0, 6, 50);



        pnl2 = wx.Panel(self, -1, style = wx.SIMPLE_BORDER)
        pnl3 = wx.Panel(self, -1, style = wx.SIMPLE_BORDER)
        pnl4 = wx.Panel(self, -1, style = wx.SIMPLE_BORDER)

        hbox.Add(pnl1, 1, wx.EXPAND | wx.ALL, 3)
        hbox.Add(pnl2, 1, wx.EXPAND | wx.ALL, 3)
        hbox.Add(pnl3, 1, wx.EXPAND | wx.ALL, 3)
        hbox.Add(pnl4, 1, wx.EXPAND | wx.ALL, 3)

        siz = wx.GridBagSizer (4,4)

        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.data = []

        # -----------------------------------------------
        # create the widgel.ts

        # add the data viewing control
        self.pdfOlv = ObjectListView(pnl1,
                                     style=wx.LC_REPORT|wx.SUNKEN_BORDER)

### USE TO MAKE LIST OF ITEM DOUBLE CLICK AND OPEN
        self.pdfOlv.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onDoubleClick)

### FIRST THING TO DISPLAY IF NOTHING IS LOADED
        self.pdfOlv.SetEmptyListMsg("No PDFs Found!")
        self.updateDisplay()

        browseBtn = wx.Button(pnl1, label="Browse")
        browseBtn.Bind(wx.EVT_BUTTON, self.getPdfs)



        # -----------------------------------------------
        # layout the widgets
        mainSizer = wx.BoxSizer(wx.VERTICAL)

        mainSizer.Add(self.pdfOlv, 1, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(browseBtn, 0, wx.ALL|wx.CENTER, 5)

        self.SetSizer(mainSizer)


        # -----------------------------------------------
        # layout the widgets
        mainSizer = wx.BoxSizer(wx.VERTICAL)

        mainSizer.Add(self.pdfOlv, 1, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(browseBtn, 0, wx.ALL|wx.CENTER, 5)

        self.SetSizer(mainSizer)


##########################################################################################################################################
                                                                                                                                    ##   #
#Panel 2 Button Starts Here

        siz2 = wx.GridBagSizer(4, 4)
        movbtn21 = gbtn.GradientButton(pnl2, 1, label = 'Better', bitmap = wx.Bitmap("ima/mov.jpg", wx.BITMAP_TYPE_JPEG))
        siz2.Add(movbtn21, (1, 1), flag=wx.LEFT|wx.RIGHT, border = 5)

        movbtn31 = gbtn.GradientButton(pnl2, 1, label = 'Drills  ', bitmap = wx.Bitmap("ima/mov17.jpg", wx.BITMAP_TYPE_JPEG))
        siz2.Add(movbtn31, (2, 0), flag=wx.LEFT|wx.RIGHT, border = 5)

        movbtn41 = gbtn.GradientButton(pnl2, 1, label = 'Freed', bitmap = wx.Bitmap("ima/mov23.jpg", wx.BITMAP_TYPE_JPEG))
        siz2.Add(movbtn41, (3, 0), flag=wx.LEFT|wx.RIGHT, border = 5)
        movbtn51 = gbtn.GradientButton(pnl2, 1, label = 'Billz ', bitmap = wx.Bitmap("ima/mov6.jpg", wx.BITMAP_TYPE_JPEG))
        siz2.Add(movbtn51, (4, 0), flag=wx.LEFT|wx.RIGHT, border = 5)
        movbtn61 = gbtn.GradientButton(pnl2, 1, label = 'Drills', bitmap = wx.Bitmap("ima/mov7.jpg", wx.BITMAP_TYPE_JPEG))
        siz2.Add(movbtn61, (5, 0), flag=wx.LEFT|wx.RIGHT, border = 5)
        movbtn71 = gbtn.GradientButton(pnl2, 1, label = 'Drills', bitmap = wx.Bitmap("ima/mov8.jpg", wx.BITMAP_TYPE_JPEG))
        siz2.Add(movbtn71, (6, 0), flag=wx.LEFT|wx.RIGHT, border = 5)
        movbtn81 = gbtn.GradientButton(pnl2, 1, label = 'Drills', bitmap = wx.Bitmap("ima/mov9c.jpg", wx.BITMAP_TYPE_JPEG))
        siz2.Add(movbtn81, (7, 0), flag=wx.LEFT|wx.RIGHT, border = 5)

##########################################################################################################################################
##########################################################################################################################################

#Panel 3 Button Starts Here

        siz3 = wx.GridBagSizer(4, 4)
        movbtn211 = gbtn.GradientButton(pnl3, 1, label = 'Better', bitmap = wx.Bitmap("ima/mov17.jpg", wx.BITMAP_TYPE_JPEG))
        siz3.Add(movbtn211, (1, 1), flag=wx.LEFT|wx.RIGHT, border = 5)

        movbtn311 = gbtn.GradientButton(pnl3, 1, label = 'Drills  ', bitmap = wx.Bitmap("ima/mov.jpg", wx.BITMAP_TYPE_JPEG))
        siz3.Add(movbtn311, (2, 0), flag=wx.LEFT|wx.RIGHT, border = 5)

        movbtn411 = gbtn.GradientButton(pnl3, 1, label = 'Freed', bitmap = wx.Bitmap("ima/mov6.jpg", wx.BITMAP_TYPE_JPEG))
        siz3.Add(movbtn411, (3, 0), flag=wx.LEFT|wx.RIGHT, border = 5)
        movbtn511 = gbtn.GradientButton(pnl3, 1, label = 'Billz ', bitmap = wx.Bitmap("ima/mov23.jpg", wx.BITMAP_TYPE_JPEG))
        siz3.Add(movbtn511, (4, 0), flag=wx.LEFT|wx.RIGHT, border = 5)
        movbtn611 = gbtn.GradientButton(pnl3, 1, label = 'Drills', bitmap = wx.Bitmap("ima/mov8.jpg", wx.BITMAP_TYPE_JPEG))
        siz3.Add(movbtn611, (5, 0), flag=wx.LEFT|wx.RIGHT, border = 5)
        movbtn711 = gbtn.GradientButton(pnl3, 1, label = 'Drills', bitmap = wx.Bitmap("ima/mov7.jpg", wx.BITMAP_TYPE_JPEG))
        siz3.Add(movbtn711, (6, 0), flag=wx.LEFT|wx.RIGHT, border = 5)
        movbtn811 = gbtn.GradientButton(pnl3, 1, label = 'Drills', bitmap = wx.Bitmap("ima/mov9c.jpg", wx.BITMAP_TYPE_JPEG))
        siz3.Add(movbtn811, (7, 0), flag=wx.LEFT|wx.RIGHT, border = 5)

########################################################################################################################################


##########################################################################################################################################
                                                                                                                                  ##   #
#Panel 4 Button Starts Here

        siz4 = wx.GridBagSizer(4, 4)
        movbtn2111 = gbtn.GradientButton(pnl4, 1, label = 'Better', bitmap = wx.Bitmap("ima/mov.jpg", wx.BITMAP_TYPE_JPEG))
        siz4.Add(movbtn2111, (1, 1), flag=wx.LEFT|wx.RIGHT, border = 5)

        movbtn3111 = gbtn.GradientButton(pnl4, 1, label = 'Drills  ', bitmap = wx.Bitmap("ima/mov23.jpg", wx.BITMAP_TYPE_JPEG))
        siz4.Add(movbtn3111, (2, 0), flag=wx.LEFT|wx.RIGHT, border = 5)

        movbtn4111 = gbtn.GradientButton(pnl4, 1, label = 'Freed', bitmap = wx.Bitmap("ima/mov17.jpg", wx.BITMAP_TYPE_JPEG))
        siz4.Add(movbtn4111, (3, 0), flag=wx.LEFT|wx.RIGHT, border = 5)
        movbtn5111 = gbtn.GradientButton(pnl4, 1, label = 'Billz ', bitmap = wx.Bitmap("ima/mov8.jpg", wx.BITMAP_TYPE_JPEG))
        siz4.Add(movbtn5111, (4, 0), flag=wx.LEFT|wx.RIGHT, border = 5)
        movbtn6111 = gbtn.GradientButton(pnl4, 1, label = 'Drills', bitmap = wx.Bitmap("ima/mov9c.jpg", wx.BITMAP_TYPE_JPEG))
        siz4.Add(movbtn6111, (5, 0), flag=wx.LEFT|wx.RIGHT, border = 5)
        movbtn7111 = gbtn.GradientButton(pnl4, 1, label = 'Drills', bitmap = wx.Bitmap("ima/mov6.jpg", wx.BITMAP_TYPE_JPEG))
        siz4.Add(movbtn7111, (6, 0), flag=wx.LEFT|wx.RIGHT, border = 5)
        movbtn8111 = gbtn.GradientButton(pnl4, 1, label = 'Drills', bitmap = wx.Bitmap("ima/mov7.jpg", wx.BITMAP_TYPE_JPEG))
        siz4.Add(movbtn8111, (7, 0), flag=wx.LEFT|wx.RIGHT, border = 5)

########################################################################################################################################







        self.SetSize((400, 120))
        self.SetSizer(hbox)
        self.Centre()


        #siz.AddGrowableRow(1)
        #siz.AddGrowableCol(2)
        #pnl1.SetSizer(siz)
        pnl2.SetSizer(siz2)
        pnl3.SetSizer(siz3)
        pnl4.SetSizer(siz4)

    #def OnScroll(self, evt):

        #pnl1.Scroll(50,10)
    def updateDisplay(self):
        """
        Updates the object list view control
        """
        self.pdfOlv.SetColumns([
            ColumnDefn("Files", "left", 300, "filename"),
            ColumnDefn("Title", "left", 120, "title"),
            ColumnDefn("Size (MB)", "center", 100, "GetSizeInMb"),
            ColumnDefn("Last Played", "left", 100, "lastPlayed"),
            ColumnDefn("Rating", "center", 100, "rating")
            ])
        self.pdfOlv.SetObjects(self.data)


    def getPdfs(self, event):
        """
        Attempts to load PDFs into objectlistview
        """
        self.dataq = []

        dlg = wx.DirDialog(self, "UCNET SOUND LIBRARY:",'c:/users/kingston/documents/job/testor_player/bitmaps',
                          style=wx.DD_DEFAULT_STYLE)
        res = dlg.ShowModal()
        if res != wx.ID_OK:
            return
        path = dlg.GetPath()
        dlg.Destroy()

#### Only display pdf  files


        pdfs = glob.glob(path + "/*.mp3")

        if pdfs:
            for pdf in pdfs:
                self.data.append(File(pdf))

            self.updateDisplay()


    #----------------------------------------------------------------------
    def onDoubleClick(self, event):
        """
        Opens the PDF that is double-clicked
        """
        obj = self.pdfOlv.GetSelectedObject() # USE THIS TO GET EVENT OF DOUBLE CLICKED FILE
        print "You just double-clicked on %s" % obj.path


        mess = onPlayer(self, -1, "Player")

        mess.Show(True)

        mc = mediactrl

#####################################################################################################
# MEDIA CONTROL HERE

    def symbol(self, event):
        sym = Symbols(None, -1, "Administration Point")
        sym.Show(True)


class onPlayer(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title,size = (400, 280))
        panel = wx.Panel(self, -1)
        sizer = wx.GridBagSizer(0,0)
        u = '\u03d2'

        r = u'\u03d2'
        t = u'\u03b2'
        ti = u'\u03c0'
        we = u'\u0192'
        tr = u'\u00b1'
        qw = u'\u1f68'
        q = u'\u2030'
        ol = u'\u2071'
        gi = u'\u2072'
        po = u'\u2073'
        qr = u'\u2074'
        pp = u'\u2075'
        rt = u'\u2076'
        hl = u'\u2079'
        lp = u'\u2078'
        px = u'\u2070'
        tip = u'\u2080'
        asl = u'\u2081'
        df = u'\u2082'
        ki = u'\u2083'
        ui = u'\u2084'
        az = u'\u2085'
        sh =u'\u2086'
        ah =u'\u2087'


        a1 =u'\u2153'
        a2 =u'\u2152'
        a3 =u'\u2154'
        a4 =u'\u2155'
        a5 =u'\u2156'
        a6 =u'\u2157'
        a7 =u'\u2158'
        a8 =u'\u2159'
        a9 =u'\u1f68'
        b1 =u'\u20a6'
        b2 =u'\u20a4'

        b3 =u'\u20ac'
        b5 = u'\u20dd'
        b6 =u'\u20b5'
        b7 =u'\u212e'
        b8 =u'\u2211'
        b9 =u'\u2260'
        c1 =u'\u222b'
        c2 =u'\u2229'

        c3 =u'\u2321'
        c4 =u'\u2190'
        c5 =u'\u2199'





        self.help1 =wx.Button(panel,1,label=ah)
        sizer.Add(self.help1, (0, 0), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help1.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))
        self.Bind(wx.EVT_BUTTON, self.Kiss, self.help1)


        self.help3 =wx.Button(panel,1,label=sh)
        sizer.Add(self.help3, (0, 1 ), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help3.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))



        self.help2 =wx.Button(panel,1,label=az)
        sizer.Add(self.help2, (0, 2), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help2.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))



        self.help3 =wx.Button(panel,1,label=ui)
        sizer.Add(self.help3, (0, 3), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help3.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))



        self.help4 = wx.Button(panel,1,label=ki)
        sizer.Add(self.help4, (0, 4), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help4.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))


        self.help5 =wx.Button(panel,1,label=df)
        sizer.Add(self.help5, (1, 0), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help5.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))





        self.help6 =wx.Button(panel,1,label=asl)
        sizer.Add(self.help6, (1, 1), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help6.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))



        self.help7 =wx.Button(panel,1,label=tip)
        sizer.Add(self.help7, (1,2), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help7.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))


        self.help8 =wx.Button(panel,1,label=px)
        sizer.Add(self.help8, (1, 3), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help8.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))


        self.help9 =wx.Button(panel,1,label=hl)
        sizer.Add(self.help9, (1, 4), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help9.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))


        self.help0 =wx.Button(panel,1,label=r)
        sizer.Add(self.help0,  (2, 0), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help0.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))


        self.help11 =wx.Button(panel,1,label=lp)
        sizer.Add(self.help11, (2, 1), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help11.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))


        self.help12=wx.Button(panel,1,label=rt)
        sizer.Add(self.help12, (2, 2), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help12.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))


        self.help13 =wx.Button(panel,1,label=pp)
        sizer.Add(self.help13, (2, 3), flag=wx.LEFT|wx.RIGHT, border = 5)
        self.help13.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))



        self.help14 =wx.Button(panel,1,label=qr)
        sizer.Add(self.help14, (2, 4), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help14.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))


        self.help15 =wx.Button(panel,1,label=po)
        sizer.Add(self.help15, (3, 0), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help15.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))


        self.help16 =wx.Button(panel,1,label=gi)
        sizer.Add(self.help16, (3, 1), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help16.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))


        self.help17 =wx.Button(panel,1,label=qw)
        sizer.Add(self.help17, (3, 2), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help17.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))




        self.help18 =wx.Button(panel,1,label=ol)
        sizer.Add(self.help18, (3, 3), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help18.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))


        self.help19 =wx.Button(panel,1,label=q)
        sizer.Add(self.help19, (3, 4), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help19.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))

        self.help20 =wx.Button(panel,1,label= tip)
        sizer.Add(self.help20, (4, 0), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help20.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))


        self.help21 =wx.Button(panel,1,label=tr)
        sizer.Add(self.help21, (4, 1), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help21.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))


        self.help22 =wx.Button(panel,1,label=we)
        sizer.Add(self.help22, (4, 2), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help22.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))


        self.help23 =wx.Button(panel,1,label=ti)
        sizer.Add(self.help23, (4, 3), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help23.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))

        self.help24 =wx.Button(panel,1,label=a1)
        sizer.Add(self.help24, (4, 4), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help24.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))

        self.help25 =wx.Button(panel,1,label=a2)
        sizer.Add(self.help25, (5, 0), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help25.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))

        self.help125 =wx.Button(panel,1,label=a3)
        sizer.Add(self.help125, (5, 1), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help125.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))


        self.help26 =wx.Button(panel,1,label=a4)
        sizer.Add(self.help26, (5, 2), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help26.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))


        self.help27 =wx.Button(panel,1,label=a5)
        sizer.Add(self.help27, (5, 3), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help27.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))



        self.help28 =wx.Button(panel,1,label=a6)
        sizer.Add(self.help28, (5, 4), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help28.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))

        self.help28 =wx.Button(panel,1,label=a7)
        sizer.Add(self.help28, (6, 0), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help28.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))


        self.help28 =wx.Button(panel,1,label=a8)
        sizer.Add(self.help28, (6, 1), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help28.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))


        self.help28 =wx.Button(panel,1,label=c3)
        sizer.Add(self.help28, (6, 2), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help28.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))
        self.help28 =wx.Button(panel,1,label= b1)
        sizer.Add(self.help28, (6, 3), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help28.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))
        self.help28 =wx.Button(panel,1,label=b2)
        sizer.Add(self.help28, (6, 4), flag=wx.LEFT|wx.RIGHT, border=5)
        self.help28.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.BOLD))

        panel.SetSizerAndFit(sizer)

    def Kiss(self, event):
        self.logger.AppendText('(a)%s'%event.GetString())


                                                                              ###
                                                                                                 ###
                                                                                                  ###
#####################################################################################################



        #cmd = os.getenv("comspec")
        #acrobat = "wmplayer.exe"   # THIS WHERE THE PLAY FUNCTION RESIDES
        #pdf = obj.path

        #cmds = [cmd, "/c", "start", acrobat, "/s", pdf]
        #subprocess.Popen(cmds)

'''
class PanelThree(wx.Panel):

    #----------------------------------------------------------------------
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent)

        grid = gridlib.Grid(self)
        grid.CreateGrid(25,12)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(grid, 0, wx.EXPAND)
        self.SetSizer(sizer)'''



class frame (wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, None, wx.ID_ANY, 'Panel Switcher',size = (1000, 650))
        self.Maximize(True)
        self.Show(True)

        self.panel_one = PanelOne(self)
        self.panel_two = PanelTwo(self)



        #self.panel_three = PanelThree(self)
        #self.panel_three.Hide()
        self.panel_two.Hide()

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel_one, 1, wx.EXPAND)
        self.sizer.Add(self.panel_two, 1, wx.EXPAND)
        #self.sizer.Add(self.panel_three,1, wx.EXPAND)
        self.SetSizer(self.sizer)



        menub = wx.MenuBar()
        fmenu = wx.Menu()
        fmenu.Append(wx.ID_OPEN, "Open\tCtrl+O")
        fmenu.AppendSeparator()
        fmenu.Append(wx.ID_SAVE, "Save\tCtrl+S")
        fmenu.Append(wx.ID_SAVEAS, "Save As\tCtrl+Shift+S")
        fmenu.AppendSeparator()
        fmenu.Append(wx.ID_EXIT, "Exit\tCtrl+Q")


        xmenu = wx.Menu()
        xmenu.Append(40, "Edit Profile")
        xmenu.Append(41, "Copy")
        xmenu.Append(43, "Paste")

        omenu = wx.Menu()
        omenu.Append(44, "view")

        omenu.Append(45, "Help")


        fily = wx.Menu()
        switch = fily.Append(wx.ID_ANY, 'Switch panel')
        self.Bind(wx.EVT_MENU,self.onSwitchPanels, switch)

        menub.Append(xmenu, "File")
        menub.Append(fmenu, "Edit")
        menub.Append(omenu, "Option")
        menub.Append(fily, "Switch")

        self.SetMenuBar(menub)

        toolbar = self.CreateToolBar()
        toolbar.AddLabelTool(41, '', wx.Bitmap('icon/back.png'))
        toolbar.AddLabelTool(42, '', wx.Bitmap('icon/blank_page.png'))
        toolbar.AddLabelTool(43, '', wx.Bitmap('icon/book.png'))
        toolbar.AddLabelTool(44, '', wx.Bitmap('icon/comments.png'))
        toolbar.AddLabelTool(45, '', wx.Bitmap('icon/mail.png'))
        toolbar.AddLabelTool(46, '', wx.Bitmap('icon/cloud.png'))
        toolbar.AddLabelTool(47, '', wx.Bitmap('icon/folder.png'))
        toolbar.AddLabelTool(48, '', wx.Bitmap('icon/eye.png'))
        toolbar.AddLabelTool(49, '', wx.Bitmap('icon/grid.png'))
        toolbar.AddLabelTool(50, '', wx.Bitmap('icon/fullscreen.png'))
        toolbar.AddLabelTool(51, '', wx.Bitmap('icon/image.png'))
        toolbar.AddSeparator()

        toolbar.AddLabelTool(3, '', wx.Bitmap('icon/process.png'))
        toolbar.AddLabelTool(3, '', wx.Bitmap('icon/news.png'))
        toolbar.AddLabelTool(3, '', wx.Bitmap('icon/map_pin.png'))
        toolbar.AddLabelTool(3, '', wx.Bitmap('icon/news.png'))
        toolbar.AddLabelTool(3, '', wx.Bitmap('icon/star.png'))
        toolbar.AddLabelTool(3, '', wx.Bitmap('icon/quote.png'))
        toolbar.AddLabelTool(3, '', wx.Bitmap('icon/settings.png'))
        toolbar.AddLabelTool(3, '', wx.Bitmap('icon/computer.png'))
        toolbar.AddLabelTool(3, '', wx.Bitmap('icon/page.png'))
        toolbar.AddSeparator()
        toolbar.AddLabelTool(3, '', wx.Bitmap('icon/block.png'))
        toolbar.AddLabelTool(3, '', wx.Bitmap('icon/id_card.png'))
        toolbar.AddLabelTool(3, '', wx.Bitmap('icon/film.png'))
        toolbar.AddLabelTool(3, '', wx.Bitmap('icon/check_mark.png'))
        toolbar.AddLabelTool(3, '', wx.Bitmap('icon/male_user.png'))
        toolbar.AddLabelTool(3, '', wx.Bitmap('icon/tablet.png'))
        toolbar.AddLabelTool(3, '', wx.Bitmap('icon/down.png'))
        toolbar.AddLabelTool(3, '', wx.Bitmap('icon/tag.png'))
        toolbar.AddLabelTool(3, '', wx.Bitmap('icon/up.png'))
        toolbar.AddLabelTool(3, '', wx.Bitmap('icon/drop.png'))
        toolbar.AddLabelTool(3, '', wx.Bitmap('icon/users.png'))
        toolbar.AddLabelTool(3, '', wx.Bitmap('icon/next.png'))

        toolbar.Realize()


        self.Centre()
        self.Show(True)

    def onSwitchPanels(self, event):

        if self.panel_one.IsShown():
            self.SetTitle("Ucnet-App")
            self.panel_one.Hide()
            self.panel_two.Show()


        else:
            self.SetTitle("Media files")
            self.panel_one.Show()
            self.panel_two.Hide()
        self.Layout()

app = wx.App()
frame(None, -1, 'New')
app.MainLoop()


#####################################################################################################


                                                                                                     ###                                                                                               ##                                                                                               ###
#####################################################################################################

