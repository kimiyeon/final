async function generate() {
    const family_size = parseInt(document.getElementById("family").value);

    const allergies = document.getElementById("allergies").value
        .split(",")
        .map(x => x.trim())
        .filter(Boolean);

    const purpose = document.getElementById("purpose").value;
    const budget = parseInt(document.getElementById("budget").value);

    const response = await fetch("/generate-shopping-list", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            family_size,
            allergies,
            purpose,
            budget
        })
    });

    const data = await response.json();

    let html = `<h2>Meal Plan</h2><ul>`;
    data.meal_plan.forEach(item => {
        html += `<li>${item}</li>`;
    });

    html += `</ul><h2>Shopping List</h2><ul>`;

    data.shopping_list.forEach(item => {
        html += `<li>${item.name}: ₩${item.price}</li>`;
    });

    html += `</ul><h2>Total Cost: ₩${data.total_cost}</h2>`;

    document.getElementById("result").innerHTML = html;
}