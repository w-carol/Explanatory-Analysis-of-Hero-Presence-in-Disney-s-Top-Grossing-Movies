import pandas as pd
import altair as alt
import pytest 

from plot_hero_presence import plot_hero_presence


def test_plot_hero_presence():

    # create helper data and write tests for the function
    helper_data = pd.DataFrame(
        {
            "movie_title": [
                "Shang-Chi",
                "Logan",
                "Spider-Man",
                "Black Widow",
                "Sky High",
            ],
            "total_gross": [2000, 5000, 8000, 1000, 3000],
            "has_hero": ["yes", "no", "yes", "yes", "no"],
        }
    )

    chart = plot_hero_presence(helper_data, 3)

    assert chart["movie_title"].dtype == str, "Movie title should be type of str."
    assert isinstance(chart, alt.Chart), "The output should be an Altair chart."
    assert (
        chart.title == "Movie Revenue by Hero Presence"
    ), "The chart title is incorrect."


test_plot_hero_presence()
