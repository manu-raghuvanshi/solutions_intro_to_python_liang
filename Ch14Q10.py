
dictionary = {
  "Alabama":"Montgomery",
  "Alaska":"Juneau",
  "Arizona":"Phoenix",
  "Arkansas":"Little Rock",
  "California":"Sacramento",
  "Colorado":"Denver",
  "Connecticut":"Hartford",
  "Delaware":"Dover",
  "Florida":"Tallahassee",
  "Georgia":"Atlanta"}


correctCount = 0

states = dictionary.keys()

for state in states:
    capital = input("What is the capital of " + state + "? ")
  
    if capital.lower() == dictionary[state].lower():
        print("Your answer is correct");
        correctCount += 1
    else:
        print("The correct answer should be " + dictionary[state])

println("The correct count is " + correctCount)
