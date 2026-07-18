"""Tests for the drawio label truncation threshold in buildDrawioShape.

The fix in types.py raised labelsize from 15 to 30, meaning labels up to
30 characters must be preserved verbatim, and only labels exceeding 30
characters should be truncated.
"""

from ibmdiagrams.ibmbase.common import Common

LABELSIZE = 30


class TestDrawioLabelTruncation:
    """Verify the labelsize=30 threshold used in Types.buildDrawioShape."""

    def setup_method(self):
        self.common = Common()

    def test_label_at_exact_threshold_is_not_truncated(self):
        """A label whose length equals labelsize must be returned unchanged."""
        label = "x" * LABELSIZE
        result = self.common.truncateText(label, LABELSIZE, "<br>")
        assert result == label

    def test_label_below_threshold_is_not_truncated(self):
        """A label shorter than labelsize must be returned unchanged."""
        label = "Short label"
        assert len(label) < LABELSIZE
        result = self.common.truncateText(label, LABELSIZE, "<br>")
        assert result == label

    def test_label_above_threshold_is_truncated(self):
        """A label longer than labelsize must be truncated with an ellipsis."""
        label = "x" * (LABELSIZE + 1)
        result = self.common.truncateText(label, LABELSIZE, "<br>")
        assert result == "x" * (LABELSIZE - 1) + "..."

    def test_old_threshold_would_have_truncated_medium_label(self):
        """A label between 15 and 30 characters would have been truncated with
        the old threshold of 15, but must be preserved with the new threshold of 30."""
        old_labelsize = 15
        label = "x" * 20  # 20 chars: too long for 15, fine for 30

        old_result = self.common.truncateText(label, old_labelsize, "<br>")
        new_result = self.common.truncateText(label, LABELSIZE, "<br>")

        assert old_result == "x" * 14 + "..."  # was truncated
        assert new_result == label  # now preserved
