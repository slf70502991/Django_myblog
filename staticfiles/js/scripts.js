
    const nav= document.querySelector('#main');
    // let topofNav = nav.offsetTop; 
    
    const slideImages = document.querySelectorAll('.slide-in');
    const li = document.querySelectorAll('li.menu');
    const ham = document.querySelector('.ham');
    const logo = document.querySelector('li.logo');
    function toCross(x) {
    x.classList.toggle("change");

    
    }
    function show(){
        li.forEach(i=>{
            i.classList.toggle('show');
        }); 
    }
    ham.addEventListener('click', show);
    
    
    function fixNav(){
        if (window.scrollY >= 100){
            document.body.style.paddingTop = nav.offsetHeight + 'px';
            document.body.classList.add('fixed-nav');
            
        }else{
            document.body.classList.remove('fixed-nav');
            // nav.classList.remove('fixed-nav');
            document.body.style.paddingTop = 0;
        }
    }
    
    
    function debounce(func, wait = 10, immediate = true){
        var timeout;
        return function(){
            var context = this, args = arguments;
            var later = function(){
                timeout = null;
                if(!immediate) func.apply(context, args);
            };
            var callNow = immediate & !timeout;
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
            if(callNow) func.apply(context, args);
            
        };
    };
    
    function checkSlide(){
        slideImages.forEach(slideImage => {
            const slideInAt = (window.scrollY + window.innerHeight) - slideImage.height /2;
            const imageBottom = slideImage.offsetTop + slideImage.height;
            const isHalfShown = slideInAt > slideImage.offsetTop;
            const isNotScrolledPast = window.scrollY < imageBottom;
            console.log(slideImage.classList);
            if(isHalfShown && isNotScrolledPast){
                slideImage.classList.add('active');
            }else{
                slideImage.classList.remove('active');
            }
        });
    }
    

    
    window.addEventListener('scroll', fixNav);
    window.addEventListener('scroll', debounce(checkSlide));
