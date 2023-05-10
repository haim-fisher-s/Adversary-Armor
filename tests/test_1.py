"""Performs general tests."""
import tensorflow as tf

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
    model = tf.keras.applications.InceptionV3(include_top=True,
                                              weights='imagenet')
    
    model.trainable = False
    t = Tokenizer(model)
    t.generate_tokens()
