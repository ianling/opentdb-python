# opentdb-python
A python2 library for interfacing with the Open Trivia Database (openTDB) API

Allows you to generate a session token and get questions.

# Example Usage

    import opentdb
    
    opentdb_session = opentdb.Client()
    opentdb_session.getToken()
    questions = opentdb_session.getQuestions(amount=5, use_token=True, category=18)

You can retrieve a Dictionary of all the category names and ID numbers via the Client:

    categories = opentdb_session.getCategories()
    # categories['Science: Computers'] == 18

Once you've retrieved some questions, you can do whatever you'd like with them.

    for question in questions:
        print 'Category: %s (ID: %i)' % (question.category, question.getCategoryId())
        print 'Question: %s' % (question)
        print 'Answer : %s' % (question.correct_answer)

The submissions to the Open Trivia DB are usually (always?) in the form of multiple choice questions,
so you can also view a List of incorrect answers using `question.incorrect_answers`.
