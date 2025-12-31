// This is the main JavaScript file
// JavaScript adds interactivity to web pages
// It runs in the browser

// Wait for DOM to load
// NECESSARY: Ensures HTML is loaded before running scripts
// DOM stands for Document Object Model
document.addEventListener('DOMContentLoaded', function () {
    // This function runs when page is loaded
    // All our code goes inside here
    // This prevents errors from trying to access elements that don't exist yet

    // Log to console
    // Console is for debugging
    // You can see this in browser developer tools
    console.log('JavaScript loaded successfully!');

    // Get all navigation links
    // NECESSARY: Selects all anchor tags in nav-links
    const navLinks = document.querySelectorAll('.nav-links a');

    // Log the number of links
    // Just for debugging
    // Not really necessary
    console.log('Number of navigation links:', navLinks.length);

    // Add click event listeners to nav links
    // This adds smooth scrolling effect
    // Well, not really in this case, but it could
    navLinks.forEach(function (link) {
        // For each link
        // Add a click event listener
        // This runs when link is clicked
        link.addEventListener('click', function (e) {
            // e is the event object
            // It contains information about the click
            // We can use it to prevent default behavior

            // Log which link was clicked
            // Debugging purposes
            console.log('Link clicked:', this.href);

            // We're not preventing default here
            // So the link will work normally
            // But we could add custom behavior if needed
        });
    });

    // Get the contact form
    // Only exists on contact page
    // So we check if it exists first
    const contactForm = document.getElementById('contactForm');

    // Check if form exists
    // NECESSARY: Prevents errors on pages without the form
    if (contactForm) {
        // Form exists
        // Add submit event listener
        // This runs when form is submitted
        contactForm.addEventListener('submit', function (e) {
            // Prevent default form submission
            // NECESSARY: Stops page from reloading
            e.preventDefault();

            // Get form values
            // These are the input values
            // We'll use them to display a message
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;

            // Log form data
            // For debugging
            // In real app, you'd send this to server
            console.log('Form submitted!');
            console.log('Name:', name);
            console.log('Email:', email);
            console.log('Message:', message);

            // Show alert
            // NECESSARY: Gives user feedback
            // In real app, you'd show a nicer message
            alert('Thank you for your message, ' + name + '! We will get back to you soon.');

            // Reset form
            // Clears all inputs
            // Good user experience
            contactForm.reset();

            // You could also send data to server here
            // Using fetch API or XMLHttpRequest
            // But this is just a demo
        });
    }

    // Add animation to feature cards
    // When they come into view
    // This is a simple scroll animation

    // Get all feature cards
    // These are on the home page
    const featureCards = document.querySelectorAll('.feature-card');

    // Check if feature cards exist
    // Only on home page
    if (featureCards.length > 0) {
        // Create intersection observer
        // NECESSARY: Detects when elements are visible
        // This is for scroll animations
        const observer = new IntersectionObserver(function (entries) {
            // For each entry
            // Entry is an element being observed
            entries.forEach(function (entry) {
                // Check if element is intersecting
                // Intersecting means it's visible in viewport
                if (entry.isIntersecting) {
                    // Add animation class
                    // This triggers CSS animation
                    // We could add this class in CSS
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';

                    // Stop observing this element
                    // We only want animation to happen once
                    observer.unobserve(entry.target);
                }
            });
        }, {
            // Observer options
            // Threshold is how much of element must be visible
            threshold: 0.1
        });

        // Observe each feature card
        // Set initial state
        featureCards.forEach(function (card) {
            // Set initial opacity
            // Cards start invisible
            card.style.opacity = '0';

            // Set initial transform
            // Cards start below their final position
            card.style.transform = 'translateY(20px)';

            // Add transition
            // NECESSARY: Makes animation smooth
            card.style.transition = 'opacity 0.5s, transform 0.5s';

            // Start observing
            // Observer will trigger when card is visible
            observer.observe(card);
        });
    }

    // Add smooth scroll to top button
    // This is a common feature
    // But we haven't added the button to HTML
    // So this code won't do anything
    // Just here as an example

    // Create scroll to top button
    // This creates a new button element
    const scrollTopBtn = document.createElement('button');

    // Set button text
    // Arrow pointing up
    scrollTopBtn.innerHTML = '↑';

    // Set button ID
    // For styling
    scrollTopBtn.id = 'scrollTopBtn';

    // Set button styles
    // Inline styles
    // Not the best practice, but works for demo
    scrollTopBtn.style.position = 'fixed';
    scrollTopBtn.style.bottom = '20px';
    scrollTopBtn.style.right = '20px';
    scrollTopBtn.style.padding = '10px 15px';
    scrollTopBtn.style.fontSize = '20px';
    scrollTopBtn.style.background = 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)';
    scrollTopBtn.style.color = 'white';
    scrollTopBtn.style.border = 'none';
    scrollTopBtn.style.borderRadius = '50%';
    scrollTopBtn.style.cursor = 'pointer';
    scrollTopBtn.style.display = 'none';  // Hidden by default
    scrollTopBtn.style.zIndex = '1000';
    scrollTopBtn.style.transition = 'opacity 0.3s';

    // Add button to page
    // Appends to body
    document.body.appendChild(scrollTopBtn);

    // Show/hide button based on scroll position
    // NECESSARY: Button only shows when user scrolls down
    window.addEventListener('scroll', function () {
        // Check scroll position
        // If scrolled more than 300px
        if (window.pageYOffset > 300) {
            // Show button
            scrollTopBtn.style.display = 'block';
        } else {
            // Hide button
            scrollTopBtn.style.display = 'none';
        }
    });

    // Add click event to scroll to top
    // When button is clicked
    scrollTopBtn.addEventListener('click', function () {
        // Scroll to top
        // NECESSARY: Smooth scroll behavior
        window.scrollTo({
            top: 0,  // Scroll to top
            behavior: 'smooth'  // Smooth animation
        });
    });

    // Add hover effect to button
    // Mouse enter event
    scrollTopBtn.addEventListener('mouseenter', function () {
        // Change opacity on hover
        this.style.opacity = '0.8';
    });

    // Mouse leave event
    scrollTopBtn.addEventListener('mouseleave', function () {
        // Reset opacity
        this.style.opacity = '1';
    });

    // Log that setup is complete
    // For debugging
    console.log('All JavaScript setup complete!');

    // You could add more features here:
    // - Form validation
    // - AJAX requests
    // - Dynamic content loading
    // - Animations
    // - And much more!

}); // End of DOMContentLoaded event listener

