# -*- coding: utf-8 -*-
"""Crash Course Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QC-9GMBuL1qjrPwQjRLP8NNVyQBrsJfw
"""

7 **4

s = " Hi there Darwish"
s.split()

print("The diameter of {} is {}".format('Earth' , 12742))

def emailSplit(email):
  return email.split('@')[-1]

emailSplit('darwka@gmail.com')

def find_cat(cat):
  return 'dog' in cat.lower()

cat = (' Hello there cat')
find_cat(cat)

def count_word(st):
  count  = 0
  for word in st.lower().split():
      if word == 'cat':
        count += 1
 
  return count

st= ('There is a cat in the building near cat house and cat family den!')

count_word(st)

