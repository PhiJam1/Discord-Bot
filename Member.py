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
        for i in range(len(self.terms_to_track)):
            #print(str(i) + " " + str(len(self.term_total_use)) + " " + str(len(self.term_total_use)))
            self.term_total_use[i] += msg.count(self.terms_to_track[i])
        #update total msgs
        self.total_msg += len(msg.split(" "))
        #update total questions
        if (msg.find("?") != -1):
            self.total_questions += 1
            self.points += (len(msg) * 1.5)
        else:
            self.points += len(msg)
    def get_total_stats(self):
        msg = "**Stats for " + self.user_name + "**,\n"
        msg += "*Messages Sent:* " + str(self.total_msg)
        msg += " *Questions Asked:* " + str(self.total_questions) + "\n"
        #msg += "*Points:* " + str(self.points) + "\n"
        for i in range(len(self.terms_to_track)):
            msg += "Used *" + str(self.terms_to_track[i]) + "* " + ("once\n" if self.term_total_use[i] == 1 else (str(self.term_total_use[i]) + " times - "))
            #msg += "That's " + str(self.rate_of_term_use(i)) + "% of their total words\n"
        return msg

    def get_stats_of_word(self, index):
        msg = "Used " + str(self.terms_to_track[index]) + " " + str(self.term_total_use[index]) + (" once\n" if self.term_total_use[index] == 1 else " times\n")
        #msg += "That's " + str(self.rate_of_term_use(index)) + "% of their total words\n"
    def rate_of_term_use(self, index):
        if (self.total_msg == 0):
            return 0
        return self.term_total_use[index] / self.total_msg
    def get_data(self):
        s = self.user_name + ", "
        s += str(self.user_id) + ", "
        for term in self.terms_to_track:
            s += term + ":"
        s += ", "
        for use in self.term_total_use:
            s += str(use) + "$"
        s += ", "
        s += str(self.total_msg) + ", "
        s += str(self.total_questions) + ", "
        s += str(self.points)
        return s
#ideas: add an anrgy level for all caps messages
