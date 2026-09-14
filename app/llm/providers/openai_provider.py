from openai import AsyncOpenAI

from app.llm.base import BaseLLMProvider


class OpenAIProvider(BaseLLMProvider):
    """OpenAI implementation of the LLM provider."""

    def __init__(
        self,
        api_key: str,
        model: str,
    ) -> None:
        self.client = AsyncOpenAI(api_key=api_key)
        self.model = model

    async def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ) -> str:
        messages = []

        if system_prompt:
            messages.append(
                {
                    "role": "system",
                    "content": system_prompt,
                }
            )

        messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )

        return response.choices[0].message.content or ""