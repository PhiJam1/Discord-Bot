class Member(object):
    def __init__(self, _user_name, _user_id, _terms_to_track, _term_total_use, _total_msg, _total_questions, _points):
        self.user_name = _user_name
        self.user_id = _user_id
        self.terms_to_track = _terms_to_track
        self.term_total_use = _term_total_use
        self.total_msg = _total_msg
        self.total_questions = _total_questions
        self.points = _points
    
    #getters

    #setters
    #This will add a new word to be tracked to their word list
    #It will also create new indexes for other relevent fields
    def add_term(self, word):
        self.terms_to_track.append(word)
        self.term_total_use.append(0)
    
    #This will increment total messages when this user sends a message
    def update_message_history(self, msg):
        
        #see how many and which terms it has
        
        #update total msgs
        self.total_msg += 1
        #update total questions
        if (msg.find("?") != -1):
            self.total_questions += 1
            self.pts += (len(msg) * 1.5)
        else:
            self.pts += len(msg)
        

#ideas: add an anrgy level for all caps messages