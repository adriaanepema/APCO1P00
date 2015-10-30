# Assignment 2
#
# Adriaan Epema (5737499)
#
# Part A

def assign2A():
  # Define variables
  numberRandom = 0
  count = 0
  question = ""
  even = true
  # for loop for 5 questions
  for i in range(5):
    # Get a random number
    import random
    numberRandom = int(random.random() * 100)
    # Determine if x is even/odd
    if numberRandom % 2 == 0:
      even = true
    else:
      even = false
    # Ask the question
    question = "Is " + str(numberRandom) + " odd or even?"
    answer = raw_input(question)
    # Determine answer
    if str(answer.lower()) == "even":
      if even == true:
        print "Correct!"
      else:
        print "Sorry, that is incorrect."
    elif str(answer.lower()) == "odd":
      if even == false:
        print "Correct!"
      else:
        print "Sorry, that is incorrect."
    else:
      print "I'm sorry, Dave. I'm afraid I can't do that."
    
# Part B

def assign2B(size, padding):
  # Variables
  size = int(size)
  padding = int(padding)
  width = padding + size + padding + 2
  height = padding + size + padding + 2
  # Check margin width
  if (padding + padding) >= size:
    padding = (size / 2) - 4
    print "padding reset"
  else:
    print "padding ok"
  # Draw pic
  pic = makeEmptyPicture(width, height)
  # Colour margin
  getPixels(pic)
  # Add border
  addRect(pic, 0, 0, width - 1, height - 1)
  show(pic)
