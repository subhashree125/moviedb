### MovieDB

The **moviedb** repository offers a comprehensive solution for managing and exploring movie and TV series data. It provides functionalities such as searching for movies or TV series by title, viewing trending content, accessing detailed information about specific titles—including cast, crew, and similar recommendations—and managing user profiles with customizable settings. The application fetches data from The Movie Database (TMDb) API to deliver up-to-date and extensive information on films and TV shows. Additionally, it features user authentication, allowing users to create accounts, log in, and manage their personal collections securely.

**Key Features:**

- **Search Functionality:** Allows users to search for movies or TV series by title.
- **Trending Content:** Displays a list of currently trending movies or TV series.
- **Detailed Information:** Provides detailed information about specific titles, including cast, crew, and similar recommendations.
- **User Profiles:** Enables users to create and manage their profiles with customizable settings.
- **User Authentication:** Supports user registration and login for a personalized experience.

**Technologies Used:**

- **Frontend:** Developed using React.js for building the user interface.
- **Backend:** Node.js and Express.js for server-side operations.
- **Database:** MongoDB for storing user data and application information.
- **Authentication:** JSON Web Tokens (JWT) for secure user authentication.
- **API Integration:** The Movie Database (TMDb) API for accessing movie and TV series data.

**Installation:**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/subhashree125/moviedb.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd moviedb
   ```

3. **Install Dependencies:**
   ```bash
   npm install
   ```

4. **Set Up Environment Variables:**
   Create a `.env` file in the root directory and add the following variables:
   ```
   PORT=5000
   MONGO_URI=your_mongodb_connection_string
   JWT_SECRET=your_jwt_secret
   TMDB_API_KEY=your_tmdb_api_key
   ```

5. **Start the Application:**
   ```bash
   npm start
   ``` 
