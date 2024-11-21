# Pong Game

This project implements a classic Pong game using Python and Pygame. Below is an explanation of the code's structure and key components.

## **Overview**
The Pong game consists of the main game loop and three primary objects: the ball, paddles, and the game logic. The goal is for players to score points by ensuring the ball passes the opponent's paddle.

## **Components**

### **1. Main Script (`main.py`)**
The `main.py` script initializes the game and manages the main loop:
- **Game Initialization:** Configures the Pygame window, dimensions, colors, and initial player scores.
- **Game Loop:** Handles game updates, including:
  - Rendering the game elements (paddles, ball, scores).
  - Processing user inputs to control paddle movements.
  - Manage ball collisions and reset states when a point is scored.
  - Detecting victory conditions and displaying a win message.
- **Dependencies:** Utilizes `game.py`, `paddle.py`, and `ball.py` for game mechanics.

### **2. Ball (`ball.py`)**
The `Ball` class defines the behavior and properties of the ball:
- **Attributes:**
  - `init_vel`: Random initial velocity to determine the ball's initial direction.
  - `max_vel`: Limits the maximum velocity of the ball.
  - `radius`: Sets the ball's size.
  - Coordinates (`x`, `y`) and velocities (`x_vel`, `y_vel`).
- **Methods:**
  - `move()`: Updates the ball's position based on its velocity.
  - `reset()`: Resets the ball to its starting position and reverses its horizontal direction.
  - `draw()`: Renders the ball on the game window.

### **3. Paddle (`paddle.py`)**
The `Paddle` class handles the behavior of the paddles:
- **Attributes:**
  - `width` and `height`: Define the paddle dimensions.
  - `vel`: Specifies the speed at which the paddle can move.
  - Coordinates (`x`, `y`) for position.
- **Methods:**
  - `move(up)`: Moves the paddle up or down based on the direction specified.
  - `reset()`: Resets the paddle to its initial position.
  - `draw()`: Renders the paddle on the game window.

### **4. Game Logic (`game.py`)**
The `Game` class manages the overall game mechanics:
- **Attributes:**
  - `window_width` and `window_height`: Dimensions of the game window.
  - `window`: Pygame surface used for rendering.
- **Methods:**
  - `handle_paddle_movement(keys, left_paddle, right_paddle)`: Detects player input to move paddles within the window boundaries.
  - `handle_collision(ball, left_paddle, right_paddle)`: Handles collisions:
    - Ball bouncing off walls and paddles.
    - Adjusts ball velocity based on the collision point to simulate realistic behavior.
  - `draw(window, paddles, ball, left_score, right_score)`: Renders all game elements:
    - Paddles, ball, scores, and the dashed midline.

## **Gameplay Dynamics**
1. The game starts with the ball moving toward one paddle.
2. Players use the keyboard to control their paddles:
   - **Left Player:** `W` (up) and `S` (down).
   - **Right Player:** Arrow keys (`UP` and `DOWN`).
3. The ball bounces off paddles and walls, with its velocity adjusted on paddle collisions.
4. When the ball passes a paddle, the opposing player scores a point.
5. The game ends when one player reaches the winning score (`score_win`).

---

This project was an excellent introduction to game development concepts such as collision detection, movement mechanics, and user input handling, all implemented using the Pygame library.
