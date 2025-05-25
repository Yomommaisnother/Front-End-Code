from survey import AnonymousSurvey
#Define a question, and make a survey
question="What language did you learn to speak?"
my_survey=AnonymousSurvey(question)


my_survey.show_question()
print('Enter q to quit anytime.\n ')


while True:
	response=input('Language: ')
	if response== 'q':
		break
	my_survey.store_response(response)

	print("\nThank you to everyone who participated in the survey!")
	my_survey.store_response(response)