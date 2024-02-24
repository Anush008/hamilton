import numpy as np
import pandas as pd
import vaex

from hamilton.function_modifiers import extract_columns


@extract_columns("signups", "spend")
def base_df(base_df_location: str) -> vaex.dataframe.DataFrame:
    """Loads base dataframe of data.

    :param base_df_location: just showing that we could load this from a file...
    :return:
    """
    return vaex.from_pandas(
        pd.DataFrame(
            {
                "signups": [1, 10, 50, 100, 200, 400],
                "spend": [10, 10, 20, 40, 40, 50],
            }
        )
    )


def spend_per_signup(
    spend: vaex.expression.Expression, signups: vaex.expression.Expression
) -> vaex.expression.Expression:
    """The cost per signup in relation to spend."""
    return spend / signups


def spend_mean(spend: vaex.expression.Expression) -> float:
    """Shows function creating a scalar. In this case it computes the mean of the entire column."""
    return spend.mean()


def spend_zero_mean(spend: vaex.expression.Expression, spend_mean: float) -> np.ndarray:
    """Shows function that takes a scalar and returns np.ndarray."""
    return (spend - spend_mean).to_numpy()


def spend_std_dev(spend: vaex.expression.Expression) -> float:
    """Function that computes the standard deviation of the spend column."""
    return spend.std()


def spend_zero_mean_unit_variance(spend_zero_mean: np.ndarray, spend_std_dev: float) -> np.ndarray:
    """Function showing one way to make spend have zero mean and unit variance."""
    return spend_zero_mean / spend_std_dev
