// ========================================
// PLATE 2 PLATE
// SUPABASE + WEBSITE
// ========================================


// ========================================
// 1. NAVIGATION
// ========================================

function showSection(sectionId) {

    const section = document.getElementById(sectionId);

    if (section) {
        section.scrollIntoView({
            behavior: "smooth"
        });
    }

}


// ========================================
// 2. SUPABASE CONNECTION
// ========================================

const SUPABASE_URL =
    "https://ucxjzmgjmtdxtqqmdihd.supabase.co";

const SUPABASE_KEY =
    "sb_publishable_KcmP3rLIktUmFECB1Hwj9g_biGW-eT0";


const supabaseClient =
    window.supabase.createClient(
        SUPABASE_URL,
        SUPABASE_KEY
    );


// ========================================
// 3. TEST CONNECTION
// ========================================

async function testSupabaseConnection() {

    const status =
        document.getElementById("connection-status");

    if (!status) {
        console.log("Connection status element not found");
    }

    const { data, error } =
        await supabaseClient
            .from("ngos")
            .select("*")
            .limit(1);


    if (error) {

        console.error(
            "Supabase connection failed:",
            error
        );

        if (status) {
            status.innerHTML =
                "❌ Database connection failed<br>" +
                error.message;
        }

        return false;
    }


    console.log(
        "Supabase connected successfully!"
    );

    console.log(
        "NGO test data:",
        data
    );


    if (status) {
        status.innerHTML =
            "✅ Website connected to Supabase successfully!";
    }

    return true;
}


// ========================================
// 4. LOAD SURPLUS FOOD
// ========================================

async function loadSurplusFood() {

    const container =
        document.getElementById(
            "surplus-container"
        );


    if (!container) {
        console.error(
            "surplus-container not found"
        );
        return;
    }


    container.innerHTML =
        "<p>Loading surplus food...</p>";


    const { data, error } =
        await supabaseClient
            .from("food_waste")
            .select("*")
            .order(
                "Daily Surplus Quantity",
                {
                    ascending: false
                }
            );


    if (error) {

        console.error(
            "Food waste error:",
            error
        );

        container.innerHTML =
            `<p>❌ ${error.message}</p>`;

        return;
    }


    if (!data || data.length === 0) {

        container.innerHTML =
            "<p>No surplus food found.</p>";

        return;
    }


    container.innerHTML = "";


    data.forEach(food => {

        const card =
            document.createElement("div");

        card.className = "card";


        card.innerHTML = `

            <h3>
                🍞 ${food["Product Name"] || "Food Item"}
            </h3>

            <p>
                <strong>Bakery:</strong>
                ${food["Bakery Name"] || "-"}
            </p>

            <p>
                <strong>Branch:</strong>
                ${food["Branch Name"] || "-"}
            </p>

            <p>
                <strong>City:</strong>
                ${food["City"] || "-"}
            </p>

            <p>
                <strong>Category:</strong>
                ${food["Food Category"] || "-"}
            </p>

            <p>
                <strong>Quantity:</strong>
                ${food["Quantity Available"] || 0}
                ${food["Unit (pcs/kg)"] || ""}
            </p>

            <p>
                <strong>Daily Surplus:</strong>
                ${food["Daily Surplus Quantity"] || 0}
            </p>

            <p>
                <strong>Original Price:</strong>
                ₹${food["Original Price"] || 0}
            </p>

            <p>
                <strong>Discounted Price:</strong>
                ₹${food["Discounted Price"] || 0}
            </p>

            <p>
                <strong>Status:</strong>
                ${food["Availability Status"] || "-"}
            </p>

            <p>
                <strong>Donation Available:</strong>
                ${food["Donation Available (Yes/No)"] || "-"}
            </p>

        `;


        container.appendChild(card);

    });

}


// ========================================
// 5. LOAD BAKERIES
// ========================================

async function loadBakeries() {

    const container =
        document.getElementById(
            "bakery-container"
        );


    if (!container) {
        console.error(
            "bakery-container not found"
        );
        return;
    }


    container.innerHTML =
        "<p>Loading bakeries...</p>";


    const { data, error } =
        await supabaseClient
            .from("bakeries")
            .select("*")
            .order("Bakery Name");


    if (error) {

        console.error(
            "Bakery error:",
            error
        );

        container.innerHTML =
            `<p>❌ ${error.message}</p>`;

        return;
    }


    if (!data || data.length === 0) {

        container.innerHTML =
            "<p>No bakeries found.</p>";

        return;
    }


    container.innerHTML = "";


    data.forEach(bakery => {

        const card =
            document.createElement("div");

        card.className = "card";


        card.innerHTML = `

            <h3>
                🏪 ${bakery["Bakery Name"] || "-"}
            </h3>

            <p>
                <strong>Branch:</strong>
                ${bakery["Branch Name"] || "-"}
            </p>

            <p>
                <strong>City:</strong>
                ${bakery["City"] || "-"}
            </p>

            <p>
                <strong>Address:</strong>
                ${bakery["Address"] || "-"}
            </p>

            <p>
                <strong>Contact:</strong>
                ${bakery["Contact Number"] || "-"}
            </p>

            <p>
                <strong>Store Type:</strong>
                ${bakery["Store Type"] || "-"}
            </p>

        `;


        container.appendChild(card);

    });

}


