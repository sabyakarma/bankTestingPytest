# import pytest
#
# condition = True
# @pytest.mark.skip("Checking the skip")
# def test_skipFunction():
#
#     global condition
#     condition = False
#     assert 1 == 1
#
#
# @pytest.mark.skipif(False, reason=f"Checking the skip with {condition}")
# def test_skipCondition():
#     assert 1 == 1
