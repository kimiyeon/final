async function generate() {
    const family = document.getElementById("family").value
        .split(",")
        .map(x => x.trim())
        .filter(Boolean);

    const allergies = document.getElementById("allergies").value
        .split(",")
        .map(x => x.trim())
        .filter(Boolean);

    const purpose = document.getElementById("purpose").value;
    const budget = parseInt(document.getElementById("budget").value);

    const response = await fetch("http://127.0.0.1:8000/generate-shopping-list", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            family,
            allergies,
            purpose,
            budget
        })
    });

    const data = await response.json();

    let html = `
        <h2>Meal Plan</h2>
        <ul>
    `;

    data.meal_plan.forEach(item => {
        html += `<li>${item}</li>`;
    });

    html += `</ul><h2>Shopping List</h2><ul>`;

    data.shopping_list.forEach(item => {
        html += `<li>${item.item}: ₩${item.price}</li>`;
    });

    html += `</ul>`;
    html += `<h2>Total Cost: ₩${data.total_cost}</h2>`;

    document.getElementById("result").innerHTML = html;
}