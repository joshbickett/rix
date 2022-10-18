class Mail:
    def __init__(self,thread_id,date,references,in_reply_to,sender,cc,subject,messages, threads,conversation):

        self.thread_id = thread_id
        self.date = date
        self.references = references
        self.in_reply_to = in_reply_to
        self.sender = sender
        self.cc = cc
        self.subject = subject
        self.messages = messages
        self.threads = threads
        self.conversation = conversation


    def parse_cc_to_arr(self):
        print("parse_cc_to_arr")
        cc_arr = self.cc.split(",")
        cc_arr_stripped = [c.strip() for c in cc_arr]
        return cc_arr_stripped


