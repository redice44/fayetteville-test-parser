import re
import sys

ansPrefix = ['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g']

testBank = sys.stdin.read()
testBank = testBank.split('\n')
testBank = "".join(testBank)
testBank = "a" + testBank
testBank = re.split("OBJECTIVES:", testBank)
testBank = [elem for elem in testBank if elem.find("a. ") != -1]

for questionNum in range(len(testBank)):
  question = testBank[questionNum]
  question = re.split('[a-zA-z]\d+\. ', question)[1]
  question = question[:question.find("POINTS:")]
  question = re.split("ANSWER:", question)
  answer = question[1].strip()
  # Split into the question and answers
  question = re.split(' [a-g]\. ', question[0])
  # Print question with number prefix
  print "%s. %s" % (questionNum+1, question[0])
  # Print answers with answer prefix
  for ans in range(1, len(question)):
    if ansPrefix[ans] == answer or (ans == 1 and answer == "True") or (ans == 2 and answer == "False"):
      sys.stdout.write('*')
    print "%s. %s" % (ansPrefix[ans], question[ans])
  print "\n"