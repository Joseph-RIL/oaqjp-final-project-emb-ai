import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        emotion_dict = emotion_detector("I am glad this happened")
        dom_emo = emotion_dict['dominant_emotion']
        self.assertEqual(dom_emo, "joy")

    def test_anger(self):
        emotion_dict = emotion_detector("I am really mad about this")
        dom_emo = emotion_dict['dominant_emotion']
        self.assertEqual(dom_emo, "anger")

    def test_disgust(self):
        emotion_dict = emotion_detector("I feel disgusted just hearing about this")
        dom_emo = emotion_dict['dominant_emotion']
        self.assertEqual(dom_emo, "disgust")

    def test_sadness(self):
        emotion_dict = emotion_detector("I am so sad about this")
        dom_emo = emotion_dict['dominant_emotion']
        self.assertEqual(dom_emo, "sadness")

    def test_fear(self):
        emotion_dict = emotion_detector("I am really afraid that this will happen")
        dom_emo = emotion_dict['dominant_emotion']
        self.assertEqual(dom_emo, "fear")


if __name__ == "__main__":
    unittest.main()