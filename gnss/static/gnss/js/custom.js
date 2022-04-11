class MyHeader extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `
    <nav class="nav">
    <div class="nav-menu flex-row">
        <div class="nav-brand">
            <a href="../Index.html" class="text-gray">GNSS</a>
        </div>
        <div class="toggle-collapse">
            <div class="toggle-icons">
                <i class="fas fa-bars"></i>
            </div>
        </div>
        <div>
            <ul class="nav-items">
                <li class="nav-link">
                  <li class="nav-link">
                    <a href="gnss.html">Gnss</a>
                </li>
                <li class="nav-link">
                  <a href="beidou.html">GLONASS</a>
                </li>  
                <li class="nav-link">
                    <a href="galileo.html">GALILEO</a>
                </li>
                <li class="nav-link">
                    <a href="beidou.html">BEIDOU</a>
                </li>
                <li class="nav-link">
                    <a href="gps.html">GPS</a>
                </li>
                <li class="nav-link">
                    <a href="irnss.html">IRNSS</a>
                </li>
            </ul>
        </div>
        <div class="social text-gray">
            <a href="../login.html">Login/Register</a>
            
        </div>
    </div>
</nav>
           
        
        `
  }
}

customElements.define("my-header", MyHeader);

class MyFooter extends HTMLElement {
    connectedCallback() {
      this.innerHTML = `
      <footer class="footer">
        <div class="container">
            <div class="about-us" data-aos="fade-right" data-aos-delay="200">
                <h2>ABOUT US</h2>  
            </div>
            <div class="newsletter" data-aos="fade-right" data-aos-delay="200">
                <h2>CONTACT US</h2>
            </div>
            <div class="instagram" data-aos="fade-left" data-aos-delay="200">
                <h2>FAQ</h2>
   
                
            </div>
            <div class="follow" data-aos="fade-left" data-aos-delay="200">
                <h2>FEEDBACK</h2>
        
            </div>
        </div>
        <div class="rights flex-row">
            <h4 class="text-gray">
                Copyright ©2021 All rights reserved
            </h4>
        </div>
        <div class="move-up">
            <span><i class="fas fa-arrow-circle-up fa-2x"></i></span>
        </div>
    </footer>

             
          
          `
    }
  }
  
  customElements.define("my-footer", MyFooter);
