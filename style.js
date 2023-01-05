$(document).ready(function(){

var elems = ["cloud", "medium-star"];
var weights = [100, 200]; // weight of each element above

var weighedElems = [];
var currentElem = 0;
while (currentElem < elems.length) {
  for (var i = 0; i < weights[currentElem]; i++)
    weighedElems[weighedElems.length] = elems[currentElem];
  currentElem++;
}

console.log(weighedElems);

var width = $(window).width() -200;
var height = $(window).height() -200;

console.log(width);
console.log(height);

for (var i = 0; i < 10; i++) {
  var left = Math.floor(Math.random() * width-15);
  var top = Math.floor(Math.random() * height-15);
  var rnd = Math.floor(Math.random() * weighedElems.length);
  document.getElementById("sky").insertAdjacentHTML('afterbegin', '<div class = "' + weighedElems[rnd] + '" style = "top: ' + top + 'px; left: ' + left + 'px;"></div>' );
}

});

