# -- coding: utf-8 --


from survy import AnoymousSurvy

question = "What language did you first learn to speak?"
my_survy = AnoymousSurvy(question)

my_survy.show_question()
print("Enter 'q' at any time to quit. \n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survy.store_response(response)

print("\nThank you for participating in the survey")
my_survy.show_results()