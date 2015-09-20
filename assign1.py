# Assignment 1
# Adriaan Epema (5737499)

def assign1PartA():
  firstName = "Adriaan"
  lastName = "Epema"
  studentNumber = "5737499"
  program = "Interactive Arts and Science"
  year = "2nd Year"
  reasonA = "I'm taking this course to widen my knowledge of programming languages and gain experience."
  reasonB = "I think Python and Java are going to be very useful in my career path."
  print "Name: " + firstName + " " + lastName
  print "Student Number: " + studentNumber
  print "Program: " + year + " of " + program
  print reasonA
  print reasonB

def assign1PartB(feet, inches):
  bedmas1 = feet * 12
  bedmas2 = bedmas1 + inches
  centiConv = bedmas2 * 2.54
  print feet + "feet and " + inches + "inches converts to " + centiConv + "cm."
