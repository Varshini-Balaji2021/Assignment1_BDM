// ============================================================
// PLATE 2 PLATE
// FRONTEND JAVASCRIPT
// FASTAPI + SUPABASE
// ============================================================


// ============================================================
// 1. NAVIGATION
// ============================================================

function showSection(sectionId) {

    const section = document.getElementById(sectionId);

    if (section) {
        section.scrollIntoView({
            behavior: "smooth"
        });
    }

}


// ============================================================
// 2. BACKEND CONNECTION TEST
// ============================================================

async function testBackendConnection() {

    const status =
        document.getElementById("connection-status");

    try {

        const response =
            await fetch("/api/connection");

        const result =
            await response.json();

        console.log("Backend connection:", result);

        if (result.connected) {

            if (status) {
                status.textContent =
                    "Connected to Plate 2 Plate database";
            }

            return true;

        }

        if (status) {
            status.textContent =
                "Database connection failed";
        }

        console.error(
            "Database error:",
            result.error
        );

        return false;

    }

    catch (error) {

        console.error(
            "Backend connection error:",
            error
        );

        if (status) {
            status.textContent =
                "Backend connection failed";
        }

        return false;

    }

}


// ============================================================
// 3. LOAD SURPLUS FOOD
// ============================================================

async function loadSurplusFood() {

    const container =
        document.getElementById(
            "surplus-container"
        );

    if (!container) {
        return;
    }

    container.innerHTML =
        "<p>Loading surplus food...</p>";

    try {

        const response =
            await fetch("/api/surplus");

        const data =
            await response.json();

        if (!response.ok || data.success === false) {
            throw new Error(
                data.error || "Unable to load surplus food"
            );
        }

        container.innerHTML = "";

        if (!data || data.length === 0) {

            container.innerHTML =
                "<p>No surplus food found.</p>";

            return;
        }

        data.forEach(food => {

            const card =
                document.createElement("div");

            card.className = "card";

            card.innerHTML = `

                <h3>
                    🍞 ${food["Product Name"] || "Food Item"}
                </h3>

                <p>
                    <strong>Bakery ID:</strong>
                    ${food["Bakery ID"] || "-"}
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
                    <strong>Quantity Available:</strong>
                    ${food["Quantity Available"] || 0}
                </p>

                <p>
                    <strong>Daily Surplus:</strong>
                    ${food["Daily Surplus Quantity"] || 0}
                </p>

            `;

            container.appendChild(card);

        });

    }

    catch (error) {

        console.error(
            "Surplus error:",
            error
        );

        container.innerHTML =
            `<p>❌ Unable to load surplus food.</p>`;

    }

}


// ============================================================
// 4. LOAD BAKERIES
// ============================================================

async function loadBakeries() {

    const container =
        document.getElementById(
            "bakery-container"
        );

    if (!container) {
        return;
    }

    container.innerHTML =
        "<p>Loading bakeries...</p>";

    try {

        const response =
            await fetch("/api/bakeries");

        const data =
            await response.json();

        if (!response.ok || data.success === false) {
            throw new Error(
                data.error || "Unable to load bakeries"
            );
        }

        container.innerHTML = "";

        if (!data || data.length === 0) {

            container.innerHTML =
                "<p>No bakeries found.</p>";

            return;
        }

        data.forEach(bakery => {

            const card =
                document.createElement("div");

            card.className = "card";

            card.innerHTML = `

                <h3>
                    🏪 ${bakery["Bakery Name"] || bakery.bakery_name || "-"}
                </h3>

                <p>
                    <strong>Branch:</strong>
                    ${bakery["Branch Name"] || bakery.branch_name || "-"}
                </p>

                <p>
                    <strong>City:</strong>
                    ${bakery["City"] || bakery.city || "-"}
                </p>

                <p>
                    <strong>Address:</strong>
                    ${bakery["Address"] || bakery.address || "-"}
                </p>

            `;

            container.appendChild(card);

        });

    }

    catch (error) {

        console.error(
            "Bakery error:",
            error
        );

        container.innerHTML =
            "<p>❌ Unable to load bakeries.</p>";

    }

}


