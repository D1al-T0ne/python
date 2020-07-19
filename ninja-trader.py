#! python3                                                                      
                                                                                 
# ninja-trader.py a script that takes a list of 52 high stock tickers, and      
# opens a chart for each one in Ninja Trader.                                   
                                                                                 
import subprocess                                                               
import pyautogui                                                                
                                                                                 
# TODO open Ninja Trader, add a check of the exit code to ensure the app has open.

# This is a test to open textedit on MacOS using subprocess                     
subprocess.Popen(['open', '/Applications/Textedit.app/'])                       
                                                                                 
# Read in the contents of new-highs.txt file.                                   
# It is good practice to use the with keyword when dealing with file objects.   
# The advantage is that the file is properly closed after its suite finishes.   
                                                                                 
with open('new-highs.txt', 'r') as f:                                           
     for tickers in f:                                                           
#       pyautogui.hotkey('crtl', 'c')                                           
        pyautogui.typewrite('tickers')                                          
#       pyautogui.press('enter')
