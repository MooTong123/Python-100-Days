# -- coding: utf-8 --


class AnoymousSurvy():
    def __init__(self,question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("Survy results:")
        for response in self.responses:
            print('- ' + response)

