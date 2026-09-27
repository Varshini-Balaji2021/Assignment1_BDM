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
// DATABASE TABLE HELPER
// ============================================================

function renderDatabaseTable(
    container,
    data,
    emptyMessage,
    limit = 15
) {

    if (!container) return;

    if (!Array.isArray(data) || data.length === 0) {

        container.innerHTML =
            `<p>${emptyMessage}</p>`;

        return;
    }

    // Display only the requested number of records
    const displayData =
        data.slice(0, limit);

    const columns =
        Object.keys(displayData[0]);

    const table =
        document.createElement("table");

    table.className =
        "data-table";

    const thead =
        document.createElement("thead");

    const headerRow =
        document.createElement("tr");


    columns.forEach(column => {

        const th =
            document.createElement("th");

        th.textContent =
            column
                .replace(/_/g, " ")
                .replace(
                    /\b\w/g,
                    letter => letter.toUpperCase()
                );

        headerRow.appendChild(th);

    });


    thead.appendChild(headerRow);

    table.appendChild(thead);


    const tbody =
        document.createElement("tbody");


    displayData.forEach(record => {

        const row =
            document.createElement("tr");


        columns.forEach(column => {

            const td =
                document.createElement("td");

            const value =
                record[column];


            td.textContent =
                value === null ||
                value === undefined ||
                value === ""
                    ? "-"
                    : value;


            row.appendChild(td);

        });


        tbody.appendChild(row);

    });


    table.appendChild(tbody);


    const wrapper =
        document.createElement("div");

    wrapper.className =
        "table-wrapper";

    wrapper.appendChild(table);


    container.innerHTML = "";

    container.appendChild(wrapper);

}


// ============================================================
// 3. LOAD SURPLUS FOOD
// ============================================================

