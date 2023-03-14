class word(object):
    #not sure how I want to do data persistance.
    #maybe we do all the data saving in the main file.
    #or we have another file that works just to recreate all the word
    #objects everytime the sever goes up. Or its just a check we make when adding a word.
    ''' oh yea triple comment thing
    plan for tmr. tmr should be enough to get all this word stuff working
    Started with data persistance. Finding how to read and write to files.
    This where to call these fuctions.
    Other ideas to add on, a bot that tracks messages in general to make a leaderboard
    based on who talks the most or extra points for asking questions. Then a voting/poll bot that
    attacks your dms looking for answers.'''
    def __init__(self, _term, _authors, _term_use_total, _total_msg, _mes_with_term) -> None:
        self.term = _term
        self.authors = _authors
        self.term_use_total = []
        self.total_msg = []
        self.msg_with_term = []

    #some basic getters
    def get_term(self):
        return self.term
    def get_word_use_total(self, author):
        for i in range(len(self.authors)):
            if (self.authors[i] == author):
                return self.term_use_total[i]

    def get_total_msg(self, author):
        for i in range(len(self.authors)):
            if (self.authors[i] == author):
                return self.total_msg[i]

    def get_msg_with_term(self, author):
        for i in range(len(self.authors)):
            if (self.authors[i] == author):
                return self.msg_with_term[i]
    
    def set_term(self, _term):
        self.term = _term
    def set_authors(self, _authors):
        self.authors = _authors
    def set_term_use_total(self, use_total):
        self.term_use_total = use_total