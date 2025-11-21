user_input = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "")
append_input = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(append_input + "")
    print("Data successfully appended.")
print("Final content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)