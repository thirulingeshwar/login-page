// Define valid username and password combinations with URLs
const validCredentials = {
    user: { password: "password", redirectUrl: "https://skola-home.vercel.app/" },
    user1: { password: "password1", redirectUrl: "https://example-link2.com/" },
    user2: { password: "password2", redirectUrl: "https://example-link3.com/" },
  };
  
  document.getElementById("login-form").addEventListener("submit", function (e) {
    e.preventDefault();
  
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const errorMessage = document.getElementById("error-message");
  
    // Check credentials
    if (validCredentials[username] && validCredentials[username].password === password) {
      window.location.href = validCredentials[username].redirectUrl;
    } else {
      errorMessage.textContent = "Invalid username or password!";
    }
  });
  