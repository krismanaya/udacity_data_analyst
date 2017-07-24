// make array of numbers 
var data = [4, 8, 15, 16, 23, 42]; 

// selecting an element standard
var div = document.createElement('div'); 
div.innerHTML = "Hello, World"
document.body.appendChild(div); 

// create element d3
var body = d3.select("body");
var div = body.append("div");
div.html("Hello, world!");

// many elements
var section = d3.selectAll('section'); 
var div = section.append('div');
div.html('Hello, world!'); 


// chaining methods
var body = d3.select('body'); 
body.style('color', 'black');
body.style('background-color', 'white');

// chaining here 
d3.select('body')
    .style('color', 'black')
    .style('background-color', 'white')