# PassGenerator
<img src="./source/cover.jpg"  alt="error" title="cover-project">
PassGenerator(lol) is another one of my local GUI projects! :3

My application allows the user to generate a password of 8/16/32 characters of the user's choice.

## **About**
I wrote this application in pure Python 🐍, I assembled the interface using Qt5 using a little css for the look.
Python + Qt = 💚

## **How it works?**
In pg.py, I refer to passgen_ui.py, namely, to the interface object, as a result, I fasten a call to a specific function.
```python
  form.pushButton.clicked.connect( default ) # We press the button
```
  
Function  
```python
  # Generate 16x / default password by S-Mamashin
  def default():
      password = ""
      all_kinds = "1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ" 
  
      for a in range(16): 
  
          password = password + random.choice(list(all_kinds)) 
  
      return form.lineEdit.setText(password), form.label.setText("Generated password of 16 characters!")
```
---

## ** How to run it?**
You can use this after installing PyQt5 module
* pip install pyqt5
Or build it with pyinstaller
* pyinstaller -F pg.py

---
## **Author**
Stepan Mamashin


