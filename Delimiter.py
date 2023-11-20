a=input("Enter a string:")
count=0
for i in a:
     if(i==','or i==';'or i=='"' or i==' 'or i==':' or i=='\t' or i=='\n'):
          count=count+1
print("Number of Delimiters are:",count)
print("Number of Commas are:",a.count(','))
print("Number of Colons are:",a.count(':'))
print("Number of Semicolons are:",a.count(';'))
print("Number of Dots are:",a.count('.'))
