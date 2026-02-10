### Change History
# Ben Evans - 05/06/2025 - Created the Message model to handle the message table in the database.









from pymysql import NULL
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, session
import random


DATABASE = 'sll_prod'

class Message:
    def __init__(self,data):
        self.id = data['id']
        self.message = data['message']
        self.live_id = data['live_id']
        self.user_id = data['user_id']
        self.number_of_likes = data['number_of_likes']
        self.visibility_status = data['visibility_status']
        self.moderation_status = data['moderation_status']
        self.moderator_id = data['moderator_id']
        self.flagged_keywords = data['flagged_keywords']
        self.spam_detection_ind = data['spam_detection_ind']
        self.read_receipt = data['read_receipt']
        self.read_receipt_ts_cst = data['read_receipt_ts_cst']
        self.highlighted_message_ind = data['highlighted_message_ind']
        self.platform_used = data['platform_used']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def get_all_message_columns():
        return ['id', 'message', 'live_id', 'user_id', 'number_of_likes',
                'visibility_status', 'moderation_status', 'moderator_id',
                'flagged_keywords', 'spam_detection_ind', 'read_receipt',
                'read_receipt_ts_cst', 'highlighted_message_ind',
                'platform_used', 'created_at', 'updated_at']
###################################################################################################
