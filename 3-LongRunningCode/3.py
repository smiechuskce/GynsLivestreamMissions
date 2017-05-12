def magic1(a, b):
    
    # o = 0             => This is just a + b
    # i = 0             => Very long running loops...
    # while i < a:
    #    o += 1
    #    i += 1
    # i = 0
    # while i < b:
    #    o += 1
    #    i += 1
    
    return a + b

def magic2(a, b): 

    # o = 0             => This is just a * b         
    # i = 0             => Again...
    # while i < b:
    #    o = magic1(o, a)
    #    i += 1

    return a * b

n1 = int("2867279575674690971609643216365"
         "4161626212087501848651843132337"
         "3373323997065608342")
n2 = int("1240905467219837578349182398365"
         "3459812983123659128386518235966"
         "4109783723654812937")
n = magic2(magic1(n1, n2), 1337)
print hex(n)[2:-1].decode("hex").splitlines()[0]

# Result: WolneOprogramowanie!

