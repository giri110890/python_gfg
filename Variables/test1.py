# test1.py

print("file1 __name__ == %s" %(__name__))

if __name__ == "__main__":
    print("File 1 is being run directly")
else:
    print("File 1 is being imported")