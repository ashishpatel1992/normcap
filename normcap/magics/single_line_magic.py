"""Magic Class to handle very simple single line text selection."""

from .base_magic import BaseMagic
from normcap.data_model import NormcapData


class SingleLineMagic(BaseMagic):
    def score(self, request: NormcapData) -> float:
        """Calc score based on amount of lines

        Arguments:
            BaseMagic {class} -- Base class for magics
            request {NormcapData} -- NormCap's session data

        Returns:
            float -- score between 0-100 (100 = more likely)
        """
        if len(request.line_boxes) == 1:
            self._final_score = 50
        if len(request.text) == 0:
            self._final_score = 1

        return self._final_score

    def transform(self, request: NormcapData) -> str:
        """Just transform into single line of text.

        Arguments:
            request {NormcapData} -- NormCap's session data

        Returns:
            str -- Single line of text
        """
        # Just return concatenated text
        # TODO: Maybe remove unnecessary whitespace?
        return request.text
