# -- coding: utf-8 --
import unittest
from survy import AnoymousSurvy

class TestAnoymousSurvy(unittest.TestCase):

    def setUp(self):
        question = "what language did you first learn to speak?"
        self.my_survey = AnoymousSurvy(question)
        self.responses = ["English","Spanish","Mandarin"]

    def test_store_single_response(self):
        self.my_survey.store_response("English")
        self.assertIn("English", self.my_survey.responses)

    def test_stire_three_response(self):

        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main