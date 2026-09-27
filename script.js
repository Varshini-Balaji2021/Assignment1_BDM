function showSection(sectionId) {

    const section = document.getElementById(sectionId);

    section.scrollIntoView({
        behavior: "smooth"
    });

}