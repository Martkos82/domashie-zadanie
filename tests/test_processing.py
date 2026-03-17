import pytest
from processing import filter_by_state, sort_by_date

@pytest.fixture
def sample_data():
    return [
        {"id": 1, "state": "new", "date": "2023-09-01"},
        {"id": 2, "state": "done", "date": "2023-08-21"},
        {"id": 3, "state": "in_progress", "date": "2023-09-05"},
        {"id": 4, "state": "done", "date": "2023-09-02"},
    ]

def test_filter_by_state_found(sample_data):
    result = filter_by_state(sample_data, "done")
    assert len(result) == 2
    for item in result:
        assert item["state"] == "done"

def test_filter_by_state_not_found(sample_data):
    result = filter_by_state(sample_data, "archived")
    assert result == []

def test_sort_by_date_ascending(sample_data):
    sorted_list = sort_by_date(sample_data, reverse=False)
    dates = [item["date"] for item in sorted_list]
    assert dates == sorted(dates)

def test_sort_by_date_descending(sample_data):
    sorted_list = sort_by_date(sample_data, reverse=True)
    dates = [item["date"] for item in sorted_list]
    assert dates == sorted(dates, reverse=True)

@pytest.mark.parametrize(
    "dates, expected_order",
    [
        (["2023-09-01", "2023-08-21", "2023-09-05"], ["2023-09-05", "2023-09-01", "2023-08-21"]),
        (["bad-date", "2023-09-01"], ["2023-09-01", "bad-date"]),
    ]
)
def test_sort_with_various_dates(dates, expected_order):
    data = [{"date": d} for d in dates]
    result = sort_by_date(data, reverse=True)
    result_dates = [item["date"] for item in result]
    assert result_dates == expected_order