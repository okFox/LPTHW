netflix = "$9.99"
prompt = 'yes/no > '

print("Hello.  Be honest in the following question.")

print("Have you watched Netflix Lately?")

answer = input(prompt)

# how would you sanitize the user input?
if answer == "no":
  print("You have wasted ", netflix, " I hope you're happy.")

if answer == "yes":
  print("Phew, I guess you can keep paying for it.")

