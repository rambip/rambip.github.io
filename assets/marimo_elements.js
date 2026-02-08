class MarimoMermaid extends HTMLElement {
  constructor() {
    super();
    this._id = this._randomAlpha();
    this._diagram = "";
    this._darkMode = false;
  }

  static get observedAttributes() {
    return ["data-diagram", "dark-mode"];
  }

  connectedCallback() {
    this._updateDiagram();
    this._render();
  }

  attributeChangedCallback(name, oldValue, newValue) {
    if (oldValue === newValue) return;

    if (name === "data-diagram") {
      this._updateDiagram();
    } else if (name === "dark-mode") {
      this._darkMode = newValue === "true";
    }

    if (this.isConnected) {
      this._render();
    }
  }

  _updateDiagram() {
    const raw = this.getAttribute("data-diagram") || "";

    // The attribute value is a JSON-encoded string
    try {
      this._diagram = JSON.parse(raw);
    } catch {
      // Fallback: use as-is
      this._diagram = raw;
    }
  }

  _randomAlpha() {
    const alphabet = "abcdefghijklmnopqrstuvwxyz";
    return Array.from(
      { length: 6 },
      () => alphabet[Math.floor(Math.random() * alphabet.length)],
    ).join("");
  }

  async _render() {
    if (!this._diagram) {
      this.innerHTML = "";
      return;
    }

    const config = {
      startOnLoad: true,
      theme: this._darkMode ? "dark" : "forest",
      darkMode: this._darkMode,
      logLevel: "fatal",
      securityLevel: "strict",
      fontFamily: "var(--text-font)",
      arrowMarkerAbsolute: false,
      flowchart: {
        htmlLabels: true,
        curve: "linear",
      },
      sequence: {
        diagramMarginX: 50,
        diagramMarginY: 10,
        actorMargin: 50,
        width: 150,
        height: 65,
        boxMargin: 10,
        boxTextMargin: 5,
        noteMargin: 10,
        messageMargin: 35,
        mirrorActors: true,
        bottomMarginAdj: 1,
        useMaxWidth: true,
        rightAngles: false,
        showSequenceNumbers: false,
      },
      gantt: {
        titleTopMargin: 25,
        barHeight: 20,
        barGap: 4,
        topPadding: 50,
        leftPadding: 75,
        gridLineStartPadding: 35,
        fontSize: 11,
        numberSectionStyles: 4,
        axisFormat: "%Y-%m-%d",
      },
    };

    if (typeof mermaid !== "undefined") {
      mermaid.initialize(config);

      try {
        const result = await mermaid.render(this._id, this._diagram, undefined);
        this.innerHTML = result.svg;
      } catch (error) {
        document.getElementById(this._id)?.remove();
        console.warn("Failed to render mermaid diagram", error);
        this.innerHTML = "";
      }
    } else {
      console.error("Mermaid library not loaded");
    }
  }
}

customElements.define("marimo-mermaid", MarimoMermaid);
class MarimoTex extends HTMLElement {
  connectedCallback() {
    // Wait for content to be available
    setTimeout(() => {
      const latex = this.textContent.slice(3, -3);
      if (!latex) return;

      this.innerHTML = "";
      katex.render(latex, this, {
        throwOnError: false,
        displayMode: this.hasAttribute("display"),
      });
    }, 0);
  }
}

customElements.define("marimo-tex", MarimoTex);

class MarimoCarousel extends HTMLElement {
  constructor() {
    super();
    this.currentIndex = 0;
    this.attachShadow({ mode: 'open' });
  }

  connectedCallback() {
    // Use setTimeout to ensure all children are loaded
    setTimeout(() => {
      this.render();
      this.setupEventListeners();
    }, 0);
  }

