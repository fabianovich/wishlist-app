const apiURL = "http://localhost:8000/wishlist/";

function api() {
  const name = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  fetch(apiURL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json; charset=UTF-8",
    },
    body: JSON.stringify({
      name: name,
      password: password,
    }),
  })
    .then((response) => response.json())
    .then((json) => {})
    .catch((error) => console.error("Error:", error));
}
