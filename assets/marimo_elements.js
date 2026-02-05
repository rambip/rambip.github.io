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
    this._currentIndex = 0;
    this._slides = [];
    this._initialized = false;
  }

  connectedCallback() {
    // Use setTimeout to ensure all children are loaded
    setTimeout(() => {
      if (!this._initialized) {
        this._initialize();
      }
    }, 0);
  }

  _initialize() {
    this._initialized = true;
    
    // Setup container styles
    this.style.display = "block";
    this.style.position = "relative";
    this.style.width = "100%";
    this.style.height = this.getAttribute("height") || "550px";
    this.style.border = "1px solid #e5e7eb";
    this.style.borderRadius = "0.5rem";
    this.style.backgroundColor = "var(--background, #fff)";

    // Get all original children as slides
    this._slides = Array.from(this.children);
    
    if (this._slides.length === 0) return;

    // Wrap all slides in containers and hide them
    this._slides.forEach((slide, index) => {
      slide.style.position = "absolute";
      slide.style.top = "0";
      slide.style.left = "0";
      slide.style.width = "100%";
      slide.style.height = "100%";
      slide.style.padding = "1.5rem";
      slide.style.paddingBottom = "3rem";
      slide.style.boxSizing = "border-box";
      slide.style.overflowY = "auto";
      slide.style.overflowX = "hidden";
      slide.style.display = index === this._currentIndex ? "block" : "none";
    });

    // Create navigation controls
    this._createControls();
    
    // Setup keyboard navigation
    this.setAttribute("tabindex", "0");
    this.addEventListener("keydown", (e) => {
      if (e.key === "ArrowLeft") {
        e.preventDefault();
        this._navigate(-1);
      } else if (e.key === "ArrowRight") {
        e.preventDefault();
        this._navigate(1);
      }
    });
  }

  _createControls() {
    // Previous button
    const prevBtn = document.createElement("button");
    prevBtn.innerHTML = "❮";
    prevBtn.style.cssText = `
      position: absolute;
      top: 50%;
      left: 1rem;
      transform: translateY(-50%);
      z-index: 100;
      background-color: rgba(255, 255, 255, 0.9);
      border: 1px solid #e5e7eb;
      border-radius: 0.375rem;
      padding: 0.5rem 0.75rem;
      cursor: pointer;
      font-size: 1.25rem;
      line-height: 1;
      color: #374151;
    `;
    prevBtn.onclick = () => this._navigate(-1);

    // Next button
    const nextBtn = document.createElement("button");
    nextBtn.innerHTML = "❯";
    nextBtn.style.cssText = `
      position: absolute;
      top: 50%;
      right: 1rem;
      transform: translateY(-50%);
      z-index: 100;
      background-color: rgba(255, 255, 255, 0.9);
      border: 1px solid #e5e7eb;
      border-radius: 0.375rem;
      padding: 0.5rem 0.75rem;
      cursor: pointer;
      font-size: 1.25rem;
      line-height: 1;
      color: #374151;
    `;
    nextBtn.onclick = () => this._navigate(1);

    // Pagination container
    const pagination = document.createElement("div");
    pagination.style.cssText = `
      position: absolute;
      bottom: 1rem;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      gap: 0.5rem;
      z-index: 100;
    `;

    // Create dots
    this._dots = [];
    this._slides.forEach((_, index) => {
      const dot = document.createElement("button");
      dot.style.cssText = `
        width: 0.5rem;
        height: 0.5rem;
        border-radius: 50%;
        border: none;
        cursor: pointer;
        padding: 0;
        background-color: ${index === this._currentIndex ? "#3b82f6" : "#d1d5db"};
      `;
      dot.onclick = () => this._goToSlide(index);
      pagination.appendChild(dot);
      this._dots.push(dot);
    });

    this.appendChild(prevBtn);
    this.appendChild(nextBtn);
    this.appendChild(pagination);
  }

  _navigate(delta) {
    const newIndex = (this._currentIndex + delta + this._slides.length) % this._slides.length;
    this._goToSlide(newIndex);
  }

  _goToSlide(index) {
    if (index === this._currentIndex || index < 0 || index >= this._slides.length) return;
    
    this._slides[this._currentIndex].style.display = "none";
    this._currentIndex = index;
    this._slides[this._currentIndex].style.display = "block";
    
    // Update dots
    this._dots.forEach((dot, i) => {
      dot.style.backgroundColor = i === this._currentIndex ? "#3b82f6" : "#d1d5db";
    });
  }
}

customElements.define("marimo-carousel", MarimoCarousel);
