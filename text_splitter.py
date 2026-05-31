from langchain_text_splitters import RecursiveCharacterTextSplitter


class TextSplitter:

    def __init__(
        self,
        chunk_size=500,
        chunk_overlap=100
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )

    def split_text(self, text):
        """
        Split large text into smaller chunks.
        """

        if not text:
            return []

        chunks = self.text_splitter.split_text(text)

        return chunks