async function loadSurplusFood() {

    const container =
        document.getElementById(
            "surplus-container"
        );

    if (!container) return;

    container.innerHTML =
        "<p>Loading surplus food...</p>";


    try {

        const response =
            await fetch("/api/surplus");

        const data =
            await response.json();


        if (
            !response.ok ||
            data.success === false
        ) {

            throw new Error(
                data.error ||
                "Unable to load surplus food"
            );

        }


        renderDatabaseTable(
            container,
            data,
            "No surplus food found."
        );

    }

    catch (error) {

        console.error(
            "Surplus error:",
            error
        );

        container.innerHTML =
            "<p>❌ Unable to load surplus food.</p>";

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

    if (!container) return;

    container.innerHTML =
        "<p>Loading bakeries...</p>";


    try {

        const response =
            await fetch("/api/bakeries");

        const data =
            await response.json();


        if (
            !response.ok ||
            data.success === false
        ) {

            throw new Error(
                data.error ||
                "Unable to load bakeries"
            );

        }


        renderDatabaseTable(
            container,
            data,
            "No bakeries found."
        );

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

    if (!container) return;

    container.innerHTML =
        "<p>Loading NGOs...</p>";


    try {

        const response =
            await fetch("/api/ngos");

        const data =
            await response.json();


        if (
            !response.ok ||
            data.success === false
        ) {

            throw new Error(
                data.error ||
                "Unable to load NGOs"
            );

        }


        renderDatabaseTable(
            container,
            data,
            "No NGOs found."
        );

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

    if (!container) return;

    container.innerHTML =
        "<p>Loading donations...</p>";


    try {

        const response =
            await fetch("/api/donations");

        const data =
            await response.json();


        if (
            !response.ok ||
            data.success === false
        ) {

            throw new Error(
                data.error ||
                "Unable to load donations"
            );

        }


        renderDatabaseTable(
            container,
            data,
            "No donation records found."
        );

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
// 7. LOAD CUSTOMERS
// ============================================================

async function loadCustomers() {

    const container =
        document.getElementById(
            "customer-container"
        );

    if (!container) return;

    container.innerHTML =
        "<p>Loading customers...</p>";


    try {

        const response =
            await fetch("/api/customers");

        const data =
            await response.json();


        if (
            !response.ok ||
            data.success === false
        ) {

            throw new Error(
                data.error ||
                "Unable to load customers"
            );

        }


        // Display maximum 10 customer records
        renderDatabaseTable(
            container,
            data,
            "No customer records found.",
            10
        );

    }

    catch (error) {

        console.error(
            "Customer error:",
            error
        );

        container.innerHTML =
            "<p>❌ Unable to load customers.</p>";

    }

}


// ============================================================
// 8. COMPLETE BUSINESS ANALYSIS
// ============================================================

async function loadBusinessAnalysis() {

    console.log(
        "Loading complete Business Analysis..."
    );


    try {

        // Everything now comes from FastAPI

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
                    ?.highest_surplus_category ||
                "-";

        }


        if (highestWasteCategory) {

            highestWasteCategory.textContent =
                data.key_findings
                    ?.highest_waste_category ||
                "-";

        }


        // ====================================================
        // TOP BAKERIES
        // ====================================================

        const topBakeriesContainer =
            document.getElementById(
                "top-bakeries-container"
            );


        if (topBakeriesContainer) {

            const rows =
                data.top_bakeries;


            if (
                !Array.isArray(rows) ||
                rows.length === 0
            ) {

                topBakeriesContainer.innerHTML =
                    "<p>No bakery analysis available.</p>";

            }

            else {

                const table =
                    document.createElement(
                        "table"
                    );


                table.className =
                    "data-table analysis-table";


                const thead =
                    document.createElement(
                        "thead"
                    );


                const headerRow =
                    document.createElement(
                        "tr"
                    );


                [
                    {
                        key: "bakery_name",
                        label: "Bakery"
                    },
                    {
                        key: "total_surplus",
                        label: "Total Surplus"
                    }
                ].forEach(column => {

                    const th =
                        document.createElement(
                            "th"
                        );

                    th.textContent =
                        column.label;

                    headerRow.appendChild(th);

                });


                thead.appendChild(
                    headerRow
                );

                table.appendChild(
                    thead
                );


                const tbody =
                    document.createElement(
                        "tbody"
                    );


                rows.forEach(item => {

                    const row =
                        document.createElement(
                            "tr"
                        );


                    [
                        {
                            key: "bakery_name",
                            label: "Bakery"
                        },
                        {
                            key: "total_surplus",
                            label: "Total Surplus"
                        }
                    ].forEach(column => {

                        const td =
                            document.createElement(
                                "td"
                            );


                        const value =
                            item[column.key];


                        td.textContent =
                            value === null ||
                            value === undefined ||
                            value === ""
                                ? "-"
                                : value;


                        row.appendChild(td);

                    });


                    tbody.appendChild(row);

                });


                table.appendChild(
                    tbody
                );


                const wrapper =
                    document.createElement(
                        "div"
                    );


                wrapper.className =
                    "table-wrapper";


                wrapper.appendChild(
                    table
                );


                topBakeriesContainer.innerHTML =
                    "";


                topBakeriesContainer.appendChild(
                    wrapper
                );

            }

        }


        // ====================================================
        // CATEGORY ANALYSIS
        // ====================================================

        const deepercategorycontainer =
            document.getElementById(
                "deeper-category-container"
            );


        if (deepercategorycontainer) {

            const rows =
                data.category_analysis;


            if (
                !Array.isArray(rows) ||
                rows.length === 0
            ) {

                deepercategorycontainer.innerHTML =
                    "<p>No category analysis available.</p>";

            }

            else {

                const table =
                    document.createElement(
                        "table"
                    );


                table.className =
                    "data-table analysis-table";


                const thead =
                    document.createElement(
                        "thead"
                    );


                const headerRow =
                    document.createElement(
                        "tr"
                    );


                [
                    {
                        key: "category",
                        label: "Food Category"
                    },
                    {
                        key: "total_surplus",
                        label: "Total Surplus"
                    },
                    {
                        key: "total_waste",
                        label: "Total Waste"
                    },
                    {
                        key: "average_sales",
                        label: "Average Daily Sales"
                    }
                ].forEach(column => {

                    const th =
                        document.createElement(
                            "th"
                        );


                    th.textContent =
                        column.label;


                    headerRow.appendChild(
                        th
                    );

                });


                thead.appendChild(
                    headerRow
                );


                table.appendChild(
                    thead
                );


                const tbody =
                    document.createElement(
                        "tbody"
                    );


                rows.forEach(item => {

                    const row =
                        document.createElement(
                            "tr"
                        );


                    [
                        {
                            key: "category",
                            label: "Food Category"
                        },
                        {
                            key: "total_surplus",
                            label: "Total Surplus"
                        },
                        {
                            key: "total_waste",
                            label: "Total Waste"
                        },
                        {
                            key: "average_sales",
                            label: "Average Daily Sales"
                        }
                    ].forEach(column => {

                        const td =
                            document.createElement(
                                "td"
                            );


                        const value =
                            item[column.key];


                        td.textContent =
                            value === null ||
                            value === undefined ||
                            value === ""
                                ? "-"
                                : value;


                        row.appendChild(td);

                    });


                    tbody.appendChild(
                        row
                    );

                });


                table.appendChild(
                    tbody
                );


                const wrapper =
                    document.createElement(
                        "div"
                    );


                wrapper.className =
                    "table-wrapper";


                wrapper.appendChild(
                    table
                );


                deepercategorycontainer.innerHTML =
                    "";


                deepercategorycontainer.appendChild(
                    wrapper
                );

            }

        }


        // ====================================================
        // HIGH WASTE PRODUCTS
        // ====================================================

        const highwastecontainer =
            document.getElementById(
                "high-waste-container"
            );


        if (highwastecontainer) {

            const rows =
                data.high_waste_products;


            if (
                !Array.isArray(rows) ||
                rows.length === 0
            ) {

                highwastecontainer.innerHTML =
                    "<p>No high-waste products available.</p>";

            }

            else {

                const table =
                    document.createElement(
                        "table"
                    );


                table.className =
                    "data-table analysis-table";


                const thead =
                    document.createElement(
                        "thead"
                    );


                const headerRow =
                    document.createElement(
                        "tr"
                    );


                [
                    {
                        key: "product",
                        label: "Product"
                    },
                    {
                        key: "category",
                        label: "Category"
                    },
                    {
                        key: "waste",
                        label: "Average Daily Waste"
                    }
                ].forEach(column => {

                    const th =
                        document.createElement(
                            "th"
                        );


                    th.textContent =
                        column.label;


                    headerRow.appendChild(
                        th
                    );

                });


                thead.appendChild(
                    headerRow
                );


                table.appendChild(
                    thead
                );


                const tbody =
                    document.createElement(
                        "tbody"
                    );


                rows.forEach(item => {

                    const row =
                        document.createElement(
                            "tr"
                        );


                    [
                        {
                            key: "product",
                            label: "Product"
                        },
                        {
                            key: "category",
                            label: "Category"
                        },
                        {
                            key: "waste",
                            label: "Average Daily Waste"
                        }
                    ].forEach(column => {

                        const td =
                            document.createElement(
                                "td"
                            );


                        const value =
                            item[column.key];


                        td.textContent =
                            value === null ||
                            value === undefined ||
                            value === ""
                                ? "-"
                                : value;


                        row.appendChild(td);

                    });


                    tbody.appendChild(
                        row
                    );

                });


                table.appendChild(
                    tbody
                );


                const wrapper =
                    document.createElement(
                        "div"
                    );


                wrapper.className =
                    "table-wrapper";


                wrapper.appendChild(
                    table
                );


                highwastecontainer.innerHTML =
                    "";


                highwastecontainer.appendChild(
                    wrapper
                );

            }

        }


        // ====================================================
        // HIGH SURPLUS PRODUCTS
        // ====================================================

        const highsurpluscontainer =
            document.getElementById(
                "high-surplus-container"
            );


        if (highsurpluscontainer) {

            const rows =
                data.high_surplus_products;


            if (
                !Array.isArray(rows) ||
                rows.length === 0
            ) {

                highsurpluscontainer.innerHTML =
                    "<p>No high-surplus products available.</p>";

            }

            else {

                const table =
                    document.createElement(
                        "table"
                    );


                table.className =
                    "data-table analysis-table";


                const thead =
                    document.createElement(
                        "thead"
                    );


                const headerRow =
                    document.createElement(
                        "tr"
                    );


                [
                    {
                        key: "product",
                        label: "Product"
                    },
                    {
                        key: "category",
                        label: "Category"
                    },
                    {
                        key: "surplus",
                        label: "Daily Surplus"
                    }
                ].forEach(column => {

                    const th =
                        document.createElement(
                            "th"
                        );


                    th.textContent =
                        column.label;


                    headerRow.appendChild(
                        th
                    );

                });


                thead.appendChild(
                    headerRow
                );


                table.appendChild(
                    thead
                );


                const tbody =
                    document.createElement(
                        "tbody"
                    );


                rows.forEach(item => {

                    const row =
                        document.createElement(
                            "tr"
                        );


                    [
                        {
                            key: "product",
                            label: "Product"
                        },
                        {
                            key: "category",
                            label: "Category"
                        },
                        {
                            key: "surplus",
                            label: "Daily Surplus"
                        }
                    ].forEach(column => {

                        const td =
                            document.createElement(
                                "td"
                            );


                        const value =
                            item[column.key];


                        td.textContent =
                            value === null ||
                            value === undefined ||
                            value === ""
                                ? "-"
                                : value;


                        row.appendChild(td);

                    });


                    tbody.appendChild(
                        row
                    );

                });


                table.appendChild(
                    tbody
                );


                const wrapper =
                    document.createElement(
                        "div"
                    );


                wrapper.className =
                    "table-wrapper";


                wrapper.appendChild(
                    table
                );


                highsurpluscontainer.innerHTML =
                    "";


                highsurpluscontainer.appendChild(
                    wrapper
                );

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
            "high-surplus-container"

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
// 9. START APPLICATION
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
    // WEBSITE DATA
    // --------------------------------------------------------

    await loadSurplusFood();

    await loadBakeries();

    await loadNGOs();

    await loadDonations();

    await loadCustomers();


    // --------------------------------------------------------
    // COMPLETE BUSINESS ANALYSIS
    // --------------------------------------------------------

    await loadBusinessAnalysis();


    console.log(
        "Plate 2 Plate loaded successfully."
    );

}


// ============================================================
// 10. START WHEN HTML IS READY
// ============================================================

document.addEventListener(
    "DOMContentLoaded",
    loadApplication
);