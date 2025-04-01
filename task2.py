wr = input("Enter text to write to the file: ")
with open("output.txt", "w") as output:
    output.write(wr + "\n")
    print("Data successfully written output.txt.\n")
    
app = input("Enter additional text to append: ")
with open("output.txt", "a") as output:
    output.write(app)
    print("Data successfully appended.\n")


with open("output.txt", "r") as output:
    print("Final content of output.txt:"+"\n"+output.read())