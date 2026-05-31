from database.models import ChatHistoryModel


class ChatMemoryManager:

    def __init__(self):

        self.chat_model = ChatHistoryModel()

    def save_conversation(
        self,
        question,
        answer
    ):
        """
        Save user conversation.
        """

        self.chat_model.save_chat(
            question,
            answer
        )

    def build_chat_context(
        self,
        limit=5
    ):
        """
        Build formatted chat history context.
        """

        chats = self.chat_model.get_recent_chats(
            limit=limit
        )

        formatted_history = []

        for question, answer in chats:

            formatted_history.append(
                f"""
User: {question}

Assistant: {answer}
"""
            )

        return "\n".join(formatted_history)