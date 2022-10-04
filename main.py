count = 1
a = open("a.txt", "w")
while count <= 100:
    if count % 5 == 0 and count % 3 == 0:
        a.write("HelloWorld\n")
    elif count % 3 == 0 and count % 5 != 0:
        a.write("Hello\n")
    elif count % 5 == 0 and count % 3 != 0:
        a.write("World\n")
    else:
        a.write(str(count) + "\n")
    count += 1
a.close()