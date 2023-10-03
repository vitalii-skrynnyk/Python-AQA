import pytest
import random

from funcs import rand, rand_2


@pytest.mark.parametrize("mock_value", [0.499999999999999, 0.5, 0.5000000000000001])
def test_rand(mocker, mock_value):
    """Test if value is less than 0.5, the function raises RuntimeError. If value is more than 0.5, it returns value"""

    mocker.patch.object(random, "random", return_value=mock_value)

    if mock_value < 0.5:
        with pytest.raises(RuntimeError) as exc_info:
            rand()

        assert str(exc_info.value) == f"Result is less than 0.5: {mock_value}"

    else:
        assert rand() == mock_value


@pytest.mark.parametrize(
    ['values', 'res'],
    [
        [[2], (2, 1)],
        [[1, 2], (2, 2)],
        [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], (2, 10)],
    ],
)
def test_rand_2(mocker, values, res):
    """Test positive scenarios for rand function"""
    mocker.patch.object(random, 'random', side_effect=values)

    assert rand_2() == res



