const api_key = 'MhAodEJIJxQMxW9XqxKjyXfNYdLoOIym';
const userInput = document.querySelector('#searchfield');
const form = document.querySelector('#searchform');
const imageZone = document.querySelector('#img-zone');


function appendImg(img){
    const gifArr = img.data.length;
    if (gifArr) {
        const newDiv = document.createElement("div");
        const newGif = document.createElement("img");
        newGif.src = img.data[Math.floor(Math.random() * gifArr)].images.original.url      // Since it's an array, need to access the index by random
        newGif.classList.add("w-100");
        newDiv.append(newGif);       // Appending to a div that's not part of DOM yet
        imageZone.append(newDiv);   // Appending to the image area that's part of the DOM
    }   
}
// getImg('cat', api_key);



form.addEventListener("submit", async function(e) {
    e.preventDefault();

    const input = userInput.value;
    userInput.value = '';
    // console.log(input)

    const retrieved = await axios.get('http://api.giphy.com/v1/gifs/search', { params: { q: input, api_key} });

    // console.log(retrieved);

    appendImg(retrieved.data);
});


$("#remove").on("click", function() {
    $(imageZone).empty();    // a jQuery method of clearing the DOM
  });

// console.log("Let's get this party started!");
