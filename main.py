mys = "print ('hello world')"
exec(mys)

parser2 = "value=123123"
parser = parser2.split("=")
parser[0]
parser[1]

Configfile = open("Setup.config","r+")
for line in Configfile:
  exec(line)
  

  

