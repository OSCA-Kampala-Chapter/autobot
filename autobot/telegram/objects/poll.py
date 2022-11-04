from .base import BaseObject
from .user import User
from .poll import PollOption
from typing import List

class Poll(BaseObject):

    """
    This Object represents a poll

    Args:
        id (str): Unique poll identifier

        question (str): Poll question, 1-255 characters

        options (List[:class:`telegram.PollOption`]): List of poll options

        total_voter_count (int): Total number of users that voted in the poll

        is_closed (bool): True, if the poll is closed

        is_anonymous (bool): True, if the poll is anonymous

        type (str): Poll type, currently can be “regular” or “quiz”

        allows_multiple_answers (bool): True, if the poll allows multiple answers

        correct_option_id (int): Optional. 0-based identifier of the correct answer option. 
        Available only for polls in the quiz mode, which are closed, 
        or was sent (not forwarded) by the bot or to the private chat with the bot.

        explanation (str): Optional. Text that is shown when a user chooses an 
        incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters

        explanation_entities (List[:class:`telegram.MessageEntity`]): Optional. 
        Special entities like usernames, URLs, bot commands, etc. that appear in the explanation

        open_period (int): Optional. Amount of time in seconds the poll will be active after creation
        close_date (int): Optional. Point in time (Unix timestamp) when the poll will be automatically closed

    """

    __slots__ = (
        'correct_option_id',
        'explanation',
        'explanation_entities',
        'open_period',
        'close_date',
    )

    def __init__(
        self,
        id:str,
        question:str,
        options:List[PollOption],
        total_voter_count:int,
        is_closed:bool,
        is_anonymous:bool,
        type:str,
        allows_multiple_answers:bool
    ):
    
        self.id = id
        self.question = question
        self.options = options
        self.total_voter_count = total_voter_count
        self.is_closed = is_closed
        self.is_anonymous = is_anonymous
        self.type = type
        self.allows_multiple_answers = allows_multiple_answers
        self.correct_option_id = None
        self.explanation = None
        self.explanation_entities = None
        self.open_period = None
        self.close_date = None

class PollAnswer(BaseObject):
    """
    This object represents an answer of a user in a non-anonymous poll.

    Args:
        poll_id (str): Unique poll identifier

        user (:class:`telegram.User`): The user, who changed the answer to the poll

        option_ids (List[int]): 0-based identifiers of answer options, chosen by the user. 
        May be empty if the user retracted their vote.
    """

    __slots__ = ("poll_id", "user", "option_ids",)

    def __init__(self, poll_id:str, user:User, option_ids:List[int]):
        self.poll_id = poll_id
        self.user = user
        self.option_ids = option_ids

class PollOption(BaseObject):
    """
    This object contains information about one answer option in a poll.

    Args:
        text (str): Option text, 1-100 characters

        voter_count (int): Number of users that voted for this option

    """

    __slots__ = ("text", "voter_count",)

    def __init__(self, text:str, voter_count:int):
        self.text = text
        self.voter_count = voter_count
