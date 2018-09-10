import logging

logging.basicConfig(filename="f:\pythonpro\logg.log",level=logging.DEBUG)
l=logging.getLogger()

l.info("our first message")
print(l.level)
l.warning("this is warning message")
