var slider = document.getElementById("input-temperature");
var output = document.getElementById("output-temperature");
output.innerHTML = slider.value + "&deg;C";

slider.oninput = function () {
  output.innerHTML = this.value + "&deg;C";
};

document.getElementById("diseaseForm").addEventListener("submit", function (event) {
  event.preventDefault(); // Prevent the default form submission
  sendData(); // Call a function to send data to the backend
});

function sendData() {
  const inputData = {
    temperature: parseFloat(document.getElementById("input-temperature").value),
    headache: parseFloat(document.getElementById("input-headache-level").value),
    eyepain: parseFloat(document.getElementById("input-eyepain-level").value),
    musclejointpain: parseFloat(document.getElementById("input-musclejointpain-level").value),
    nausea: parseFloat(document.getElementById("input-nausea-level").value),
    vomiting: document.getElementById("vomit-yes").checked,
    swollenglands: document.getElementById("swollen-gland-yes").checked,
    rash: document.getElementById("rash-yes").checked,
  };

  fetch("http://localhost:5000/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(inputData),
  })
    .then((response) => response.json())
    .then((data) => {
      // Handle the response from the backend
      console.log("Result from backend:", data.result);
      // Update your HTML with the result if needed
    })
    .catch((error) => console.error("Error:", error));
}
