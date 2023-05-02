"""Performs general tests."""
import main
from advarmor.libs.tokenizer import Tokenizer


def test_main():
    """Test amodule.hello()."""
    main.main()


def test_true():
    """Just asserts True."""
    assert True


def test_sampleclass():
    """Test samplemodule SampleClass true method."""
    t = Tokenizer()
    t.generate_tokens()
