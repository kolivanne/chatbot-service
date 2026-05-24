from app.services.llm_service import LLMService
from app.services.prompt_safety import sanitize_message


class BedrockService(LLMService):
    """
    AWS Bedrock Provider (Mock Implementation).

    Zeigt die Struktur einer möglichen Integration.
    """

    def __init__(self):
        # In echt würde hier boto3 oder bedrock runtime client stehen:
        #
        # import boto3
        # self.client = boto3.client("bedrock-runtime")
        pass

    def generate_response(self, message: str) -> str:
        message = sanitize_message(message)
        return self._call_bedrock(message)

    def _call_bedrock(self, message: str) -> str:
        """
        Simuliert einen Bedrock Request.
        """

        # Beispiel:
        #
        # response = self.client.invoke_model(
        #     modelId="anthropic.claude-v2",
        #     body=json.dumps({
        #         "prompt": message,
        #         "max_tokens": 200
        #     })
        # )
        #
        # return parsed_response

        return f"[BEDROCK MOCK] Antwort auf: {message}"