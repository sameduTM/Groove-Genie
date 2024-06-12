# Groove-Genie

Groove-Genie is a web application that allows users to explore, like, and get recommendations for songs based on their preferences. It features a search functionality, song detail pages, liked songs list, and recommendations based on liked songs.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- **Explore Music**: Search for songs, artists, or albums.
- **Song Details**: View detailed information about each song, including the option to like or dislike.
- **Liked Songs**: View a list of all liked songs.
- **Recommendations**: Get song recommendations based on your liked songs.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript, Font Awesome
- **Backend**: Python, Flask
- **Database**: Pandas (for handling CSV data)
- **Machine Learning**: Scikit-learn (for song recommendation)

## Setup and Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/groove-genie.git
    cd groove-genie
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:
    ```bash
    python app.py
    ```

5. Open your web browser and navigate to `http://127.0.0.1:5000`.

## Usage

### Exploring Music
- Use the search bar on the home page to find songs by name, artist, or genre.

### Viewing Song Details
- Click on a song from the search results to view its details.
- Like or dislike a song from its detail page.

### Viewing Liked Songs
- Navigate to the "Liked Songs" page to view a list of all songs you have liked.

### Getting Recommendations
- Navigate to the "Recommendations" page to get song recommendations based on your liked songs.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add new feature"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Create a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
If you have any questions or suggestions, feel free to contact us at:
- **Email**: wanyamak884@gmail.com
- **GitHub**: [sameduTM](https://github.com/sameduTM)
