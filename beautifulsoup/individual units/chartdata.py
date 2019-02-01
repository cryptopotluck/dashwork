import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go


fig = {
  "data": [
    {
      "values": [452, 651],
      "labels": [
        "Rooms Rented",
        "Available Rooms",
      ],
      "domain": {"x": [0, .48]},
      "name": "Kontiki Beach Resorts",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    },
    {
      "values": [718, 1922],
      "labels": [
        "Rooms Rented",
        "Available Rooms",
      ],
      "text":["CO2"],
      "textposition":"inside",
      "domain": {"x": [.52, 1]},
      "name": "Mrs. Kitty Rentals",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    }],
  "layout": {
        "title":"Fair Share Market Cap",
        "annotations": [
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "Kontiki",
                "x": 0.20,
                "y": 0.5
            },
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "Kitty",
                "x": 0.8,
                "y": 0.5
            }
        ]
    }
}
pyo.plot(fig, filename='donut')