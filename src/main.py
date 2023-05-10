"""Main module."""
import datetime
import logging
import os
import pickle

import tensorflow as tf

from advarmor.libs import logging_config  # noqa
from advarmor.libs.tokenizer import Tokenizer


logger = logging.getLogger(__name__)


def get_inception_model() -> tf.keras.Model:
    """Get the inception model."""
    # Define the name of the pickle file
    pickle_filename = 'inception_model.pickle'

    # If the pickle file exists, load the model from the pickle file
    if os.path.exists(pickle_filename):
        with open(pickle_filename, 'rb') as f:
            model = pickle.load(f)
    # Otherwise, load the model from scratch and save it to the pickle file
    else:
        model = tf.keras.applications.InceptionV3(include_top=True, weights='imagenet')
        with open(pickle_filename, 'wb') as f:
            pickle.dump(model, f)

    return model


def main():
    """Run app flow."""
    start_time = datetime.datetime.now()
    
    model = get_inception_model()
    
    model.trainable = False
    tokenizer = Tokenizer(model)
    tokenizer.generate_tokens()

    end_time = datetime.datetime.now()
    logger.debug(f'advarmor done in :{end_time - start_time}')


if __name__ == "__main__":
    main()
