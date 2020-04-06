def process(a):
       import re
       a=re.sub('[^a-zA-Z]',' ',a)
       a=re.sub(r'\s+[a-zA-Z]\s+',' ',a)
       a=re.sub(r'\s+','',a)
       a=a.lower()
       return a
