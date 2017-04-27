from .categories import categories

class Question(object):
    def __init__(self, category='General Knowledge', type="multiple", difficulty="easy", question="Example question?", correct_answer="Yes", incorrect_answers=["No"]):
        self.category = category
        self.type = type
        self.difficulty = difficulty
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers
        
    def __str__(self):
        return self.question
    
    def __repr__(self):
        return 'Question(category=%r, type=%r, difficulty=%r, question=%r, correct_answer=%r, incorrect_answers=%r)' % (self.category, self.type, self.difficulty, self.question, self.correct_answer, self.incorrect_answers)
    
    def getCategoryId(self):
        """
            Returns the category ID number associated with this question.
        """
        try:
            category_id = categories[self.category]
            return category_id
        except:
            return 0