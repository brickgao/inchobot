# encoding: utf-8
import datetime
from ibot import db


class Discussion(db.Model):
    __tablename__ = 'discussion'

    _id = db.Column(db.Integer, primary_key=True)
    discussion = db.Column(db.String)
    date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user._id'))
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignment._id'))
    user = db.relationship('User',
                           primaryjoin='Discussion.user_id == User._id',
                           backref='discussions')
    assignment = db.relationship('Assignment',
                                 primaryjoin='Discussion.assignment_id == Assignment._id',
                                 backref=db.backref('discussions', order_by='Discussion.date'))

    def __init__(self, discussion, user_id, date=datetime.datetime.today()):
        self.discussion = discussion
        self.date = date
        self.user_id = user_id