// ============================================================
// 5. LOAD NGOs
// ============================================================

async function loadNGOs() {

    const container =
        document.getElementById(
            "ngo-container"
        );

    if (!container) {
        return;
    }

    container.innerHTML =
        "<p>Loading NGOs...</p>";

    try {

        const response =
            await fetch("/api/ngos");

        const data =
            await response.json();

        if (!response.ok || data.success === false) {
            throw new Error(
                data.error || "Unable to load NGOs"
            );
        }

        container.innerHTML = "";

        if (!data || data.length === 0) {

            container.innerHTML =
                "<p>No NGOs found.</p>";

            return;
        }

        data.forEach(ngo => {

            const card =
                document.createElement("div");

            card.className = "card";

            card.innerHTML = `

                <h3>
                    🤝 ${ngo["NGO Name"] || ngo.ngo_name || "-"}
                </h3>

                <p>
                    <strong>City:</strong>
                    ${ngo["City"] || ngo.city || "-"}
                </p>

                <p>
                    <strong>Contact:</strong>
                    ${ngo["Contact Number"] || ngo.contact_number || "-"}
                </p>

            `;

            container.appendChild(card);

        });

    }

    catch (error) {

        console.error(
            "NGO error:",
            error
        );

        container.innerHTML =
            "<p>❌ Unable to load NGOs.</p>";

    }

}


// ============================================================
// 6. LOAD DONATIONS
// ============================================================

async function loadDonations() {

    const container =
        document.getElementById(
            "donation-container"
        );

    if (!container) {
        return;
    }

    container.innerHTML =
        "<p>Loading donations...</p>";

    try {

        const response =
            await fetch("/api/donations");

        const data =
            await response.json();

        if (!response.ok || data.success === false) {
            throw new Error(
                data.error || "Unable to load donations"
            );
        }

        container.innerHTML = "";

        if (!data || data.length === 0) {

            container.innerHTML =
                "<p>No donations found.</p>";

            return;
        }

        data.forEach(donation => {

            const card =
                document.createElement("div");

            card.className = "card";

            card.innerHTML = `

                <h3>
                    🎁 ${donation.product_name || donation["Product Name"] || "-"}
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
                    <strong>Pickup Status:</strong>
                    ${donation.pickup_status || "-"}
                </p>

            `;

            container.appendChild(card);

        });

    }

    catch (error) {

        console.error(
            "Donation error:",
            error
        );

        container.innerHTML =
            "<p>❌ Unable to load donations.</p>";

    }

}


// ============================================================
// 7. COMPLETE BUSINESS ANALYSIS
// ============================================================

