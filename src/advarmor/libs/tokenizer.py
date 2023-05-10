"""
Module responsible to creates tokens based on model parameters.

Contains:
    - Tokenizer
"""
import logging
from typing import Any

import numpy as np
import tensorflow as tf

from . import logging_config  # noqa


logger = logging.getLogger(__name__)


class Tokenizer:
    """Class to generate the tokens."""

    def __init__(self, model: Any):
        """Initiatlizes Tokenizer class."""
        self._model = model
        self._model_weights = np.empty((1))
        return

    def generate_tokens(self) -> None:
        """Generate tokens based on model parameters."""
        logger.debug('generate_tokens started')

        self._get_internal_model_weights()

    def _get_internal_model_weights(self) -> None:
        """Get internal model weights."""
        if isinstance(self._model, tf.keras.Model):
            self._handle_keras_model()

    def _handle_keras_model(self) -> None:
        """Get keras model weights."""
        important_by_magnitudes = self.get_important_neurons_using_weight_magnitudes()
        
        logger.debug(important_by_magnitudes[0].size)
        logger.debug(important_by_magnitudes[1].size)

    def get_important_neurons_using_weight_magnitudes(self, percentile: float = 0.40) -> tuple[np.array, np.array]:
        """Get the indices of the most important and unimportant neurons based on weight magnitudes.

        :Args:
            percentile (float): The percentile of neurons to select based on weight magnitudes.

        :Returns:
            Tuple[np.array, np.array]: A tuple containing two arrays - the indices of the most important neurons
            and the indices of the least important neurons.
        """
        # Get the weights of all trainable layers in the model
        model_weights = [layer.get_weights() for layer in self._model.layers]
        # Flatten the weights of each layer and concatenate them into a single array
        model_weights = [np.concatenate([w.flatten() for w in weights]) if weights else np.array([])
                         for weights in model_weights]
        # Flat the array of arrays nad init _model_weights
        self._model_weights = np.concatenate(model_weights)
        logger.debug(f'model weights count: {self._model_weights.size}')
        # Normalize
        self._model_weights = np.array(self._model_weights) / np.sum(self._model_weights)
        # Compute the number of important neurons to select based on the specified percentile
        num_important_neurons = int(self._model_weights.size * percentile)
        # Get the size of the unimportant neurons
        num_unimportant_neurons = self._model_weights.size - num_important_neurons
        # Get the indices of the least important neurons based on weight magnitudes
        unimportant_neurons = np.argsort(self._model_weights)[:num_unimportant_neurons]
        # Get the indices of the most important neurons based on weight magnitudes
        important_neurons = np.argsort(self._model_weights)[-num_important_neurons:]
        return (important_neurons, unimportant_neurons)