// This is outside the DOMContentLoaded
// Code here runs immediately
// Before DOM is ready

// Function to fetch API data
// This is just a demo function
// It's not called anywhere
function fetchAPIData() {
    // Fetch data from our API endpoint
    // NECESSARY: Uses fetch API to get data
    fetch('/api/data/')
        .then(function (response) {
            // Convert response to JSON
            // Response is a promise
            return response.json();
        })
        .then(function (data) {
            // Log the data
            // This is the actual data from API
            console.log('API Data:', data);

            // You could do something with the data here
            // Like display it on the page
            // But this is just a demo
        })
        .catch(function (error) {
            // Handle errors
            // If fetch fails
            console.error('Error fetching data:', error);
        });
}

// Another utility function
// Not used anywhere
// Just for demonstration
function showNotification(message) {
    // Create notification element
    const notification = document.createElement('div');

    // Set message
    notification.textContent = message;

    // Style the notification
    notification.style.position = 'fixed';
    notification.style.top = '20px';
    notification.style.right = '20px';
    notification.style.padding = '1rem 2rem';
    notification.style.background = '#667eea';
    notification.style.color = 'white';
    notification.style.borderRadius = '5px';
    notification.style.boxShadow = '0 5px 15px rgba(0,0,0,0.2)';
    notification.style.zIndex = '9999';

    // Add to page
    document.body.appendChild(notification);

    // Remove after 3 seconds
    // NECESSARY: Auto-hide notification
    setTimeout(function () {
        // Fade out
        notification.style.opacity = '0';
        notification.style.transition = 'opacity 0.3s';

        // Remove from DOM
        setTimeout(function () {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// End of JavaScript file
// Lots of comments here too!
// Some necessary, some not
// But all educational!
