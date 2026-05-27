# creation-- creates file only there is no file with the same mentioned
file=open("a1.txt","x")
file.write("this file if created using x mode")
file.close()