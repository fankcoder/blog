import random
import os
textdir = os.getcwd()
textdir = textdir+'/blog/cheerup.txt'
#print textdir
ft = open(textdir,'r')
text = ft.readlines()
show = random.choice(text)
if __name__=="__main__":
    print show
