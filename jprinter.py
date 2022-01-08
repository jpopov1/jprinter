from win32printing import Printer
import os
from PIL import Image, ImageWin
import urllib.request
import sys
import win32print
import win32ui

#jprinter


def link(link):
    
    filename = link.split('/')[-1]
    opener = urllib.request.URLopener()
    opener.addheader('User-Agent', 'python')
    filename, headers = opener.retrieve(link,filename)
    
    
    PHYSICALWIDTH = 110
    PHYSICALHEIGHT = 110

    printer_name = win32print.GetDefaultPrinter ()
    file_name = filename

    hDC = win32ui.CreateDC ()
    hDC.CreatePrinterDC (printer_name)
    printer_size = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps (PHYSICALHEIGHT)

    bmp = Image.open (file_name)
    if bmp.size[0] < bmp.size[1]:
      bmp = bmp.rotate (90)

    hDC.StartDoc (file_name)
    hDC.StartPage ()

    dib = ImageWin.Dib (bmp)
    dib.draw (hDC.GetHandleOutput (), (0,0,printer_size[0],printer_size[1]))

    hDC.EndPage ()
    hDC.EndDoc ()
    hDC.DeleteDC ()
              
    os.remove(filename)


def img(filename):
    PHYSICALWIDTH = 110
    PHYSICALHEIGHT = 110

    printer_name = win32print.GetDefaultPrinter ()
    file_name = filename

    hDC = win32ui.CreateDC ()
    hDC.CreatePrinterDC (printer_name)
    printer_size = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps (PHYSICALHEIGHT)

    bmp = Image.open (file_name)
    if bmp.size[0] < bmp.size[1]:
      bmp = bmp.rotate (90)

    hDC.StartDoc (file_name)
    hDC.StartPage ()

    dib = ImageWin.Dib (bmp)
    dib.draw (hDC.GetHandleOutput (), (0,0,printer_size[0],printer_size[1]))

    hDC.EndPage ()
    hDC.EndDoc ()
    hDC.DeleteDC ()
    if delete == True:
        os.remove(filename) 
    else:
        pass
    
def text(text, font):
    
    fonnt = {
    "height": font,
}
    with Printer(linegap=1) as printer:
        printer.text(text, font_config=fonnt)
        printer.text("  ", font_config=fonnt)
    
    
    
    
