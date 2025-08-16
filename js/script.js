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

// Function to open Zoho chat
function openZohoChat() {
    if (typeof $zoho !== 'undefined' && $zoho.salesiq) {
        // Try different methods to show the chat
        if ($zoho.salesiq.floatbutton && $zoho.salesiq.floatbutton.visible) {
            $zoho.salesiq.floatbutton.visible('show');
        } else if ($zoho.salesiq.show) {
            $zoho.salesiq.show();
        } else if ($zoho.salesiq.open) {
            $zoho.salesiq.open();
        } else {
            // Try to trigger the default Zoho button
            var zohoButton = document.querySelector('[id*="zsiq"], [class*="zsiq"]');
            if (zohoButton) {
                zohoButton.click();
            } else {
                showWhatsAppFallback();
            }
        }
    } else {
        showWhatsAppFallback();
    }
}

// Function to show WhatsApp as fallback
function showWhatsAppFallback() {
    const whatsappButton = document.querySelector('.whatsapp-float');
    if (whatsappButton) {
        whatsappButton.style.display = 'block';
    }
}

// Check if Zoho script loaded successfully
document.addEventListener('DOMContentLoaded', function() {
    // Wait a bit for Zoho to load
    setTimeout(function() {
        if (typeof $zoho === 'undefined' || !$zoho.salesiq) {
            console.log('Zoho not loaded, showing WhatsApp fallback');
            showWhatsAppFallback();
        }
    }, 3000); // Wait 3 seconds for Zoho to load
    zsfeedbackwidgetdivFunction();
});

// Forçar CSS do botão Zoho após 3 segundos
setTimeout(function() {
    zsfeedbackwidgetdivFunction();
}, 5000);

function zsfeedbackwidgetdivFunction() {
    console.log('zsfeedbackwidgetdivFunction');
    const zsfeedbackwidgetdiv = document.getElementById('zsfeedbackwidgetdiv');
    console.log(zsfeedbackwidgetdiv);
    if (zsfeedbackwidgetdiv) {
        console.log('zsfeedbackwidgetdiv found');
        zsfeedbackwidgetdiv.style.width = '100%';
        // CSS responsivo baseado no tamanho da tela
        if (window.innerWidth <= 768) {
            // Mobile e tablet
            zsfeedbackwidgetdiv.style.width = '690px';
            zsfeedbackwidgetdiv.style.maxWidth = '100%';
        }
        
        if (window.innerWidth <= 576) {
            // Mobile pequeno
            zsfeedbackwidgetdiv.style.width = '100%';
        }
        
        if (window.innerWidth <= 480) {
            // Mobile muito pequeno
            zsfeedbackwidgetdiv.style.width = '100%';
            zsfeedbackwidgetdiv.style.fontSize = '12px';
        }
    }
}

// Executar quando a janela carregar completamente
window.addEventListener('load', function() {
    hideZohoFeedbackButton();
    
    // Executar após delays específicos para garantir que o Zoho carregou
    setTimeout(hideZohoFeedbackButton, 3000);  // 3 segundos (principal)
    setTimeout(hideZohoFeedbackButton, 5000);  // 5 segundos (backup)
    setTimeout(hideZohoFeedbackButton, 10000); // 10 segundos (backup final)
});

// Solução para problema de CORS com fontes do Zoho
function loadZohoFonts() {
    // Lista de fontes do Zoho que podem dar erro CORS
    const zohoFonts = [
        'https://js.zohostatic.com/support/fbw_v20/fonts/LatoLatin-Regular.woff2',
        'https://js.zohostatic.com/support/fbw_v20/fonts/LatoLatin-Bold.woff2',
        'https://js.zohostatic.com/support/fbw_v20/fonts/LatoLatin-Italic.woff2'
    ];
    
    zohoFonts.forEach(fontUrl => {
        // Criar link para fonte
        const fontLink = document.createElement('link');
        fontLink.rel = 'stylesheet';
        fontLink.href = fontUrl;
        fontLink.crossOrigin = 'anonymous';
        
        // Adicionar ao head
        document.head.appendChild(fontLink);
        
        // Tratar erro de CORS
        fontLink.onerror = function() {
            console.log('Fonte Zoho não carregou:', fontUrl);
            // Remover link que falhou
            document.head.removeChild(fontLink);
        };
        
        fontLink.onload = function() {
            console.log('Fonte Zoho carregada com sucesso:', fontUrl);
        };
    });
}

// Executar solução de fontes após carregamento
document.addEventListener('DOMContentLoaded', function() {
    // Aguardar um pouco para o Zoho carregar
    setTimeout(loadZohoFonts, 2000);
});

// Executar também no load da janela
window.addEventListener('load', function() {
    setTimeout(loadZohoFonts, 1000);
});
