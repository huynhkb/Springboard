const input = document.querySelector('#fruit');
const suggestions = document.querySelector('.suggestions ul');
const fruit = ['Apple', 'Apricot', 'Avocado 🥑', 'Banana', 'Bilberry', 'Blackberry', 'Blackcurrant', 'Blueberry', 'Boysenberry', 'Currant', 'Cherry', 'Coconut', 'Cranberry', 'Cucumber', 'Custard apple', 'Damson', 'Date', 'Dragonfruit', 'Durian', 'Elderberry', 'Feijoa', 'Fig', 'Gooseberry', 'Grape', 'Raisin', 'Grapefruit', 'Guava', 'Honeyberry', 'Huckleberry', 'Jabuticaba', 'Jackfruit', 'Jambul', 'Juniper berry', 'Kiwifruit', 'Kumquat', 'Lemon', 'Lime', 'Loquat', 'Longan', 'Lychee', 'Mango', 'Mangosteen', 'Marionberry', 'Melon', 'Cantaloupe', 'Honeydew', 'Watermelon', 'Miracle fruit', 'Mulberry', 'Nectarine', 'Nance', 'Olive', 'Orange', 'Clementine', 'Mandarine', 'Tangerine', 'Papaya', 'Passionfruit', 'Peach', 'Pear', 'Persimmon', 'Plantain', 'Plum', 'Pineapple', 'Pomegranate', 'Pomelo', 'Quince', 'Raspberry', 'Salmonberry', 'Rambutan', 'Redcurrant', 'Salak', 'Satsuma', 'Soursop', 'Star fruit', 'Strawberry', 'Tamarillo', 'Tamarind', 'Yuzu'];


function search(str) {
	const results = [];
	if (str.trim()) {
		const inputVal = str.toLowerCase();
		fruit.filter(item => item.toLowerCase().includes(inputVal.toLowerCase()) ? results.push(item) : null);
	}
	// TODO
	return results;
};

function searchHandler(e) {
	const typedInput = e.target.value;
	const matchedResults = search(typedInput);
	showSuggestions(matchedResults, typedInput);
	// TODO
}

function showSuggestions(results, inputVal) {
	// TODO
	suggestions.innerHTML = ''; //To clear the list content before populating a new list
	results.map(result => {
		const sugList = document.createElement('li');
		const boldMatch = result.toLowerCase().indexOf(inputVal); //check to see if ANY char of input matches 
		if (boldMatch !== -1) {
			sugList.innerHTML = result.substring(0, boldMatch) + result.substring(boldMatch, boldMatch + inputVal.length).bold() + result.substring(boldMatch + inputVal.length);
			console.log(sugList.innerHTML);
		} else {
			sugList.innerHTML = result;
		}
		suggestions.append(sugList);
	});
}

function useSuggestion(e) {
	if (e.target.tagName === 'LI') {
		const selectedFruit = e.target.innerText;
        input.value = selectedFruit + " ❤️";
        suggestions.innerHTML = '';
	}
	// TODO
}

input.addEventListener('keyup', searchHandler);
suggestions.addEventListener('click', useSuggestion);