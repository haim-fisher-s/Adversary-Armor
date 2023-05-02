"""Performs general tests."""
import main
from advarmor.libs import tokenizer as SM


def test_amodule():
    """Test amodule.hello()."""
    main.hello()


def test_true():
    """Just asserts True."""
    assert True


def test_sampleclass():
    """Test samplemodule SampleClass true method."""
    s = SM.SampleClass()
    assert s.true() is True


def test_sampleclass_false():
    """Test samplemodule SampleClass false classmethod."""
    assert SM.SampleClass.false() is False


def test_undoc_func():
    """Test the undocumented function."""
    SM.this_is_and_undocumented_function("some")
