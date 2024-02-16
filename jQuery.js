// 1. When the DOM is ready, console.log the message “Let’s get ready to party with jQuery!”
$(function () {
    console.log("Let's get ready to party with jQuery!");
});

// 2. Give all images inside of an article tag the class of image-center (this class is defined inside of the style tag in the head).
$('article img').addClass("image-center");

// 3. Remove the last paragraph in the article.
$('article p:last-child').remove();

// 4. Set the font size of the title to be a random pixel size from 0 to 100.
$('#title').css('font-size', Math.floor(Math.random() * 100));

// 5. Add an item to the list; it can say whatever you want.
$('ol').append('<li>HOWDY PATNA</li>');

// 6. Scratch that; the list is silly. Empty the aside and put a paragraph in it apologizing for the list’s existence.
$('aside').empty().append('<p>SORRY FOR THE LIST PATNA! DIS NOW A PARAGRAPH</p>');

// 7. When you change the numbers in the three inputs on the bottom, the background color of the body should change to match whatever the three values in the inputs are.
$('input[type="number"]').on('input', function() {
    let $number = $('input[type="number"]')
    let red = $number.eq(0).val();
    let green = $number.eq(1).val();
    let blue = $number.eq(2).val();
    $("body").css('background-color', `rgb(${red}, ${green}, ${blue})`);
  //$("body").css("background-color", "rgb(" + red + "," + green + "," + blue + ");    >>>>>> same thing, ${} is ES6!
});

// 8. Add an event listener so that when you click on the image, it is removed from the DOM.
$('img').on('click', function(){
    $(this).remove();
});









