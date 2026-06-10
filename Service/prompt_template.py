class PromptTemplate:

    def build_prompt(
        self,
        user_question,
        retrieved_chunks,
        chat_history=""
    ):
        """
        Build RAG prompt with source context.
        """

        context_parts = []

        for chunk in retrieved_chunks:

            context_parts.append(
                f"""
Source {chunk['source_id']}:
{chunk['content']}
"""
            )

        context = "\n\n".join(context_parts)

        prompt = f"""
You are an intelligent AI assistant.

Answer ONLY using the provided context.

If answer is not found in context, say:
"I could not find the answer in the uploaded PDFs."

-----------------------------------
Previous Conversation:
{chat_history}
-----------------------------------

Context:
{context}

-----------------------------------
Question:
{user_question}
-----------------------------------

While answering:
- Be clear and concise
- Mention source numbers if possible

Answer:
"""

        return prompt