// ========================================
// 6. LOAD NGOs
// ========================================

async function loadNGOs() {

    const container =
        document.getElementById(
            "ngo-container"
        );


    if (!container) {
        console.error(
            "ngo-container not found"
        );
        return;
    }


    container.innerHTML =
        "<p>Loading NGOs...</p>";


    const { data, error } =
        await supabaseClient
            .from("ngos")
            .select("*")
            .order("ngo_name");


    if (error) {

        console.error(
            "NGO error:",
            error
        );

        container.innerHTML =
            `<p>❌ ${error.message}</p>`;

        return;
    }


    if (!data || data.length === 0) {

        container.innerHTML =
            "<p>No NGOs found.</p>";

        return;
    }


    container.innerHTML = "";


    data.forEach(ngo => {

        const card =
            document.createElement("div");

        card.className = "card";


        card.innerHTML = `

            <h3>
                🤝 ${ngo.ngo_name || "-"}
            </h3>

            <p>
                <strong>City:</strong>
                ${ngo.city || "-"}
            </p>

            <p>
                <strong>Food Categories:</strong>
                ${ngo.food_categories_accepted || "-"}
            </p>

            <p>
                <strong>Pickup Available:</strong>
                ${ngo.pickup_available || "-"}
            </p>

            <p>
                <strong>Contact:</strong>
                ${ngo.contact_number || "-"}
            </p>

        `;


        container.appendChild(card);

    });

}


// ========================================
// 7. LOAD DONATIONS
// ========================================

async function loadDonations() {

    const container =
        document.getElementById(
            "donation-container"
        );


    if (!container) {
        console.error(
            "donation-container not found"
        );
        return;
    }


    container.innerHTML =
        "<p>Loading donations...</p>";


    const { data, error } =
        await supabaseClient
            .from("donations")
            .select("*")
            .order(
                "donation_date",
                {
                    ascending: false
                }
            );


    if (error) {

        console.error(
            "Donation error:",
            error
        );

        container.innerHTML =
            `<p>❌ ${error.message}</p>`;

        return;
    }


    if (!data || data.length === 0) {

        container.innerHTML =
            "<p>No donations found.</p>";

        return;
    }


    container.innerHTML = "";


    data.forEach(donation => {

        const card =
            document.createElement("div");

        card.className = "card";


        card.innerHTML = `

            <h3>
                🎁 ${donation.product_name || "-"}
            </h3>

            <p>
                <strong>Bakery ID:</strong>
                ${donation.bakery_id || "-"}
            </p>

            <p>
                <strong>NGO ID:</strong>
                ${donation.ngo_id || "-"}
            </p>

            <p>
                <strong>Quantity Donated:</strong>
                ${donation.quantity_donated || 0}
            </p>

            <p>
                <strong>Date:</strong>
                ${donation.donation_date || "-"}
            </p>

            <p>
                <strong>Pickup Status:</strong>
                ${donation.pickup_status || "-"}
            </p>

        `;


        container.appendChild(card);

    });

}


// ========================================
// 8. LOAD DASHBOARD COUNTS
// ========================================

async function loadDashboardStats() {

    const tables = [
        "food_waste",
        "bakeries",
        "ngos",
        "donations"
    ];


    for (const table of tables) {

        const { count, error } =
            await supabaseClient
                .from(table)
                .select("*", {
                    count: "exact",
                    head: true
                });


        if (error) {

            console.error(
                `Error counting ${table}:`,
                error
            );

            continue;
        }


        const element =
            document.getElementById(
                `${table}-count`
            );


        if (element) {

            element.textContent =
                count;

        }

    }

}


// ========================================
// 9. START EVERYTHING
// ========================================

async function loadApplication() {

    const connected =
        await testSupabaseConnection();


    if (!connected) {
        return;
    }


    await loadSurplusFood();

    await loadBakeries();

    await loadNGOs();

    await loadDonations();

    await loadDashboardStats();

}


// ========================================
// START
// ========================================

loadApplication();