# Crypto Dashboard Web App

A web application written in Dash for cryptocurrency market data visualization. 

## Table of Contents

* [Overview](#Overview)
* [Features](#Features)
* [Setup](#Setup)
* [Credits](#Credits)
* [License](#License)

## Overview

The web app is used to monitor and visualize financial data on the cryptocurrency market. It uses the Dash framework along with the Plotly library for displaying and updating charts interactively.

Data is collected in from the following financial services that provice free API keys:

* https://alternative.me/crypto/
* https://coincap.io/
* https://polygon.io/

Technologies used:

* Plotly/Dash
* Pandas
* SQLAlchemy (SQLite as DB backend)

## Features

The main view displays a graph of historical cryptocurrency prices which can be filtered by base currency cryptocurrencies, start date and end date.

Below the graph there's a dynamic table that shows the ten most biggest cryptocurrencies by market capitalization. 

Other financial indicators of the cryptocurrency market are also available:

* Fear and Greed Index.
* Bitcoin Relative Strength Index.
* Simple and Exponentially Weighted Moving Averages.

All of them can be filtered by indicator type and time period.

## Setup

* Clone repository

* Create and activate a new virtual environment

```
python3 -m venv YOUR_ENV_NAME
souce ./YOUR_ENV_NAME/bin/activate
```

* Rename .env.example to `.env` and set your value (get free API key from polygon.io)

```
POLYGON_API_KEY=<your_polygon_api_key>
```

* Install packages from `requirements.txt`

```
pip install -r requirements.txt
```

* Start app

```
python app.py
```

## Credits

This app is based on [this](https://github.com/szymcio32/currency-monitor-dash-app.git) currency monitor dash app, which has a similar functionality but focused on Fiat currencies.

## License

MIT License.
