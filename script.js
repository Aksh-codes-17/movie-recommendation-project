async function getRecommendation() {
    const movie = document.getElementById("movie").value;

    const response = await fetch("/recommend", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ movie: movie })
    });

    const data = await response.json();
    document.getElementById("result").innerText = data.join(", ");
}
