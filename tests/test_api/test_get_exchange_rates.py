import pandas as pd
import pytest

from api import get_exchange_rates


class TestGetExchangeRates:

    @pytest.mark.vcr
    def test_successful_api_call(self):
        # Returns a pandas DataFrame object with exchange df_rates data when API call is successful
        expected_columns = [
            'id', 'symbol', 'currencySymbol', 
            'type', 'rateUsd'
        ]
        df_rates = get_exchange_rates()
        assert isinstance(df_rates, pd.DataFrame)
        assert not df_rates.empty
        assert all((col in expected_columns) for col in df_rates.columns)
        assert df_rates['symbol'].dtype == 'object'
        assert df_rates['rateUsd'].dtype == 'float64'
