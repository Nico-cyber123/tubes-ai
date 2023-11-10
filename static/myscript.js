var slider = document.getElementById("input-temperature");
var output = document.getElementById("output-temperature");
output.innerHTML = slider.value + "&deg;C";

slider.oninput = function () {
  output.innerHTML = this.value + "&deg;C";
};