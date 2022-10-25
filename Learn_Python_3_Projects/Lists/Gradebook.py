# Creating a list called subjects and filling it up with classes
subject = ["physics", "calculus", "poetry", "history"]

# Creating a list called grades and filling it up with scores of different classes
grades = [98, 97, 85, 88]

# Creating a two-dimensional list to combine both subjects and grades into gradebook
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# Printing the Gradebook
print(gradebook)

# Adding more subjects
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# Modifying the Gradebook
gradebook[-1][-1] = 98
gradebook[2].remove(85)
gradebook[2].append("Pass")

# Creating a last semester gradebook [Adding last semester gradebook avoid NameError in the code]
last_semester_gradebook = [["python", 98], ["ethical hacking", 99], ["english", 95], ["networking", 100], ["linux administration", 97], ["windows server administration", 94], ["enterprise risk assessment", 100]]

# Adding information from last semester gradebook list
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
