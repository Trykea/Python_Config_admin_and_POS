document.addEventListener('DOMContentLoaded', function () {
    // Your existing code here
    // index.js

    const links = document.querySelectorAll('.nav_link');

    function handleLinkClick(event) {

        console.log("log")
        // Remove the class from all links
        links.forEach(link => link.classList.remove('bg-gray-900'));

        // Add the class to the clicked link
        event.target.classList.add('bg-gray-900');
    }

// Attach the click event listener to each link
    links.forEach(link => {

        link.addEventListener('click', handleLinkClick);

    });

});
