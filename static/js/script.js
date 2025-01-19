document.getElementById("kundaliForm").addEventListener("submit", async function (e) {
    e.preventDefault(); // Prevent the default form submission

    // Collect form data
    const formData = new FormData(this);

    try {
        // Send data to the backend
        const response = await fetch("/generate_kundali", {
            method: "POST",
            body: formData, // FormData is directly sent without converting to JSON
        });

        const result = await response.json();

        if (result.success) {
            // Display the result in the modal
            const resultContent = document.getElementById("resultContent");
            resultContent.innerHTML = `<pre>${result.kundali}</pre>`;
            document.getElementById("resultModal").style.display = "block";
        } else {
            alert("Error generating Kundali: " + result.error);
        }
    } catch (error) {
        alert("An unexpected error occurred: " + error.message);
    }
});

// Close result modal
document.getElementById("closeModal").addEventListener("click", () => {
    document.getElementById("resultModal").style.display = "none";
});
