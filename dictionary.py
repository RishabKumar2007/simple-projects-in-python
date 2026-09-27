info = {
    "name": "Rishab",
    "age": "19",
    "learning": "python",
    "marks" : "98.8",
    "subjects" : ["python", "calculus","web development"
                  "ece", "digital design"]
}
print(info)
# we can put any data typr inside a dictionary
# we can even put lists and tuples inside a dictionary
#dictionaries are also mutable
print(type(info))
#dictonaries are unordedred means there is no indexing used
print(info["name"])#this is how we can print elements inside a disctionary
print(info["subjects"][1])#this is how we can access list inside a dictionary
info["name"] = "RishabKumar"#this is how we wcan change data inside a dictionary
print(info["name"])
null = {}#this is a null dictionary
print(null)
print(type(null))

#we can use nested dictionary 
student = {"name" : "Rishab",
           "subject" : {"physics" : "39", 
                        "chemistry": "37",
                        "maths" : "38"}}

print(student["subject"])
print(info.keys())#this is how we can prrint all keys inside a dictionary
print(list(student.keys()))#we use typecasting to convert dictionary to list
print(len(student))#we can find length of dictionary keys

print(student.values())#this is how we can access whats inside the keys in the dictionary

print(student.items())#return all the data in pairs like inside the ( , )

print(info.get("name"))#to get the value of specific key


print(student["name"]) #-> returns an error if the key is not found
print(student.get("name")) # returns -> none if the key is not found

student.update({"City" : "Patna"})
print(student)
student.update({"name": "R"})
print(student)