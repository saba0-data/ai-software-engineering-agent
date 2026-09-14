from app.llm.providers.mock_provider import MockLLMProvider


async def test_mock_provider_generates_response() -> None:
    provider = MockLLMProvider()

    response = await provider.generate(
        prompt="Build a Python REST API."
    )

    assert isinstance(response, str)
    assert len(response) > 0