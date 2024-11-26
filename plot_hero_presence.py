import pandas as pd
import altair as alt


def plot_hero_presence(df, N):

    """
    Reads the dataframe and create a bar chart showing the count of movies by hero presence for the top N rows.

    Parameters
    ----------
    df: pandas.core.frame.DataFrame
        The dataframe used for the plot.
    N: int
        Number of top rows selected for the plot. This also represent the top N movies with the highest revenue.

    Raises
    -------
    ValueError
        If N is greater than the number of rows in dataframe.
    TypeError
        If N is not an int type data.
    AssertError
        If 'has_hero' is not in the dataframe columns.

    Returns
    -------
    An altair bar chart that shows the count of movies by hero presence.


    Examples
    --------
    >>> plot_hero_presence(adjusted_merged_data, 50)

    """

    top_grossing_movies = df.iloc[0:N]
    movie_counts = top_grossing_movies["has_hero"].value_counts().reset_index()
    movie_counts.columns = ["has_hero", "count"]

    chart = (
        alt.Chart(movie_counts, width=400, height=300)
        .mark_bar()
        .encode(
            x=alt.X("has_hero:N", title="Hero Presence"),
            y=alt.Y("count:Q", title="Count of Movies"),
        )
        .properties(title="Count of Top Grossing Movies by Hero Presence")
    )

    # check if data is a the type of dataframe
    if not isinstance(df, pd.DataFrame):
        raise TypeError("The df augement is not of type DataFrame.")

    # check if N is greater than 0
    if N <= 0:
        raise ValueError("N must be a positive integer.")

    # check if N is less than the number of rows in data
    if N > len(df):
        raise ValueError(
            "N cannot be greater than the number of rows in the dataframe."
        )

    # Check if 'has_hero' column exists
    if "has_hero" not in df.columns:
        raise ValueError("'has_hero' column is missing from the DataFrame.")

    return chart