async function loadBusinessAnalysis() {

    console.log(
        "Loading complete Business Analysis..."
    );

    try {

        // IMPORTANT:
        // We no longer read:
        // results/analysis/business_analysis.json
        //
        // Everything now comes from FastAPI.

        const response =
            await fetch(
                "/api/business-analysis"
            );

        if (!response.ok) {

            throw new Error(
                "Business Analysis API failed"
            );

        }

        const data =
            await response.json();

        console.log(
            "Business Analysis:",
            data
        );

        if (!data.success) {

            throw new Error(
                data.error ||
                "Business Analysis failed"
            );

        }


        // ====================================================
        // BUSINESS METRICS
        // ====================================================

        const totalSurplus =
            document.getElementById(
                "business-total-surplus"
            );

        const totalWaste =
            document.getElementById(
                "business-total-waste"
            );

        const totalDonated =
            document.getElementById(
                "business-total-donated"
            );

        const donationRate =
            document.getElementById(
                "business-donation-rate"
            );


        if (totalSurplus) {

            totalSurplus.textContent =
                data.metrics.total_surplus;

        }


        if (totalWaste) {

            totalWaste.textContent =
                data.metrics.total_waste;

        }


        if (totalDonated) {

            totalDonated.textContent =
                data.metrics.total_donations;

        }


        if (donationRate) {

            donationRate.textContent =
                data.metrics.donation_rate +
                "%";

        }


        // ====================================================
        // KEY FINDINGS
        // ====================================================

        const highestSurplusCategory =
            document.getElementById(
                "highest-surplus-category"
            );

        const highestWasteCategory =
            document.getElementById(
                "highest-waste-category"
            );


        if (highestSurplusCategory) {

            highestSurplusCategory.textContent =
                data.key_findings
                    .highest_surplus_category;

        }


        if (highestWasteCategory) {

            highestWasteCategory.textContent =
                data.key_findings
                    .highest_waste_category;

        }


        // ====================================================
        // TOP BAKERIES
        // ====================================================

        const bakeryContainer =
            document.getElementById(
                "top-bakeries-container"
            );

        if (bakeryContainer) {

            bakeryContainer.innerHTML = "";

            if (
                data.top_bakeries &&
                data.top_bakeries.length > 0
            ) {

                data.top_bakeries.forEach(
                    (bakery, index) => {

                        const row =
                            document.createElement(
                                "div"
                            );

                        row.className =
                            "analysis-row";

                        row.innerHTML = `

                            <p>
                                <strong>
                                    ${index + 1}.
                                    Bakery ${bakery.bakery_id}
                                </strong>

                                —
                                ${bakery.surplus_quantity}
                                units surplus
                            </p>

                        `;

                        bakeryContainer
                            .appendChild(row);

                    }
                );

            }

            else {

                bakeryContainer.innerHTML =
                    "<p>No bakery analysis available.</p>";

            }

        }


        // ====================================================
        // FOOD CATEGORY ANALYSIS
        // ====================================================

        const categoryContainer =
            document.getElementById(
                "deeper-category-container"
            );

        if (categoryContainer) {

            categoryContainer.innerHTML = "";

            if (
                data.category_analysis &&
                data.category_analysis.length > 0
            ) {

                data.category_analysis.forEach(
                    category => {

                        const row =
                            document.createElement(
                                "div"
                            );

                        row.className =
                            "analysis-row";

                        row.innerHTML = `

                            <p>
                                <strong>
                                    ${category.category}
                                </strong>
                            </p>

                            <p>
                                Total Surplus:
                                ${category.total_surplus}
                            </p>

                            <p>
                                Total Waste:
                                ${category.total_waste}
                            </p>

                            <p>
                                Average Daily Sales:
                                ${category.average_sales}
                            </p>

                        `;

                        categoryContainer
                            .appendChild(row);

                    }
                );

            }

            else {

                categoryContainer.innerHTML =
                    "<p>No category analysis available.</p>";

            }

        }


        // ====================================================
        // HIGH-WASTE PRODUCTS
        // ====================================================

        const wasteContainer =
            document.getElementById(
                "high-waste-container"
            );

        if (wasteContainer) {

            wasteContainer.innerHTML = "";

            if (
                data.high_waste_products &&
                data.high_waste_products.length > 0
            ) {

                data.high_waste_products.forEach(
                    product => {

                        const row =
                            document.createElement(
                                "div"
                            );

                        row.className =
                            "analysis-row";

                        row.innerHTML = `

                            <p>
                                <strong>
                                    ${product.product}
                                </strong>
                                (${product.category})
                            </p>

                            <p>
                                Average Daily Waste:
                                ${product.waste}
                            </p>

                        `;

                        wasteContainer
                            .appendChild(row);

                    }
                );

            }

            else {

                wasteContainer.innerHTML =
                    "<p>No high-waste products available.</p>";

            }

        }


        // ====================================================
        // HIGH-SURPLUS PRODUCTS
        // ====================================================

        const surplusContainer =
            document.getElementById(
                "high-surplus-container"
            );

        if (surplusContainer) {

            surplusContainer.innerHTML = "";

            if (
                data.high_surplus_products &&
                data.high_surplus_products.length > 0
            ) {

                data.high_surplus_products.forEach(
                    product => {

                        const row =
                            document.createElement(
                                "div"
                            );

                        row.className =
                            "analysis-row";

                        row.innerHTML = `

                            <p>
                                <strong>
                                    ${product.product}
                                </strong>
                                (${product.category})
                            </p>

                            <p>
                                Daily Surplus:
                                ${product.surplus}
                            </p>

                        `;

                        surplusContainer
                            .appendChild(row);

                    }
                );

            }

            else {

                surplusContainer.innerHTML =
                    "<p>No high-surplus products available.</p>";

            }

        }


        // ====================================================
        // DONATION AVAILABILITY
        // ====================================================

        const donationContainer =
            document.getElementById(
                "donation-availability-container"
            );

        if (donationContainer) {

            donationContainer.innerHTML = "";

            if (
                data.donation_availability &&
                data.donation_availability.length > 0
            ) {

                data.donation_availability.forEach(
                    item => {

                        const row =
                            document.createElement(
                                "div"
                            );

                        row.className =
                            "analysis-row";

                        row.innerHTML = `

                            <p>
                                <strong>
                                    Donation Available:
                                    ${item.status}
                                </strong>
                            </p>

                            <p>
                                Products:
                                ${item.products}
                            </p>

                            <p>
                                Total Surplus:
                                ${item.total_surplus}
                            </p>

                            <p>
                                Total Waste:
                                ${item.total_waste}
                            </p>

                        `;

                        donationContainer
                            .appendChild(row);

                    }
                );

            }

            else {

                donationContainer.innerHTML =
                    "<p>No donation availability analysis available.</p>";

            }

        }


        // ====================================================
        // REMOVE OLD UNUSED ANALYSIS SECTIONS
        // ====================================================

        const wasteLevelContainer =
            document.getElementById(
                "waste-level-container"
            );

        if (wasteLevelContainer) {

            wasteLevelContainer.parentElement
                .style.display = "none";

        }


        const surplusLevelContainer =
            document.getElementById(
                "surplus-level-container"
            );

        if (surplusLevelContainer) {

            surplusLevelContainer.parentElement
                .style.display = "none";

        }


        console.log(
            "Business Analysis successfully displayed."
        );

    }

    catch (error) {

        console.error(
            "Business Analysis error:",
            error
        );


        const ids = [

            "business-total-surplus",
            "business-total-waste",
            "business-total-donated",
            "business-donation-rate",
            "highest-surplus-category",
            "highest-waste-category"

        ];


        ids.forEach(id => {

            const element =
                document.getElementById(id);

            if (element) {

                element.textContent =
                    "Unable to load";

            }

        });


        const containers = [

            "top-bakeries-container",
            "deeper-category-container",
            "high-waste-container",
            "high-surplus-container",
            "donation-availability-container"

        ];


        containers.forEach(id => {

            const element =
                document.getElementById(id);

            if (element) {

                element.innerHTML =
                    "<p>Unable to load business analysis.</p>";

            }

        });

    }

}


// ============================================================
// 8. START APPLICATION
// ============================================================

async function loadApplication() {

    console.log(
        "===================================="
    );

    console.log(
        "Starting Plate 2 Plate..."
    );

    console.log(
        "===================================="
    );


    // --------------------------------------------------------
    // TEST FASTAPI + DATABASE
    // --------------------------------------------------------

    const connected =
        await testBackendConnection();

    if (!connected) {

        console.error(
            "FastAPI/database connection failed."
        );

        return;

    }


    // --------------------------------------------------------
    // EXISTING WEBSITE DATA
    // --------------------------------------------------------

    await loadSurplusFood();

    await loadBakeries();

    await loadNGOs();

    await loadDonations();


    // --------------------------------------------------------
    // ONE COMPLETE BUSINESS ANALYSIS
    // --------------------------------------------------------

    await loadBusinessAnalysis();


    console.log(
        "Plate 2 Plate loaded successfully."
    );

}


// ============================================================
// 9. START WHEN HTML IS READY
// ============================================================

document.addEventListener(
    "DOMContentLoaded",
    loadApplication
);