x=24*726
y=320
print("without Formatting:{} {}".format(x,y))
print("right justify:{0:<7} {1}".format(x,y))
print("left justify:{0:>7} {1}".format(x,y))
print("right justify with zero:{0:<07} {1}".format(x,y))
print("left justify with zero:{0:>07} {1}".format(x,y))
print("right justify with plus:{0:<+07} {1}".format(x,y))
print("left justify with plus:{0:>+07} {1}".format(x,y))
print("using commas:{:,}".format(x))
print("using replace:{:,}".format(x).replace(",","."))
print("default number of decimal places:{:f}".format(x)) #use x, o and b for hexadecimal, octal and binary respectively
print("fixed number of decimal places:{:.3f}".format(x))
