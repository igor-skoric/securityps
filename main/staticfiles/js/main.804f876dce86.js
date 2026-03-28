const { createApp, mounted, beforeUnmount } = Vue;

// Globalna Vue instanca za registraciju komponenti
const app = createApp({ delimiters: ['[[', ']]'] });

// Funkcija za mount svake stranice
function mountPage(selector, options) {
    if (document.querySelector(selector)) {
        createApp({
            delimiters: ['[[', ']]'],
            ...options
        }).mount(selector);
    }
}

// Header
mountPage('#app-header', {
  data() {
    return {
      scrolled: false,
      menuOpen: false,
      topHeight: 0
    };
  },
  methods: {
    toggleMenu() {
      this.menuOpen = !this.menuOpen;
    },
    handleScroll() {
      this.scrolled = window.scrollY > 50;
    },
    updateTopHeight() {
      this.topHeight = this.$refs.topHeader.offsetHeight;
    }
  },
  mounted() {
    this.updateTopHeight();
    window.addEventListener('scroll', this.handleScroll);
    window.addEventListener('resize', this.updateTopHeight);
  },
  beforeUnmount() {
    window.removeEventListener('scroll', this.handleScroll);
    window.removeEventListener('resize', this.updateTopHeight);
  },
});


// Footer
mountPage('#app-footer', {
    data() {
        return {
            message: 'Ovo je Footer',
        }
    },
    methods: {
    }
});

mountPage('#app-home', {
  delimiters: ['[[', ']]'],
  data() {
    return {
      currentIndex: 0,
      autoSlideInterval: null,
      slideDuration: 5000,
      slides: [
        {
            image: "/static/img/slider/slider1.jpg",
            mobile: "/static/img/slider/slider1.jpg",
            title: "Obezbedite svoje poslovanje"
        },
        {
            image: "/static/img/slider/slider2.jpg",
            mobile: "/static/img/slider/slider2-mobile.jpg"
        }
      ]
    };
  },

  methods: {
    nextSlide() {
      this.currentIndex = (this.currentIndex + 1) % this.slides.length;
    },

    prevSlide() {
      this.currentIndex = (this.currentIndex - 1 + this.slides.length) % this.slides.length;
    },

    goToSlide(index) {
      this.currentIndex = index;
    },

    startAuto() {
      this.stopAuto();
      this.autoSlideInterval = setInterval(() => {
        this.nextSlide();
      }, this.slideDuration);
    },

    pauseAuto() {
      this.stopAuto();
    },

    stopAuto() {
      if (this.autoSlideInterval) {
        clearInterval(this.autoSlideInterval);
        this.autoSlideInterval = null;
      }
    }
  },

  mounted() {
    this.startAuto();
  },

  beforeUnmount() {
    this.stopAuto();
  }
});

mountPage('#app-single-services', {
  data() {
    return {
      currentIndex2: 0,
      tabs: [
        {
          title: 'Telesna zaštita (Bodyguard)',
          text: 'Naši profesionalni telohranitelji pružaju potpunu fizičku zaštitu klijenata, uz diskretan pristup i visok stepen obučenosti. Svaki član tima prolazi kroz specijalizovane treninge za procenu rizika, prepoznavanje potencijalnih pretnji i brzo reagovanje u kriznim situacijama. Cilj nam je da osiguramo vašu sigurnost, ali i da održimo vašu slobodu kretanja i svakodnevnu rutinu bez ometanja.'
        },
        {
          title: 'Obezbeđenje događaja',
          text: 'Za javne i privatne događaje pružamo sveobuhvatno obezbeđenje koje obuhvata kontrolu pristupa, nadzor publike, koordinaciju sa organizatorima i brzu reakciju na svaku nepredviđenu situaciju. Naši timovi deluju nenametljivo, ali efikasno, osiguravajući da vaš događaj protekne bez incidenata i u potpunoj bezbednosti svih učesnika.'
        },
        {
          title: 'VIP i korporativna zaštita',
          text: 'Specijalizovani smo za zaštitu poslovnih ljudi, diplomata i javnih ličnosti. Naš pristup je baziran na proceni rizika i planiranju bezbednosnih ruta, sa posebnim naglaskom na preventivu. Diskrecija, profesionalizam i poverenje predstavljaju temelje našeg delovanja, dok klijent u svakom trenutku ima osećaj sigurnosti i kontrole.'
        },
        {
          title: 'Transport novca i dragocenosti',
          text: 'Pružamo sigurnu i osiguranu uslugu prevoza gotovine, dokumenata i vrednih predmeta. Naši specijalizovani timovi koriste oklopna vozila i modernu GPS tehnologiju za praćenje, čime obezbeđujemo potpunu kontrolu i zaštitu tokom transporta. Svaka isporuka se planira unapred i sprovodi prema najvišim bezbednosnim standardima.'
        },
        {
          title: 'Tehnička zaštita i nadzor',
          text: 'Pored fizičkog prisustva, nudimo i integrisana tehnička rešenja – video nadzor, alarmne sisteme i kontrolu pristupa. Naš tim projektuje i implementira sisteme koji odgovaraju konkretnim potrebama klijenta, uz 24/7 nadzor i brzu reakciju u slučaju ugrožavanja bezbednosti. Tehnologija i ljudski faktor čine savršenu kombinaciju zaštite.'
        }
      ]
    };
  }
});




