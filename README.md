# Interactive U.S. Tornado Tracks Map

This project is an interactive web application for visualizing U.S. tornado tracks, hail, and wind reports using Leaflet.js and CSV datasets. It allows users to:

- View tornado paths as color-coded lines by EF/F scale
- Filter by year and month
- Switch between tornado, hail, and wind datasets
- See event details in popups
- Explore a responsive, modern map UI

## Features
- **Dataset Selector:** Choose between tornadoes, all tornadoes, hail, and wind reports
- **Year/Month Filters:** Instantly filter events by year and month
- **Color-Coded Visualization:** Tornadoes as lines (by EF/F scale), hail and wind as points (by size/intensity)
- **Dynamic Legend:** Updates with dataset and filter selection
- **Professional Layout:** Responsive, accessible, and visually appealing
- **Attribution:** Written by Robert Massey

## Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/MasseyConsultants/WeatherAftermathTracker.git
   cd WeatherAftermathTracker
   ```
2. Ensure you have Python 3 installed.
3. Start the server:
   ```sh
   python server.py
   ```
4. Open your browser and navigate to `http://localhost:8000/Interactive%20U.S.html`

## Data
- Tornado, hail, and wind CSV files are located in the `Data/` directory.
- Data is loaded and filtered client-side using PapaParse.

## Credits
- Map tiles: [OpenStreetMap contributors](https://www.openstreetmap.org/)
- Mapping: [Leaflet.js](https://leafletjs.com/)
- CSV parsing: [PapaParse](https://www.papaparse.com/)
- Application: Written by Robert Massey

---

*For questions or contributions, please open an issue or pull request on GitHub.* 