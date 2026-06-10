from database.db import DatabaseConnection


class ChatHistoryModel:

    def __init__(self):

        self.connection = DatabaseConnection.get_connection()

        self.cursor = self.connection.cursor()

        self.create_table()

    def create_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS chat_history (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_question TEXT,
            ai_answer TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """

        self.cursor.execute(query)

        self.connection.commit()

    def save_chat(self, question, answer):

        query = """
        INSERT INTO chat_history
        (user_question, ai_answer)
        VALUES (%s, %s)
        """

        values = (question, answer)

        self.cursor.execute(query, values)

        self.connection.commit()

    def get_recent_chats(self, limit=5):

        query = f"""
        SELECT user_question, ai_answer
        FROM chat_history
        ORDER BY created_at DESC
        LIMIT {limit}
        """

        self.cursor.execute(query)

        results = self.cursor.fetchall()

        return results
