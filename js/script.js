document.addEventListener('DOMContentLoaded', function() {
    // Language detection and switching
    const userLang = navigator.language || navigator.userLanguage;
    let currentLang = userLang.startsWith('pt') ? 'pt-BR' : 'en-US';
    
    // Set initial language based on browser
    setLanguage(currentLang);
    
    // Language selector buttons
    const langButtons = document.querySelectorAll('.lang-btn');
    langButtons.forEach(btn => {
        if (btn.dataset.lang === currentLang) {
            btn.classList.add('active');
        }
        
        btn.addEventListener('click', function() {
            currentLang = this.dataset.lang;
            setLanguage(currentLang);
            
            // Update active button
            langButtons.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
        });
    });
    
    // Mobile menu toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const nav = document.querySelector('nav');
    
    mobileMenuBtn.addEventListener('click', function() {
        nav.classList.toggle('active');
        this.classList.toggle('active');
    });
    
    // Close mobile menu when clicking on a link
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            nav.classList.remove('active');
            mobileMenuBtn.classList.remove('active');
        });
    });
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                const headerHeight = document.querySelector('header').offsetHeight;
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - headerHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Update Calendly URL based on language
    updateCalendlyUrl(currentLang);
});

// Function to set language
function setLanguage(lang) {
    const isPortuguese = lang.startsWith('pt');
    
    // Update all elements with data-pt and data-en attributes
    document.querySelectorAll('[data-pt][data-en]').forEach(element => {
        element.textContent = isPortuguese ? element.dataset.pt : element.dataset.en;
    });
    
    // Update document language
    document.documentElement.lang = isPortuguese ? 'pt-BR' : 'en-US';
    
    // Update Calendly URL
    updateCalendlyUrl(lang);
}

// Function to update Calendly URL based on language
function updateCalendlyUrl(lang) {
    const calendlyWidget = document.querySelector('.calendly-inline-widget');
    if (calendlyWidget) {
        const baseUrl = 'https://calendly.com/renatomateusx/';
        const urlSuffix = lang.startsWith('pt') ? 'strategic-consultant' : 'strategic-consultant';
        calendlyWidget.setAttribute('data-url', baseUrl + urlSuffix);
        
        // Reload Calendly widget
        if (typeof Calendly !== 'undefined') {
            Calendly.initInlineWidget({
                url: baseUrl + urlSuffix,
                parentElement: calendlyWidget,
                prefill: {},
                utm: {}
            });
        }
    }
}

// Add scroll event listener to handle header styling
window.addEventListener('scroll', function() {
    const header = document.querySelector('header');
    if (window.scrollY > 50) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});
