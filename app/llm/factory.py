from app.core.config import get_settings
from app.llm.base import BaseLLMProvider
from app.llm.providers.mock_provider import MockLLMProvider
from app.llm.providers.openai_provider import OpenAIProvider


def get_llm_provider() -> BaseLLMProvider:
    """Create the configured LLM provider."""

    settings = get_settings()

    if settings.llm_provider == "mock":
        return MockLLMProvider()

    if settings.llm_provider == "openai":
        if not settings.openai_api_key:
            raise ValueError(
                "OPENAI_API_KEY is required when using OpenAI."
            )

        return OpenAIProvider(
            api_key=settings.openai_api_key,
            model=settings.openai_model,
        )

    raise ValueError(
        f"Unsupported LLM provider: {settings.llm_provider}"
    )