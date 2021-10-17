
# Master Mind

MasterMind is a logic board game from the 70’s in which you have to co-
rrectly guess a random secret code in a determined number of guesses.

This game can be played by two players, the code-maker and the co-
de-breaker.

• The code-maker creates the secret combination, composed by a se-
quence of 4 colored pegs

• The code-breaker makes a series of guesses, each guess composed in
the same way by 4 colores pegs. After each guess, the code-maker gives

feedback to the code-breaker to see how close you got to the real se-
cret code.
  
## Roadmap

- Add database

- Parameterize the code
- Add container
- Make it a web service
- Make a global score rank
- Allow two or more players
- Allow diferent levels of complexity 
- Add more screen resolutions support

  
## Run Locally

Clone the project

```bash
  https://github.com/katacliny/InariChalengeMasterMindGame.git
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  python -m pip install -r requirements.txt
```

Run app

```bash
  python game.py
```

  
## Screenshots

![imagen](https://user-images.githubusercontent.com/34369026/137625851-8605755f-a47c-4e9f-a7f4-37074f47806b.png)
![imagen](https://user-images.githubusercontent.com/34369026/137626020-a5428def-1dd4-4903-933f-733a72bbad56.png)


  
## Running Tests

To run tests, run the following command

```bash
  pytest
```
## Limitations

This app is made to be executed especially on the terminal of the visual studio or on a high resolution monitor, preferably both.
  
