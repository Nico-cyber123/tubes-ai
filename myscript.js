var slider = document.getElementById("input-temperature");
var output = document.getElementById("output-temperature");
output.innerHTML = slider.value + "&deg;C"; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function () {
  output.innerHTML = this.value + "&deg;C";
};
