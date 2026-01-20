const loginURL = "http://localhost:8000/login";
const signupURL = "http://localhost:8000/signup"

function login() {
  const name = document.getElementById("login-name").value;
  const password = document.getElementById("login-password").value;

  fetch(loginURL, {
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
    .then((json) => {
          const data = json;
          document.getElementById("login-output").textContent = data;
          console.log(data);
        })
    .catch((error) => console.error("Error:", error));
}

function signup() {
  const name = document.getElementById("signup-name").value;
  const password = document.getElementById("signup-password").value;

  fetch(signupURL, {
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
    .then((json) => {
          const data = json;
          document.getElementById("output-signup").textContent = data;
          console.log(data);
        })
    .catch((error) => console.error("Error:", error));
}
