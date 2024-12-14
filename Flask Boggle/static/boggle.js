class BoggleGame {
    // Start a new game with the given board and time limit
    constructor(boardId, secs = 60) {
      this.secs = secs; // game time in seconds
      this.score = 0; // starting score
      this.words = new Set(); // keep track of words already used
      this.board = $(`#${boardId}`); // grab the game board
  
      // Start the countdown
      this.showTimer();
      this.timer = setInterval(this.tick.bind(this), 1000);
  
      // Event listener for word submissions
      $(".add-word", this.board).on("submit", this.handleSubmit.bind(this));
    }
  
    // Add a word to the list on the board
    showWord(word) {
      $(".words", this.board).append($("<li>", { text: word }));
    }
  
    // Update the score display
    showScore() {
      $(".score", this.board).text(this.score);
    }
  
    // Display status message 
    showMessage(msg, cls) {
      $(".msg", this.board)
        .text(msg)
        .removeClass()
        .addClass(`msg ${cls}`);
    }
  
    // Check if it’s valid and update score when submitting
    async handleSubmit(evt) {
      evt.preventDefault(); // stop the form from refreshing the page
      const $word = $(".word", this.board);
  
      let word = $word.val();
      if (!word) return; // return if the input is empty
  
      if (this.words.has(word)) {
        this.showMessage(`You already found '${word}'!`, "err");
        return;
      }
  
      try {
        // Check if the word is valid with server
        const resp = await axios.get("/check", { params: { word: word } });
        if (resp.data.result === "not-word") {
          this.showMessage(`'${word}' isn’t a real word.`, "err");
        } else if (resp.data.result === "not-on-board") {
          this.showMessage(`'${word}' isn’t on this board.`, "err");
        } else {
          // Word is valid and on the board
          this.showWord(word);
          this.score += word.length;
          this.showScore();
          this.words.add(word);
          this.showMessage(`Nice! Added '${word}'.`, "ok");
        }
      } catch (err) {
        console.error("Error checking word:", err);
        this.showMessage("Something went wrong. Try again!", "err");
      }
  
      $word.val("").focus(); // clear the input and focus it again
    }
  
    // Update the timer display
    showTimer() {
      $(".timer", this.board).text(this.secs);
    }
  
    // Countdown logic: reduce seconds and stop game
    async tick() {
      this.secs -= 1;
      this.showTimer();
  
      if (this.secs <= 0) {
        clearInterval(this.timer); // stop the timer
        await this.scoreGame(); // finalize the score
      }
    }
  
    // End the game: hide input and show final score
    async scoreGame() {
      $(".add-word", this.board).hide(); // disable further input
  
      try {
        const resp = await axios.post("/score", { score: this.score });
        if (resp.data.brokeRecord) {
          this.showMessage(`Amazing! New record: ${this.score}`, "ok");
        } else {
          this.showMessage(`Final score: ${this.score}`, "ok");
        }
      } catch (err) {
        console.error("Error posting score:", err);
        this.showMessage("Couldn’t save your score. Try again!", "err");
      }
    }
  }
  