
        function login() {
            var email = document.getElementById("email").value;
            var password = document.getElementById("password").value;

            // Check if email and password are provided
            if (email.trim() === "" || password.trim() === "") {
                alert("Please enter email and password.");
                return;
            }

            // Replace this with your actual authentication logic
            var validEmail = "teacher@example.com";
            var validPassword = "password123";

            // Check if email and password are correct
            if (email === validEmail && password === validPassword) {
                // Redirect to teacher dashboard or any other page
                window.location.href = "teacher_dashboard.html";
            } else {
                alert("Invalid email or password. Please try again.");
            }
        }