  render() {
    const height = this.getAttribute("height") || "550px";
    
    const style = `
      <style>
        :host {
          display: block;
          position: relative;
          width: 100%;
          height: ${height};
          border: 1px solid #e5e7eb;
          border-radius: 0.5rem;
          background-color: var(--background, #fff);
          overflow: hidden;
        }

        .carousel-container {
          position: relative;
          width: 100%;
          height: 100%;
        }

        .carousel-content {
          position: relative;
          width: 100%;
          height: 100%;
        }

        /* Using position absolute stacks all slides on top of each other.
           This means the carousel height is fixed (not dependent on content),
           and we must handle overflow for each slide independently. */
        ::slotted(*) {
          position: absolute !important;
          top: 0 !important;
          left: 0 !important;
          width: 100% !important;
          height: 100% !important;
          padding: 1.5rem !important;
          padding-bottom: 3rem !important;
          box-sizing: border-box !important;
          overflow-y: auto !important;
          overflow-x: hidden !important;
          display: none !important;
        }

        ::slotted(.active) {
          display: block !important;
        }

        .carousel-controls {
          position: absolute;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
          pointer-events: none;
        }

        .carousel-btn {
          pointer-events: auto;
          position: absolute;
          top: 0;
          height: 100%;
          z-index: 100;
          background-color: rgba(255, 255, 255, 0.9);
          border: 1px solid #e5e7eb;
          border-radius: 0.375rem;
          padding: 0 1rem;
          cursor: pointer;
          font-size: 1.5rem;
          color: #374151;
          transition: background-color 0.2s;
          display: flex;
          align-items: center;
          justify-content: center;
        }

        .carousel-btn:hover {
          background-color: rgba(255, 255, 255, 1);
        }

        .carousel-btn.prev {
          left: 0;
          border-left: none;
          border-top-left-radius: 0.5rem;
          border-bottom-left-radius: 0.5rem;
          border-top-right-radius: 0;
          border-bottom-right-radius: 0;
        }

        .carousel-btn.next {
          right: 0;
          border-right: none;
          border-top-right-radius: 0.5rem;
          border-bottom-right-radius: 0.5rem;
          border-top-left-radius: 0;
          border-bottom-left-radius: 0;
        }

        .pagination {
          pointer-events: auto;
          position: absolute;
          bottom: 1rem;
          left: 50%;
          transform: translateX(-50%);
          display: flex;
          gap: 0.5rem;
          z-index: 100;
        }

        .dot {
          width: 0.5rem;
          height: 0.5rem;
          border-radius: 50%;
          border: none;
          cursor: pointer;
          padding: 0;
          background-color: #d1d5db;
          transition: background-color 0.2s;
        }

        .dot.active {
          background-color: #3b82f6;
        }

        .dot:hover {
          background-color: #9ca3af;
        }

        .dot.active:hover {
          background-color: #2563eb;
        }
      </style>
    `;

    const template = `
      ${style}
      <div class="carousel-container">
        <div class="carousel-content">
          <slot></slot>
        </div>
        <div class="carousel-controls">
          <button class="carousel-btn prev" aria-label="Previous slide">❮</button>
          <button class="carousel-btn next" aria-label="Next slide">❯</button>
          <div class="pagination"></div>
        </div>
      </div>
    `;

    this.shadowRoot.innerHTML = template;
    this.createPaginationDots();
  }

  createPaginationDots() {
    const pagination = this.shadowRoot.querySelector('.pagination');
    const children = this.getChildren();
    
    children.forEach((_, index) => {
      const dot = document.createElement('button');
      dot.className = 'dot';
      dot.setAttribute('aria-label', `Go to slide ${index + 1}`);
      if (index === this.currentIndex) {
        dot.classList.add('active');
      }
      dot.addEventListener('click', () => this.goTo(index));
      pagination.appendChild(dot);
    });
  }

  setupEventListeners() {
    const prevBtn = this.shadowRoot.querySelector('.prev');
    const nextBtn = this.shadowRoot.querySelector('.next');

    prevBtn.addEventListener('click', () => this.prev());
    nextBtn.addEventListener('click', () => this.next());

    // Keyboard navigation - requires element to be focusable
    this.setAttribute('tabindex', '0');
    this.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft') {
        e.preventDefault();
        this.prev();
      } else if (e.key === 'ArrowRight') {
        e.preventDefault();
        this.next();
      }
    });

    // Initialize: show first child
    this.updateDisplay();
  }

  getChildren() {
    return Array.from(this.children);
  }

  updateDisplay() {
    const children = this.getChildren();
    const dots = this.shadowRoot.querySelectorAll('.dot');
    
    children.forEach((child, index) => {
      if (index === this.currentIndex) {
        child.classList.add('active');
      } else {
        child.classList.remove('active');
      }
    });

    dots.forEach((dot, index) => {
      if (index === this.currentIndex) {
        dot.classList.add('active');
      } else {
        dot.classList.remove('active');
      }
    });
  }

  next() {
    const children = this.getChildren();
    if (children.length === 0) return;
    
    this.currentIndex = (this.currentIndex + 1) % children.length;
    this.updateDisplay();
  }

  prev() {
    const children = this.getChildren();
    if (children.length === 0) return;
    
    this.currentIndex = (this.currentIndex - 1 + children.length) % children.length;
    this.updateDisplay();
  }

  goTo(index) {
    const children = this.getChildren();
    if (index >= 0 && index < children.length) {
      this.currentIndex = index;
      this.updateDisplay();
    }
  }
}

customElements.define("marimo-carousel", MarimoCarousel);
